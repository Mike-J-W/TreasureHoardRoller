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
    mundanes = dict(zip(mundane_mappings.categories,
                        [{} for i in range(len(mundane_mappings.categories))]))
    magics = dict(zip(magic_mappings.magic_rarities,
                      [{} for i in range(len(magic_mappings.magic_rarities))]))

    def increment_counts(self, count_dict, objects):
        """increase stored counts of given items"""
        for obj in objects:
            if obj in count_dict:
                count_dict[obj] +=1
            else:
                count_dict[obj] = 1

    def print_counts(self, count_dict):
        """print list of item counts and items"""
        if count_dict:
            max_count = max(count_dict.values())
            width = len(str(max_count))
            for obj in sorted(count_dict):
                print("    {0:{width}} {1}".format(count_dict[obj], obj,
                                                   width=width))
        else:
            print()

    def get_total_cp_value(self):
        """sum all treasure value, in cp units"""
        total = self.cp
        total += cp_values["sp"] * self.sp
        total += cp_values["gp"] * self.gp
        total += cp_values["pp"] * self.pp
        for obj_class in [self.mundanes, self.magics]:
            for obj_type, count_dict in obj_class.items():
                total += cp_values[obj_type] * sum(count_dict.values())
        return total

    def add_mundanes(self, object_info):
        """record new mundane items in treasure group"""
        table_name = object_info[0]
        object_list = object_info[1]
        for obj in object_list:
            category = mundane_mappings.qualities[obj][0]
            self.increment_counts(self.mundanes[category], [obj])

    def add_magics(self, object_info):
        """record new magic items in treasure group"""
        object_list = object_info[1]
        for obj in object_list:
            rarity = magic_mappings.magic_qualities[obj][0]
            self.increment_counts(self.magics[rarity], [obj])

    def print_result(self):
        """print all treasure to formatted style"""
        print("COINS: ")
        print("  cp: {}".format(self.cp))
        print("  sp: {}".format(self.sp))
        print("  gp: {}".format(self.gp))
        print("  pp: {}".format(self.pp))
        print()
        print("MUNDANE ITEMS: ")
        for category, count_dict in self.mundanes.items():
            if count_dict:
                print("  {}:".format(category))
                self.print_counts(count_dict)
        print()
        print("MAGIC ITEMS: ")
        for rarity, count_dict in self.magics.items():
            if count_dict:
                print("  {}:".format(rarity))
                self.print_counts(count_dict)
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


def roll_table(table):
    """randomly choose an item from the given table"""
    if len(table) == 1:
        return table[0]

    return table[roll_die(len(table), 1)]


def get_mundanes(table_name, die_type, die_count):
    """'roll' on the given table of mundane items"""
    objects = []
    roll_count = roll_die(die_type, die_count)
    for r in range(roll_count):
        mundane_result = roll_table(mundane_tables.tables[table_name])
        objects += [roll_table(mundane_result)]
    return (table_name, objects)


def get_magics(table_name, die_type, die_count):
    """'roll' on the given table of magic items"""
    objects = []
    roll_count = roll_die(die_type, die_count)
    for r in range(roll_count):
        magic_result = roll_table(magic_tables.tables[table_name])
        objects += [roll_table(magic_result)]
    return (table_name, objects)


def roll_hoard_table(table_name, result):
    hoard_table_row = roll_table(table_name)
    mundane_info = hoard_table_row[0]
    for mi in mundane_info:
        mundane_objects = get_mundanes(*mi)
        result.add_mundanes(mundane_objects)
    magic_info = hoard_table_row[1]
    for mi in magic_info:
        magic_objects = get_magics(*mi)
        result.add_magics(magic_objects)


def roll_table_one(rolls, result):
    """'roll' on the hoard table for CR 0-4 and record the result"""
    for roll_index in range(rolls):
        result.cp += roll_die(6, 6) * 100
        result.sp += roll_die(6, 3) * 100
        result.gp += roll_die(6, 2) * 10
        roll_hoard_table(hoardtables.table_one, result)


def roll_table_two(rolls, result):
    """'roll' on the hoard table for CR 5-10 and record the result"""
    for roll_index in range(rolls):
        result.cp += roll_die(6, 2) * 100
        result.sp += roll_die(6, 2) * 1000
        result.gp += roll_die(6, 6) * 100
        result.pp += roll_die(6, 3) * 10
        roll_hoard_table(hoardtables.table_two, result)


def roll_table_three(rolls, result):
    """'roll' on the hoard table for CR 11-16 and record the result"""
    for roll_index in range(rolls):
        result.gp += roll_die(6, 4) * 1000
        result.pp += roll_die(6, 5) * 100
        roll_hoard_table(hoardtables.table_three, result)


def roll_table_four(rolls, result):
    """'roll' on the hoard table for CR 17+ and record the result"""
    for roll_index in range(rolls):
        result.gp += roll_die(6, 12) * 1000
        result.pp += roll_die(6, 6) * 1000
        roll_hoard_table(hoardtables.table_two, result)


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
