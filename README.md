# TreasureHoardRoller
A python script to automate the process of rolling on any combination 
of the Treasure Hoard tables in the 5e D&amp;D DMG.

I've tested and run this script with python 3.6.1.  It does not work 
with python 2.7.  I have no comment on other python 3 versions.

# Usage
    usage: TreasureHoardRoller.py [-h] [-a TABLE_ONE] [-b TABLE_TWO] 
                                       [-c TABLE_THREE] [-d TABLE_FOUR]

    Roll on the 5e Treasure Hoard tables. Any combination of rolls is 
    allowed. The Total Value calculation uses the following values.
      common: 75gp
      uncommon: 300gp
      rare: 2750gp
      very rare: 27500gp
      legendary: 275000gp

    optional arguments:
      -h, --help
        show this help message and exit
      -a TABLE_ONE, --table-one TABLE_ONE
        The number of rolls to make on the table for CR 0-4
      -b TABLE_TWO, --table-two TABLE_TWO
        The number of rolls to make on the table for CR 5-10
      -c TABLE_THREE, --table-three TABLE_THREE
        The number of rolls to make on the table for CR 11-16
      -d TABLE_FOUR, --table-four TABLE_FOUR
        The number of rolls to make on the table for CR 17+

# Sample Output

    $ python3 TreasureHoardRoller.py -a 2 -b 1
    COINS:
      cp: 4100
      sp: 8700
      gp: 2520
      pp: 140

    MUNDANE ITEMS:
      25gp:
        1 Black velvet mask stitched with silver thread
        1 Cloth-of-gold vestments
        2 Copper chalice with silver filigree
        2 Embroidered silk handkerchief
        1 Gold locket with a painted portrait inside
        1 Small mirror set in a painted wooden frame
      100gp:
        1 Amethyst (transparent deep purple)
        1 Chrysoberyl (transparent yellow-green to pale green)
        1 Garnet (transparent red, brown-green, or violet)
        2 Jade (translucent light green, deep green, or white)
        6 Jet (opaque deep black)
        1 Pearl (opaque lustrous white, yellow, or pink)
        1 Spinel (transparent red, red-brown, or deep green)

    MAGIC ITEMS:
      common:
        1 Potion of Healing
        1 Spell Scroll (1st Level)
      uncommon:
        1 Cloak of Elvenkind
      rare:
        1 Bead of Force
        1 Potion of Mind Reading
        1 Spell Scroll (4th Level)

    TOTAL VALUE:
      gp: 15031

# Homebrew

This script can support homebrewed items. Adding or removing items 
in the tables in magicitems.py and mundaneitems.py is supported. You 
may either add the item at the top level of the table or you may add 
it to an interior list.  The former will make all other top-level 
items slightly less likely to be rolled.  The latter will only affect 
the probability of the other items in that interior list.

Adding or removing tables is not yet supported.

If you add an item to magicitems.py or mundaneitems.py, you must also
add it to the corresponding <>mappings.py file and include the
expected qualities.  Right now, the only expected qualities are rarity
for magic items and price category for mundane items.

# Further Work

I intend to move the treasure hoard table specifications to an 
exterior file.  This will allow customizing the chances that each 
mundane or magic item table will be used.  This will also allow the 
addition or removal of such tables.

The values in the qualities dictionary in magicmappings.py and in 
mundanemappings.py are lists.  Right now, the lists only have
1 element, the rarity or price category.  Other elements in these
lists could be used to store item descriptions or other qualities.
I have no current plans to add any other qualities to the lists.

I may explore homebrewed coins.

I'm open to other ideas as well.

buymeacoff.ee/QBuD3fbJN
