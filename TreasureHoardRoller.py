import sys
import random
from argparse import ArgumentParser

import magicitems as magi
import mundaneitems as muni
import magicmappings as magmap
import mundanemappings as munmap

cp_values = {**munmap.cp_values, **magmap.cp_values,
             "cp": 1, "sp": 10, "gp": 100, "pp": 1000}


class TreasureHoard:
    """repository of all treasue in the hoard, with I/O methods"""

    cp = 0
    sp = 0
    gp = 0
    pp = 0
    mundanes = dict(zip(munmap.categories,
                        [{} for i in range(len(munmap.categories))]))
    magics = dict(zip(magmap.magic_rarities,
                      [{} for i in range(len(magmap.magic_rarities))]))

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
            category = munmap.qualities[obj][0]
            self.increment_counts(self.mundanes[category], [obj])

    def add_magics(self, object_info):
        """record new magic items in treasure group"""
        object_list = object_info[1]
        for obj in object_list:
            rarity = magmap.magic_qualities[obj][0]
            self.increment_counts(self.magics[rarity], [obj])

    def print(self):
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
        print("  cp: {}".format(self.get_total_cp_value()))
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
        mundane_result = roll_table(muni.tables[table_name])
        objects += [roll_table(mundane_result)]
    return (table_name, objects)


def get_magics(table_name, die_type, die_count):
    """'roll' on the given table of magic items"""
    objects = []
    roll_count = roll_die(die_type, die_count)
    for r in range(roll_count):
        magic_result = roll_table(magi.tables[table_name])
        objects += [roll_table(magic_result)]
    return (table_name, objects)


def roll_table_one(rolls, result):
    """'roll' on the hoard table for CR 0-4 and record the result"""
    num_to_mundane = {}
    for i in list(range(7,17)) \
             + list(range(37,45)) \
             + list(range(61,66)) \
             + list(range(76,79)):
        num_to_mundane[i] = ("gem_10gp", 6, 2)
    for i in list(range(27,37)) \
             + list(range(53,61)) \
             + list(range(71,76)) \
             + list(range(81,86)) \
             + list(range(93,98)) \
             + [100]:
        num_to_mundane[i] = ("gem_50gp", 6, 2)
    for i in list(range(17,27)) \
             + list(range(45,53)) \
             + list(range(66,71)) \
             + [79,80] \
             + list(range(86,93)) \
             + [98,99]:
        num_to_mundane[i] = ("art_25gp", 4, 2)

    num_to_magic = {}
    for i in list(range(37,61)):
        num_to_magic[i] = ("magic_a", 6, 1)
    for i in list(range(61,76)):
        num_to_magic[i] = ("magic_b", 4, 1)
    for i in list(range(76,86)):
        num_to_magic[i] = ("magic_c", 4, 1)
    for i in list(range(86,97)):
        num_to_magic[i] = ("magic_f", 4, 1)
    for i in [97,98,99,100]:
        num_to_magic[i] = ("magic_g", 1, 1)

    for roll_index in range(rolls):
        result.cp += roll_die(6, 6) * 100
        result.sp += roll_die(6, 3) * 100
        result.gp += roll_die(6, 2) * 10

        table_roll = roll_die(100, 1)

        if table_roll > 6:
            mundane_info = num_to_mundane[table_roll]
            mundane_objects = get_mundanes(*mundane_info)
            result.add_mundanes(mundane_objects)

        if table_roll > 36:
            magic_info = num_to_magic[table_roll]
            magic_objects = get_magics(*magic_info)
            result.add_magics(magic_objects)


def roll_table_two(rolls, result):
    """'roll' on the hoard table for CR 5-10 and record the result"""
    num_to_mundane = {}
    for i in list(range(11,17)) \
             + list(range(33,37)) \
             + list(range(50,55)) \
             + list(range(67,70)) \
             + [77,78] \
             + list(range(85,89)):
        num_to_mundane[i] = ("gem_50gp", 6, 3)
    for i in list(range(17,23)) \
             + list(range(37,41)) \
             + list(range(55,60)) \
             + list(range(70,73)) \
             + [79] \
             + list(range(89,92)) \
             + [95,96,99]:
        num_to_mundane[i] = ("gem_100gp", 6, 3)
    for i in list(range(5,11)) \
             + list(range(29,33)) \
             + list(range(45,50)) \
             + list(range(64,67)) \
             + [75,76] \
             + list(range(81,85)):
        num_to_mundane[i] = ("art_25gp", 4, 2)
    for i in list(range(23,29)) \
             + list(range(41,45)) \
             + list(range(60,64)) \
             + list(range(92,95)) \
             + [73,74,80,97,98,100]:
        num_to_mundane[i] = ("art_250gp", 4, 2)

    num_to_magic = {}
    for i in list(range(29,45)):
        num_to_magic[i] = ("magic_a", 6, 1)
    for i in list(range(45,64)):
        num_to_magic[i] = ("magic_b", 4, 1)
    for i in list(range(64,75)):
        num_to_magic[i] = ("magic_c", 4, 1)
    for i in list(range(75,81)):
        num_to_magic[i] = ("magic_d", 1, 1)
    for i in list(range(81,95)):
        num_to_magic[i] = ("magic_f", 4, 1)
    for i in [95,96,97,98]:
        num_to_magic[i] = ("magic_g", 4, 1)
    for i in [99,100]:
        num_to_magic[i] = ("magic_h", 1, 1)

    for roll_index in range(rolls):
        result.cp += roll_die(6, 2) * 100
        result.sp += roll_die(6, 2) * 1000
        result.gp += roll_die(6, 6) * 100
        result.pp += roll_die(6, 3) * 10

        table_roll = roll_die(100, 1)

        if table_roll > 4:
            mundane_info = num_to_mundane[table_roll]
            mundane_objects = get_mundanes(*mundane_info)
            result.add_mundanes(mundane_objects)

        if table_roll > 28:
            magic_info = num_to_magic[table_roll]
            magic_objects = get_magics(*magic_info)
            result.add_magics(magic_objects)


