# Maps each item available in mundaneitems.py to the item's 
# price category. Using a list for each value gives the 
# option to include more item qualities in each mapping.
#
# Also provides a list of all price categories and maps
# those to their value in copper pieces.

qualities = {
    "Azurite (opaque mottled deep blue)":
        ["10gp", ""],
    "Banded agate (translucent striped brown, blue, white, or red)":
        ["10gp", ""],
    "Blue quartz (transparent pale blue)":
        ["10gp", ""],
    "Eye agate (translucent circles of gray, white, brown, blue, or green)":
        ["10gp", ""],
    "Hematite (opaque gray-black)":
        ["10gp", ""],
    "Lapis lazuli (opaque light and dark blue with yellow flecks)":
        ["10gp", ""],
    "Malachite (opaque striated light and dark green)":
        ["10gp", ""],
    "Moss agate (translucent pink or yellow-white with mossy gray or green " \
            "markings)":
        ["10gp", ""],
    "Obsidian (opaque black)":
        ["10gp", ""],
    "Rhodochrosite (opaque light pink)":
        ["10gp", ""],
    "Tiger eye (translucent brown with golden center)":
        ["10gp", ""],
    "Turquoise (opaque light blue-green)":
        ["10gp", ""],
    "Bloodstone (opaque dark gray with red flecks)":
        ["50gp", ""],
    "Carnelian (opaque orange to red-brown)":
        ["50gp", ""],
    "Chalcedony (opaque white)":
        ["50gp", ""],
    "Chrysoprase (translucent green)":
        ["50gp", ""],
    "Citrine (transparent pale yellow-brown)":
        ["50gp", ""],
    "Jasper (opaque blue, black, or brown)":
        ["50gp", ""],
    "Moonstone (translucent white with pale blue glow)":
        ["50gp", ""],
    "Onyx (opaque bands of black and white, or pure black or white)":
        ["50gp", ""],
    "Quartz (transparent white, smoky gray, or yellow)":
        ["50gp", ""],
    "Sardonyx (opaque bands of red and white)":
        ["50gp", ""],
    "Star rose quartz (translucent rosy stone with white star-shaped center)":
        ["50gp", ""],
    "Zircon (transparent pale blue-green)":
        ["50gp", ""],
    "Amber (transparent watery gold to rich gold)":
        ["100gp", ""],
    "Amethyst (transparent deep purple)":
        ["100gp", ""],
    "Chrysoberyl (transparent yellow-green to pale green)":
        ["100gp", ""],
    "Coral (opaque crimson)":
        ["100gp", ""],
    "Garnet (transparent red, brown-green, or violet)":
        ["100gp", ""],
    "Jade (translucent light green, deep green, or white)":
        ["100gp", ""],
    "Jet (opaque deep black)":
        ["100gp", ""],
    "Pearl (opaque lustrous white, yellow, or pink)":
        ["100gp", ""],
    "Spinel (transparent red, red-brown, or deep green)":
        ["100gp", ""],
    "Tourmaline (transparent pale green, blue, brown, or red)":
        ["100gp", ""],
    "Alexandrite (transparent dark green)":
        ["500gp", ""],
    "Aquamarine (transparent pale blue-green)":
        ["500gp", ""],
    "Black pearl (opaque pure black)":
        ["500gp", ""],
    "Blue spinel (transparent deep blue)":
        ["500gp", ""],
    "Peridot (transparent rich olive green)":
        ["500gp", ""],
    "Topaz (transparent golden yellow)":
        ["500gp", ""],
    "Black opal (translucent dark green with black mottling and golden " \
            "flecks)":
        ["1000gp", ""],
    "Blue sapphire (transparent blue-white to medium blue)":
        ["1000gp", ""],
    "Emerald (transparent deep bright green)":
        ["1000gp", ""],
    "Fire opal (translucent fiery red)":
        ["1000gp", ""],
    "Opal (translucent pale blue with green and golden mottling)":
        ["1000gp", ""],
    "Star ruby (translucent ruby with white star-shaped center)":
        ["1000gp", ""],
    "Star sapphire (translucent blue sapphire with white star-shaped center)":
        ["1000gp", ""],
    "Yellow sapphire (transparent fiery yellow or yellow-green)":
        ["1000gp", ""],
    "Black sapphire (translucent lustrous black with glowing highlights)":
        ["5000gp", ""],
    "Diamond (transparent blue-white, canary, pink, brown, or blue)":
        ["5000gp", ""],
    "Jacinth (transparent fiery orange)":
        ["5000gp", ""],
    "Ruby (transparent clear red to deep crimson)":
        ["5000gp", ""],
    "Silver ewer":
        ["25gp", ""],
    "Carved bone statuette":
        ["25gp", ""],
    "Small gold bracelet":
        ["25gp", ""],
    "Cloth-of-gold vestments":
        ["25gp", ""],
    "Black velvet mask stitched with silver thread":
        ["25gp", ""],
    "Copper chalice with silver filigree":
        ["25gp", ""],
    "Pair of engraved bone dice":
        ["25gp", ""],
    "Small mirror set in a painted wooden frame":
        ["25gp", ""],
    "Embroidered silk handkerchief":
        ["25gp", ""],
    "Gold locket with a painted portrait inside":
        ["25gp", ""],
    "Gold ring set with bloodstones":
        ["250gp", ""],
    "Carved ivory statuette":
        ["250gp", ""],
    "Large gold bracelet":
        ["250gp", ""],
    "Silver necklace with a gemstone pendant":
        ["250gp", ""],
    "Bronze crown":
        ["250gp", ""],
    "Silk robe with gold embroidery":
        ["250gp", ""],
    "Large well-made tapestry":
        ["250gp", ""],
    "Brass mug with jade inlay":
        ["250gp", ""],
    "Box of turquoise animal figurines":
        ["250gp", ""],
    "Gold bird cage with electrum filigree":
        ["250gp", ""],
    "Silver chalice set with moonstones":
        ["750gp", ""],
    "Silver-plated steellongsword with jet set in hilt":
        ["750gp", ""],
    "Carved harp of exotic wood with ivory inlay and zircon gems":
        ["750gp", ""],
    "Small gold idol":
        ["750gp", ""],
    "Gold dragon comb set with red garnets as eyes":
        ["750gp", ""],
    "Bottle stopper cork embossed with gold leaf and set with amethysts":
        ["750gp", ""],
    "Ceremonial electrum dagger wit~ a black pearl in the pommel":
        ["750gp", ""],
    "Silver and gold brooch":
        ["750gp", ""],
    "Obsidian statuette with gold fittings and inlay":
        ["750gp", ""],
    "Painted gold war mask":
        ["750gp", ""],
    "Fine gold chain set with a fire opal":
        ["2500gp", ""],
    "Old masterpiece painting":
        ["2500gp", ""],
    "Embroidered silk and velvet mantle set with numerous moonstones":
        ["2500gp", ""],
    "Platinum bracelet set with a sapphire":
        ["2500gp", ""],
    "Embroidered glove set with jewel chips":
        ["2500gp", ""],
    "Jeweled anklet":
        ["2500gp", ""],
    "Gold music box":
        ["2500gp", ""],
    "Gold circlet set with four aquamarines":
        ["2500gp", ""],
    "Eye patch with a mock eye set in blue sapphire and moonstone":
        ["2500gp", ""],
    "A necklace string of small pink pearls":
        ["2500gp", ""],
    "Jeweled gold crown":
        ["7500gp", ""],
    "Jeweled platinum ring":
        ["7500gp", ""],
    "Small gold statuette set with rubies":
        ["7500gp", ""],
    "Gold cup set with emeralds":
        ["7500gp", ""],
    "Gold jewelry box with platinum filigree":
        ["7500gp", ""],
    "Painted gold child's sarcophagus":
        ["7500gp", ""],
    "Jade game board with solid gold playing pieces":
        ["7500gp", ""],
    "Bejeweled ivory drinking horn with gold filigree":
        ["7500gp", ""],
}

categories = [
                "10gp",
                "25gp",
                "50gp",
                "75gp",
                "100gp",
                "250gp",
                "500gp",
                "750gp",
                "1000gp",
                "2500gp",
                "5000gp",
                "7500gp",
                ]

cp_values = dict(zip(categories,
                     [
                       1000,
                       2500,
                       5000,
                       7500,
                       10000,
                       25000,
                       50000,
                       75000,
                       100000,
                       250000,
                       500000,
                       750000,
                       ]))
