import sys
import random
from argparse import ArgumentParser

import hoard_tables
import magic_tables
import mundane_tables
import magic_mappings
import mundane_mappings

cp_values = {"cp": 1, "sp": 10, "gp": 100, "pp": 1000}
cp_values.update(mundane_mappings.cp_values)
cp_values.update(magic_mappings.cp_values)


class TreasureHoard:
    """repository of all treasue in the hoard, with I/O methods"""

    cp = 0
    sp = 0
    gp = 0
    pp = 0
    mundane_treasures_by_category = dict(zip(mundane_mappings.categories,
                                        [{} for i in range(len(mundane_mappings.categories))]))
    magic_treasures_by_rarity = dict(zip(magic_mappings.magic_rarities,
                                    [{} for i in range(len(magic_mappings.magic_rarities))]))

    def increment_counts(self, treasure_counts, treasures):
        """increase stored counts of given items"""
        for treasure in treasures:
            if treasure in treasure_counts:
                treasure_counts[treasure] +=1
            else:
                treasure_counts[treasure] = 1

    def print_counts(self, treasure_counts):
        """print list of item counts and items, with even spacing"""
        if treasure_counts:
            max_count = max(treasure_counts.values())
            characters_in_max_count = len(str(max_count))
            for treasure in sorted(treasure_counts):
                print("    {0:{width}} {1}".format(treasure_counts[treasure], treasure, width=characters_in_max_count))
        else:
            print()

    def get_total_cp_value(self):
        """sum all treasure value, in cp units"""
        total = self.cp
        total += cp_values["sp"] * self.sp
        total += cp_values["gp"] * self.gp
        total += cp_values["pp"] * self.pp
        for treasure_grouping in [self.mundane_treasures_by_category, self.magic_treasures_by_rarity]:
            for treasure_type, treasure_counts in treasure_grouping.items():
                total += cp_values[treasure_type] * sum(treasure_counts.values())
        return total

    def add_mundane_treasures(self, treasures):
        """record new mundane items in treasure group"""
        for treasure in treasures:
            category = mundane_mappings.qualities[treasure][0]
            self.increment_counts(self.mundane_treasures_by_category[category], [treasure])

    def add_magic_treasures(self, treasures):
        """record new magic items in treasure group"""
        for treasure in treasures:
            rarity = magic_mappings.magic_qualities[treasure][0]
            self.increment_counts(self.magic_treasures_by_rarity[rarity], [treasure])

    def print_result(self):
        """print all treasure to formatted style"""
        print("COINS: ")
        print("  cp: {}".format(self.cp))
        print("  sp: {}".format(self.sp))
        print("  gp: {}".format(self.gp))
        print("  pp: {}".format(self.pp))
        print()
        print("MUNDANE ITEMS: ")
        for category, treasure_counts in self.mundane_treasures_by_category.items():
            if treasure_counts:
                print("  {}:".format(category))
                self.print_counts(treasure_counts)
        print()
        print("MAGIC ITEMS: ")
        for rarity, treasure_counts in self.magic_treasures_by_rarity.items():
            if treasure_counts:
                print("  {}:".format(rarity))
                self.print_counts(treasure_counts)
        print()
        print("TOTAL VALUE:")
        print("  gp: {}".format(round(self.get_total_cp_value() / 100)))
        print()


def roll_die(max, rolls):
    """simulate and sum a series of die rolls"""
    if max == 1:
        return rolls

    total = 0
    for r in range(rolls):
        total += random.randrange(1, max, 1)
    return total


def roll_on_table(table):
    """randomly choose an item from the given table"""
    if len(table) == 1:
        return table[0]

    return table[roll_die(len(table), 1)]