def roll_table_three(rolls, result):
    """'roll' on the hoard table for CR 11-16 and record the result"""
    num_to_mundane = {}
    for i in [11,12,24,25,26] \
             + list(range(41,46)) \
             + list(range(59,63)) \
             + [71,72,79,80,89,90,97,98]:
        num_to_mundane[i] = ("gem_500gp", 6, 3)
    for i in list(range(13,16)) \
             + list(range(27,30)) \
             + list(range(46,51)) \
             + list(range(63,67)) \
             + [73,74,81,82,91,92,99,100]:
        num_to_mundane[i] = ("gem_1000gp", 6, 3)
    for i in list(range(4,7)) \
             + list(range(16,20)) \
             + list(range(30,36)) \
             + list(range(51,55)) \
             + [67,68,75,76] \
             + list(range(83,86)) \
             + [93,94]:
        num_to_mundane[i] = ("art_250gp", 4, 2)
    for i in list(range(7,11)) \
             + list(range(20,24)) \
             + list(range(36,41)) \
             + list(range(55,59)) \
             + [69,70,77,78,86,87,88,95,96]:
        num_to_mundane[i] = ("art_750gp", 4, 2)

    num_to_magic = {}
    for i in list(range(16,30)):
        num_to_magic[i] = [("magic_a", 4, 1), ("magic_b", 6, 1)]
    for i in list(range(30,51)):
        num_to_magic[i] = [("magic_c", 6, 1)]
    for i in list(range(51,67)):
        num_to_magic[i] = [("magic_d", 4, 1)]
    for i in list(range(67,75)):
        num_to_magic[i] = [("magic_e", 1, 1)]
    for i in list(range(75,83)):
        num_to_magic[i] = [("magic_f", 1, 1), ("magic_g", 4, 1)]
    for i in list(range(83,93)):
        num_to_magic[i] = [("magic_h", 4, 1)]
    for i in list(range(93,101)):
        num_to_magic[i] = [("magic_i", 1, 1)]

    for roll_index in range(rolls):
        result.gp += roll_die(6, 4) * 1000
        result.pp += roll_die(6, 5) * 100

        table_roll = roll_die(100, 1)

        if table_roll > 3:
            mundane_info = num_to_mundane[table_roll]
            mundane_objects = get_mundanes(*mundane_info)
            result.add_mundanes(mundane_objects)

        if table_roll > 15:
            magic_info = num_to_magic[table_roll]
            for mi in magic_info:
                magic_objects = get_magics(*mi)
                result.add_magics(magic_objects)


def roll_table_four(rolls, result):
    """'roll' on the hoard table for CR 17+ and record the result"""
    num_to_mundane = {}
    for i in list(range(3,6)) \
             + list(range(15,23)) \
             + list(range(47,53)) \
             + [69,73,74,81,82,83,84,85]:
        num_to_mundane[i] = ("gem_1000gp", 6, 3)
    for i in list(range(12,15)) \
             + list(range(39,47)) \
             + list(range(64,69)) \
             + [72,79,80,96,97,98,99,100]:
        num_to_mundane[i] = ("gem_5000gp", 6, 3)
    for i in list(range(6,9)) \
             + list(range(23,31)) \
             + list(range(53,59)) \
             + [70,75,76,86,87,88,89,90]:
        num_to_mundane[i] = ("art_2500gp", 4, 2)
    for i in list(range(9,12)) \
             + list(range(31,39)) \
             + list(range(59,64)) \
             + [71,77,78,91,92,93,94,95]:
        num_to_mundane[i] = ("art_7500gp", 4, 2)

    num_to_magic = {}
    for i in list(range(3,15)):
        num_to_magic[i] = [("magic_c", 8, 1)]
    for i in list(range(15,47)):
        num_to_magic[i] = [("magic_d", 6, 1)]
    for i in list(range(47,69)):
        num_to_magic[i] = [("magic_e", 4, 1)]
    for i in list(range(69,73)):
        num_to_magic[i] = [("magic_g", 4, 1)]
    for i in list(range(73,81)):
        num_to_magic[i] = [("magic_h", 4, 1)]
    for i in list(range(81,101)):
        num_to_magic[i] = [("magic_i", 4, 1)]

    for roll_index in range(rolls):
        result.gp += roll_die(6, 12) * 1000
        result.pp += roll_die(6, 6) * 1000

        table_roll = roll_die(100, 1)

        if table_roll > 2:
            mundane_info = num_to_mundane[table_roll]
            mundane_objects = get_mundanes(*mundane_info)
            result.add_mundanes(mundane_objects)

        if table_roll > 2:
            magic_info = num_to_magic[table_roll]
            for mi in magic_info:
                magic_objects = get_magics(*mi)
                result.add_magics(magic_objects)


def main(arglist):
    """take arguments, 'roll' on the tables, print the full result"""
    values_list = []
    [values_list.extend([k,v//100]) for k,v in magmap.cp_values.items()]
    values_str = " {}: {}gp,".join([""]+["" for e in magmap.cp_values])[:-1]
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

    hoard.print()


if __name__ == "__main__":
    main(sys.argv[1:])