def get_treasures(treasure_type, table_name, die_type, die_count):
    """'roll' on the given table of treasure items"""
    treasures = []
    table_rolls = roll_die(die_type, die_count)
    for roll_counter in range(table_rolls):
        table_result = []
        if treasure_type == "mundane":
            table_result = roll_on_table(mundane_tables.tables[table_name])
        elif treasure_type == "magic":
            table_result = roll_on_table(magic_tables.tables[table_name])
        else:
            print("ERROR: unrecognized treasure type")
            exit()
        # Some table rows have additional possibilities, 
        # so all rows are returned as a list to be rolled on
        treasures += [roll_on_table(table_result)]
    return treasures


def roll_on_hoard_table(table_name, hoard):
    hoard_table_row = roll_on_table(table_name)
    mundane_instructions = hoard_table_row[0]
    for instruction in mundane_instructions:
        mundane_treasures = get_treasures("mundane", *instruction)
        hoard.add_mundane_treasures(mundane_treasures)
    magic_instructions = hoard_table_row[1]
    for instruction in magic_instructions:
        magic_treasures = get_treasures("magic", *instruction)
        hoard.add_magic_treasures(magic_treasures)


def roll_table_one(rolls, hoard):
    """'roll' on the hoard table for CR 0-4 and record the result"""
    for roll_counter in range(rolls):
        hoard.cp += roll_die(6, 6) * 100
        hoard.sp += roll_die(6, 3) * 100
        hoard.gp += roll_die(6, 2) * 10
        roll_on_hoard_table(hoard_tables.table_one, hoard)


def roll_table_two(rolls, hoard):
    """'roll' on the hoard table for CR 5-10 and record the result"""
    for roll_counter in range(rolls):
        hoard.cp += roll_die(6, 2) * 100
        hoard.sp += roll_die(6, 2) * 1000
        hoard.gp += roll_die(6, 6) * 100
        hoard.pp += roll_die(6, 3) * 10
        roll_on_hoard_table(hoard_tables.table_two, hoard)


def roll_table_three(rolls, hoard):
    """'roll' on the hoard table for CR 11-16 and record the result"""
    for roll_counter in range(rolls):
        hoard.gp += roll_die(6, 4) * 1000
        hoard.pp += roll_die(6, 5) * 100
        roll_on_hoard_table(hoard_tables.table_three, hoard)


def roll_table_four(rolls, hoard):
    """'roll' on the hoard table for CR 17+ and record the result"""
    for roll_counter in range(rolls):
        hoard.gp += roll_die(6, 12) * 1000
        hoard.pp += roll_die(6, 6) * 1000
        roll_on_hoard_table(hoard_tables.table_two, hoard)


def main(arglist):
    """take arguments, 'roll' on the tables, print the full result"""
    values_list = []
    [values_list.extend([k,v//100]) for k,v in magic_mappings.cp_values.items()]
    values_str = " {}: {}gp,".join([""]+["" for e in magic_mappings.cp_values])[:-1]
    values_str = values_str.format(*values_list)
    parser = ArgumentParser(description="Roll on the 5e Treasure Hoard " \
                                        "tables. Any combination of rolls" \
                                        " is allowed. The Total Value " \
                                        "calculation uses the following " \
                                        "values. " \
                                        + values_str
                                        )
    parser.add_argument("-a", "--table-one",
                        type=int,
                        help="The number of rolls to make on the table for " \
                             + "CR 0-4")
    parser.add_argument("-b", "--table-two",
                        type=int,
                        help="The number of rolls to make on the table for " \
                             + "CR 5-10")
    parser.add_argument("-c", "--table-three",
                        type=int,
                        help="The number of rolls to make on the table for " \
                             + "CR 11-16")
    parser.add_argument("-d", "--table-four",
                        type=int,
                        help="The number of rolls to make on the table for " \
                             + "CR 17+")
    args = parser.parse_args(arglist)

    hoard = TreasureHoard()

    if args.table_one is not None:
        roll_table_one(args.table_one, hoard)

    if args.table_two is not None:
        roll_table_two(args.table_two, hoard)

    if args.table_three is not None:
        roll_table_three(args.table_three, hoard)

    if args.table_four is not None:
        roll_table_four(args.table_four, hoard)

    hoard.print_result()


if __name__ == "__main__":
    main(sys.argv[1:])
