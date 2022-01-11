# Maps each item available in magicitems.py to the item's 
# rarity. Using a list for each value gives the 
# option to include more item qualities in each mapping.
#
# Also provides a list of all rarities and maps those to
# the average of the uppoer and lower price bounds of 
# the rarity, as given in the 5e DMG.

magic_qualities = {
    "Adamantine Armor (Breastplate)": ["uncommon"],
    "Adamantine Armor (Chain Mail)": ["uncommon"],
    "Adamantine Armor (Chain Shirt)": ["uncommon"],
    "Adamantine Armor (Half Plate)": ["uncommon"],
    "Adamantine Armor (Plate)": ["uncommon"],
    "Adamantine Armor (Ring Mail)": ["uncommon"],
    "Adamantine Armor (Scale Mail)": ["uncommon"],
    "Adamantine Armor (Splint)": ["uncommon"],
    "Alchemy Jug": ["uncommon"],
    "Ammunition, +1": ["uncommon"],
    "Ammunition, +2": ["rare"],
    "Ammunition, +3": ["very rare"],
    "Amulet of Health": ["rare"],
    "Amulet of Proof against Detection and Location": ["uncommon"],
    "Amulet of the Planes": ["very rare"],
    "Animated Shield": ["very rare"],
    "Apparatus of Kwalish": ["legendary"],
    "Armor, +1 (Breastplate)": ["rare"],
    "Armor, +1 (Chain Mail)": ["rare"],
    "Armor, +1 (Chain Shirt)": ["rare"],
    "Armor, +1 (Half Plate)": ["rare"],
    "Armor, +1 (Hide)": ["rare"],
    "Armor, +1 (Leather)": ["rare"],
    "Armor, +1 (Padded)": ["rare"],
    "Armor, +1 (Plate)": ["rare"],
    "Armor, +1 (Ring Mail)": ["rare"],
    "Armor, +1 (Scale Mail)": ["rare"],
    "Armor, +1 (Splint)": ["rare"],
    "Armor, +1 (Studded Leather)": ["rare"],
    "Armor, +2 (Breastplate)": ["very rare"],
    "Armor, +2 (Chain Mail)": ["very rare"],
    "Armor, +2 (Chain Shirt)": ["very rare"],
    "Armor, +2 (Half Plate)": ["very rare"],
    "Armor, +2 (Hide)": ["very rare"],
    "Armor, +2 (Leather)": ["very rare"],
    "Armor, +2 (Padded)": ["very rare"],
    "Armor, +2 (Plate)": ["very rare"],
    "Armor, +2 (Ring Mail)": ["very rare"],
    "Armor, +2 (Scale Mail)": ["very rare"],
    "Armor, +2 (Splint)": ["very rare"],
    "Armor, +2 (Studded Leather)": ["very rare"],
    "Armor, +3 (Breastplate)": ["legendary"],
    "Armor, +3 (Chain Mail)": ["legendary"],
    "Armor, +3 (Chain Shirt)": ["legendary"],
    "Armor, +3 (Half Plate)": ["legendary"],
    "Armor, +3 (Hide)": ["legendary"],
    "Armor, +3 (Leather)": ["legendary"],
    "Armor, +3 (Padded)": ["legendary"],
    "Armor, +3 (Plate)": ["legendary"],
    "Armor, +3 (Ring Mail)": ["legendary"],
    "Armor, +3 (Scale Mail)": ["legendary"],
    "Armor, +3 (Splint)": ["legendary"],
    "Armor, +3 (Studded Leather)": ["legendary"],
    "Armor of Invulnerability": ["legendary"],
    "Armor of Gleaming (Breastplate)": ["common"],
    "Armor of Gleaming (Chain Mail)": ["common"],
    "Armor of Gleaming (Chain Shirt)": ["common"],
    "Armor of Gleaming (Half Plate)": ["common"],
    "Armor of Gleaming (Hide)": ["common"],
    "Armor of Gleaming (Plate)": ["common"],
    "Armor of Gleaming (Ring Mail)": ["common"],
    "Armor of Gleaming (Scale Mail)": ["common"],
    "Armor of Gleaming (Splint)": ["common"],
    "Armor of Resistance (Breastplate)": ["rare"],
    "Armor of Resistance (Chain Mail)": ["rare"],
    "Armor of Resistance (Chain Shirt)": ["rare"],
    "Armor of Resistance (Half Plate)": ["rare"],
    "Armor of Resistance (Leather)": ["rare"],
    "Armor of Resistance (Plate)": ["rare"],
    "Armor of Resistance (Scale Mail)": ["rare"],
    "Armor of Resistance (Splint)": ["rare"],
    "Armor of Resistance (Studded Leather)": ["rare"],
    "Armor of Vulnerability": ["rare"],
    "Arrow of Slaying": ["very rare"],
    "Arrow-Catching Shield": ["rare"],
    "Bag of Beans": ["rare"],
    "Bag of Devouring": ["very rare"],
    "Bag of Holding": ["uncommon"],
    "Bag of Tricks (Gray)": ["uncommon"],
    "Bag of Tricks (Rust)": ["uncommon"],
    "Bag of Tricks (Tan)": ["uncommon"],
    "Bead of Force": ["rare"],
    "Bead of Nourishment": ["common"],
    "Bead of Refreshment": ["common"],
    "Belt of Cloud Giant Strength": ["legendary"],
    "Belt of Dwarvenkind": ["rare"],
    "Belt of Fire Giant Strength": ["very rare"],
    "Belt of Frost (or Stone) Giant Strength": ["very rare"],
    "Belt of Hill Giant Strength": ["rare"],
    "Belt of Storm Giant Strength": ["legendary"],
    "Berserker Axe": ["rare"],
    "Boots of Elvenkind": ["uncommon"],
    "Boots of False Tracks": ["common"],
    "Boots of Levitation": ["rare"],
    "Boots of Speed": ["rare"],
    "Boots of Striding and Springing": ["uncommon"],
    "Boots of the Winterlands": ["uncommon"],
    "Bowl of Commanding Water Elementals": ["rare"],
    "Bracers of Archery": ["uncommon"],
    "Bracers of Defense": ["rare"],
    "Brazier of Commanding Fire Elementals": ["rare"],
    "Brooch of Shielding": ["uncommon"],
    "Broom of Flying": ["uncommon"],
    "Candle of Invocation": ["very rare"],
    "Candle of the Deep": ["common"],
    "Cap of Water Breathing": ["uncommon"],
    "Cape of the Mountebank": ["rare"],
    "Carpet of Flying": ["very rare"],
    "Cast-Off Armor (Breastplate)": ["common"],
    "Cast-Off Armor (Chain Mail)": ["common"],
    "Cast-Off Armor (Chain Shirt)": ["common"],
    "Cast-Off Armor (Half Plate)": ["common"],
    "Cast-Off Armor (Hide)": ["common"],
    "Cast-Off Armor (Leather)": ["common"],
    "Cast-Off Armor (Padded)": ["common"],
    "Cast-Off Armor (Plate)": ["common"],
    "Cast-Off Armor (Ring Mail)": ["common"],
    "Cast-Off Armor (Scale Mail)": ["common"],
    "Cast-Off Armor (Splint)": ["common"],
    "Cast-Off Armor (Studded Leather)": ["common"],
    "Censer of Controlling Air Elementals": ["rare"],
    "Charlatan's Die": ["common"],
    "Chest of Preserving": ["common"],
    "Chime of Opening": ["rare"],
    "Circlet of Blasting": ["uncommon"],
    "Cloak of Arachnida": ["very rare"],
    "Cloak of Billowing": ["common"],
    "Cloak of Displacement": ["rare"],
    "Cloak of Elvenkind": ["uncommon"],
    "Cloak of Invisibility": ["legendary"],
    "Cloak of Many Fashions": ["common"],
    "Cloak of Protection": ["uncommon"],
    "Cloak of the Bat": ["rare"],
    "Cloak of the Manta Ray": ["uncommon"],
    "Clockwork Amulet": ["common"],
    "Clothes of Mending": ["common"],
    "Crystal Ball of Mind Reading": ["legendary"],
    "Crystal Ball of Scrying": ["very rare"],
    "Crystal Ball of Telepathy": ["legendary"],
    "Crystal Ball of True Seeing": ["legendary"],
    "Cube of Force": ["rare"],
    "Cubic Gate": ["legendary"],
    "Daern's Instant Fortress": ["rare"],
    "Dagger of Venom": ["rare"],
    "Dancing Sword": ["very rare"],
    "Dark Shard Amulet": ["common"],
    "Decanter of Endless Water": ["uncommon"],
    "Deck of Illusions": ["uncommon"],
    "Deck of Many Things": ["legendary"],
    "Defender": ["legendary"],
    "Demon Armor": ["very rare"],
    "Dimensional Shackles": ["rare"],
    "Dragon Scale Mail": ["very rare"],
    "Dragon Slayer": ["rare"],
    "Dread Helm": ["common"],
    "Driftglobe": ["uncommon"],
    "Dust of Disappearance": ["uncommon"],
    "Dust of Dryness": ["uncommon"],
    "Dust of Sneezing and Choking": ["uncommon"],
    "Dwarven Plate": ["very rare"],
    "Dwarven Thrower": ["very rare"],
    "Ear Horn of Listening": ["common"],
    "Efreeti Bottle": ["very rare"],
    "Efreeti Chain": ["legendary"],
    "Elemental Gem": ["uncommon"],
    "Elixir of Health": ["rare"],
    "Elven Chain": ["rare"],
    "Enduring Spellbook": ["common"],
    "Ersatz Eye": ["common"],
    "Eversmoking Bottle": ["uncommon"],
    "Eyes of Charming": ["uncommon"],
    "Eyes of Minute Seeing": ["uncommon"],
    "Eyes of the Eagle": ["uncommon"],
    "Figurine of Wondrous Power (Bronze Griffon)": ["rare"],
    "Figurine of Wondrous Power (Ebony Fly)": ["rare"],
    "Figurine of Wondrous Power (Golden Lions)": ["rare"],
    "Figurine of Wondrous Power (Ivory Goats)": ["rare"],
    "Figurine of Wondrous Power (Marble Elephant)": ["rare"],
    "Figurine of Wondrous Power (Obsidian Steed)": ["very rare"],
    "Figurine of Wondrous Power (Onyx Dog)": ["rare"],
    "Figurine of Wondrous Power (Serpentine Owl)": ["rare"],
    "Figurine of Wondrous Power (Silver Raven)": ["uncommon"],
    "Flame Tongue": ["rare"],
    "Folding Boat": ["rare"],
    "Frost Brand": ["very rare"],
    "Gauntlets of Ogre Power": ["uncommon"],
    "Gem of Brightness": ["uncommon"],
    "Gem of Seeing": ["rare"],
    "Giant Slayer": ["rare"],
    "Glamoured Studded Leather": ["rare"],
    "Gloves of Missile Snaring": ["uncommon"],
    "Gloves of Swimming and Climbing": ["uncommon"],
    "Gloves of Thievery": ["uncommon"],
    "Goggles of Night": ["uncommon"],
    "Hammer of Thunderbolts": ["legendary"],
    "Hat of Disguise": ["uncommon"],
    "Hat of Vermin": ["common"],
    "Hat of Wizardry": ["common"],
    "Headband of Intellect": ["uncommon"],
    "Helm of Brilliance": ["very rare"],
    "Helm of Comprehending Languages": ["uncommon"],
    "Helm of Telepathy": ["uncommon"],
    "Helm of Teleportation": ["rare"],
    "Heward's Handy Haversack": ["rare"],
    "Heward's Handy Spice Pouch": ["common"],
    "Holy Avenger": ["legendary"],
    "Horn of Blasting": ["rare"],
    "Horn of Silent Alarm": ["common"],
    "Horn of Valhalla (Bronze)": ["very rare"],
    "Horn of Valhalla (Iron)": ["legendary"],
    "Horn of Valhalla (Silver or Brass)": ["rare"],
    "Horseshoes of A Zephyr": ["very rare"],
    "Horseshoes of Speed": ["rare"],
    "Immovable Rod": ["uncommon"],
    "Instrument of the Bards (Anstruth Harp)": ["very rare"],
    "Instrument of the Bards (Canaith Mandolin)": ["rare"],
    "Instrument of the Bards (Cli Lyre)": ["rare"],
    "Instrument of the Bards (Doss Lute)": ["uncommon"],
    "Instrument of the Bards (Fochlucan Bandore)": ["uncommon"],
    "Instrument of the Bards (Mac-Fuimidh Cittern)": ["uncommon"],
    "Instrument of the Bards (Ollamh Harp)": ["legendary"],
    "Instrument of Illusions": ["common"],
    "Instrument of Scribing": ["common"],
    "Ioun Stone (Absorption)": ["very rare"],
    "Ioun Stone (Agility)": ["very rare"],
    "Ioun Stone (Awareness)": ["rare"],
    "Ioun Stone (Fortitude)": ["very rare"],
    "Ioun Stone (Greater Absorption)": ["legendary"],
    "Ioun Stone (Insight)": ["very rare"],
    "Ioun Stone (Intellect)": ["very rare"],
    "Ioun Stone (Leadership)": ["very rare"],
    "Ioun Stone (Mastery)": ["legendary"],
    "Ioun Stone (Protection)": ["rare"],
    "Ioun Stone (Regeneration)": ["legendary"],
    "Ioun Stone (Reserve)": ["rare"],
    "Ioun Stone (Strength)": ["very rare"],
    "Ioun Stone (Sustenance)": ["rare"],
    "Iron Bands of Bilarro": ["rare"],
    "Iron Flask": ["legendary"],
    "Javelin of Lightning": ["uncommon"],
    "Keoghtom's Ointment": ["uncommon"],
    "Lantern of Revealing": ["uncommon"],
    "Lock of Trickery": ["common"],
    "Luck Blade": ["legendary"],
    "Mace of Disruption": ["rare"],
    "Mace of Smiting": ["rare"],
    "Mace of Terror": ["rare"],
    "Mantle of Spell Resistance": ["rare"],
    "Manual of Bodily Health": ["very rare"],
    "Manual of Gainful Exercise": ["very rare"],
    "Manual of Golems": ["very rare"],
    "Manual of Quickness of Action": ["very rare"],
    "Mariner's Armor (Breastplate)": ["uncommon"],
    "Mariner's Armor (Chain Mail)": ["uncommon"],
    "Mariner's Armor (Chain Shirt)": ["uncommon"],
    "Mariner's Armor (Half Plate)": ["uncommon"],
    "Mariner's Armor (Hide)": ["uncommon"],
    "Mariner's Armor (Leather)": ["uncommon"],
    "Mariner's Armor (Padded)": ["uncommon"],
    "Mariner's Armor (Plate)": ["uncommon"],
    "Mariner's Armor (Ring Mail)": ["uncommon"],
    "Mariner's Armor (Scale Mail)": ["uncommon"],
    "Mariner's Armor (Splint)": ["uncommon"],
    "Mariner's Armor (Studded Leather)": ["uncommon"],
    "Medallion of Thoughts": ["uncommon"],
    "Mirror of Life Trapping": ["very rare"],
    "Mithral Armor (Breastplate)": ["uncommon"],
    "Mithral Armor (Chain Mail)": ["uncommon"],
    "Mithral Armor (Chain Shirt)": ["uncommon"],
    "Mithral Armor (Half Plate)": ["uncommon"],
    "Mithral Armor (Plate)": ["uncommon"],
    "Mithral Armor (Ring Mail)": ["uncommon"],
    "Mithral Armor (Scale Mail)": ["uncommon"],
    "Mithral Armor (Splint)": ["uncommon"],
    "Moon-Touched Sword (Greatsword)": ["common"],
    "Moon-Touched Sword (Longsword)": ["common"],
    "Moon-Touched Sword (Rapier)": ["common"],
    "Moon-Touched Sword (Scimitar)": ["common"],
    "Moon-Touched Sword (Shortsword)": ["common"],
    "Mystery Key": ["common"],
    "Necklace of Adaptation": ["uncommon"],
    "Necklace of Fireballs": ["rare"],
    "Necklace of Prayer Beads": ["rare"],
    "Nine Lives Stealer": ["very rare"],
    "Nolzur's Marvelous Pigments": ["very rare"],
    "Oath Bow": ["very rare"],
    "Oil of Etherealness": ["rare"],
    "Oil of Sharpness": ["very rare"],
    "Oil of Slipperiness": ["uncommon"],
    "Orb of Direction": ["common"],
    "Orb of Gonging": ["common"],
    "Orb of Time": ["common"],
    "Pearl of Power": ["uncommon"],
    "Perfume of Bewitching": ["common"],
    "Periapt of Health": ["uncommon"],
    "Periapt of Proof against Poison": ["rare"],
    "Periapt of Wound Closure": ["uncommon"],
    "Philter of Love": ["uncommon"],
    "Pipe of Remembrance": ["common"],
    "Pipe of Smoke Monsters": ["common"],
    "Pipes of Haunting": ["uncommon"],
    "Pipes of the Sewers": ["uncommon"],
    "Plate Armor of Etherealness": ["legendary"],
    "Pole of Angling": ["common"],
    "Pole of Collapsing": ["common"],
    "Portable Hole": ["rare"],
    "Pot of Awakening": ["common"],
    "Potion of Animal Friendship": ["uncommon"],
    "Potion of Clairvoyance": ["rare"],
    "Potion of Climbing": ["common"],
    "Potion of Cloud Giant Strength": ["very rare"],
    "Potion of Comprehension": ["common"],
    "Potion of Diminution": ["rare"],
    "Potion of Fire Breath": ["uncommon"],
    "Potion of Fire Giant Strength": ["rare"],
    "Potion of Flying": ["very rare"],
    "Potion of Frost Giant Strength": ["rare"],
    "Potion of Gaseous Form": ["rare"],
    "Potion of Greater Healing": ["uncommon"],
    "Potion of Growth": ["uncommon"],
    "Potion of Healing": ["common"],
    "Potion of Heroism": ["rare"],
    "Potion of Hill Giant Strength": ["uncommon"],
    "Potion of Invisibility": ["very rare"],
    "Potion of Invulnerability": ["rare"],
    "Potion of Longevity": ["very rare"],
    "Potion of Mind Reading": ["rare"],
    "Potion of Poison": ["uncommon"],
    "Potion of Resistance": ["uncommon"],
    "Potion of Speed": ["very rare"],
    "Potion of Stone Giant Strength": ["rare"],
    "Potion of Storm Giant Strength": ["legendary"],
    "Potion of Superior Healing": ["rare"],
    "Potion of Supreme Healing": ["very rare"],
    "Potion of Vitality": ["very rare"],
    "Potion of Watchful Rest": ["common"],
    "Potion of Water Breathing": ["uncommon"],
    "Pressure Capsule": ["common"],
    "Quaal's Feather Token": ["rare"],
    "Quiver of Ehlonna": ["uncommon"],
    "Ring of Air Elemental Command": ["legendary"],
    "Ring of Animal Influence": ["rare"],
    "Ring of Djinni Summoning": ["legendary"],
    "Ring of Earth Elemental Command": ["legendary"],
    "Ring of Evasion": ["rare"],
    "Ring of Feather Falling": ["rare"],
    "Ring of Fire Elemental Command": ["legendary"],
    "Ring of Free Action": ["rare"],
    "Ring of Invisibility": ["legendary"],
    "Ring of Jumping": ["uncommon"],
    "Ring of Mind Shielding": ["uncommon"],
    "Ring of Protection": ["rare"],
    "Ring of Regeneration": ["very rare"],
    "Ring of Resistance": ["rare"],
    "Ring of Shooting Stars": ["very rare"],
    "Ring of Spell Storing": ["rare"],
    "Ring of Spell Turning": ["legendary"],
    "Ring of Swimming": ["uncommon"],
    "Ring of Telekinesis": ["very rare"],
    "Ring of the Ram": ["rare"],
    "Ring of Three Wishes": ["legendary"],
    "Ring of Warmth": ["uncommon"],
    "Ring of Water Elemental Command": ["legendary"],
    "Ring of Water Walking": ["uncommon"],
    "Ring of X-Ray Vision": ["rare"],
    "Robe of Eyes": ["rare"],
    "Robe of Scintillating Colors": ["very rare"],
    "Robe of Stars": ["very rare"],
    "Robe of the Archmagi": ["legendary"],
    "Robe of Useful Items": ["uncommon"],
    "Rod of Absorption": ["very rare"],
    "Rod of Alertness": ["very rare"],
    "Rod of Lordly Might": ["legendary"],
    "Rod of Resurrection": ["legendary"],
    "Rod of Rulership": ["rare"],
    "Rod of Security": ["very rare"],
    "Rod of the Pact Keeper, +1": ["uncommon"],
    "Rod of the Pact Keeper, +2": ["rare"],
    "Rod of the Pact Keeper, +3": ["very rare"],
    "Rope of Climbing": ["uncommon"],
    "Rope of Entanglement": ["rare"],
    "Rope of Mending": ["common"],
    "Ruby of the War Mage": ["common"],
    "Saddle of the Cavalier": ["uncommon"],
    "Scarab of Protection": ["legendary"],
    "Scimitar of Speed": ["very rare"],
    "Scroll of Protection": ["rare"],
    "Sending Stones": ["uncommon"],
    "Sentinel Shield": ["uncommon"],
    "Shield, +1": ["uncommon"],
    "Shield, +2": ["rare"],
    "Shield, +3": ["very rare"],
    "Shield of Expression": ["common"],
    "Shield of Missile Attraction": ["rare"],
    "Slippers of Spider Climbing": ["uncommon"],
    "Smoldering Armor (Breastplate)": ["common"],
    "Smoldering Armor (Chain Mail)": ["common"],
    "Smoldering Armor (Chain Shirt)": ["common"],
    "Smoldering Armor (Half Plate)": ["common"],
    "Smoldering Armor (Hide)": ["common"],
    "Smoldering Armor (Leather)": ["common"],
    "Smoldering Armor (Padded)": ["common"],
    "Smoldering Armor (Plate)": ["common"],
    "Smoldering Armor (Ring Mail)": ["common"],
    "Smoldering Armor (Scale Mail)": ["common"],
    "Smoldering Armor (Splint)": ["common"],
    "Smoldering Armor (Studded Leather)": ["common"],
    "Sovereign Glue": ["legendary"],
    "Spell Scroll (1st Level)": ["common"],
    "Spell Scroll (2nd Level)": ["uncommon"],
    "Spell Scroll (3rd Level)": ["uncommon"],
    "Spell Scroll (4th Level)": ["rare"],
    "Spell Scroll (5th Level)": ["rare"],
    "Spell Scroll (6th Level)": ["very rare"],
    "Spell Scroll (7th Level)": ["very rare"],
    "Spell Scroll (8th Level)": ["very rare"],
    "Spell Scroll (9th Level)": ["legendary"],
    "Spell Scroll (Cantrip)": ["common"],
    "Spellguard Shield": ["very rare"],
    "Sphere of Annihilation": ["legendary"],
    "Staff of Adornment": ["common"],
    "Staff of Birdcalls": ["common"],
    "Staff of Charming": ["rare"],
    "Staff of Fire": ["very rare"],
    "Staff of Flowers": ["common"],
    "Staff of Frost": ["very rare"],
    "Staff of Healing": ["rare"],
    "Staff of Power": ["very rare"],
    "Staff of Striking": ["very rare"],
    "Staff of Swarming Insects": ["rare"],
    "Staff of the Adder": ["uncommon"],
    "Staff of the Magi": ["legendary"],
    "Staff of the Python": ["uncommon"],
    "Staff of the Woodlands": ["rare"],
    "Staff of Thunder and Lightning": ["very rare"],
    "Staff of Withering": ["rare"],
    "Stone of Controlling Earth Elementals": ["rare"],
    "Stone of Good Luck": ["uncommon"],
    "Sun Blade": ["rare"],
    "Sword of Answering": ["legendary"],
    "Sword of Life Stealing": ["rare"],
    "Sword of Sharpness": ["very rare"],
    "Sword of Vengeance": ["uncommon"],
    "Sword of Wounding": ["rare"],
    "Talisman of Pure Good": ["legendary"],
    "Talisman of the Sphere": ["legendary"],
    "Talisman of Ultimate Evil": ["legendary"],
    "Talking Doll": ["common"],
    "Tankard of Plenty": ["common"],
    "Tankard of Sobriety": ["common"],
    "Tentacle Rod": ["rare"],
    "Tome of Clear Thought": ["very rare"],
    "Tome of Leadership and Influence": ["very rare"],
    "Tome of the Stilled Tongue": ["legendary"],
    "Tome of Understanding": ["very rare"],
    "Trident of Fish Command": ["uncommon"],
    "Unbreakable Arrow, 5": ["common"],
    "Universal Solvent": ["legendary"],
    "Veteran's Cane": ["common"],
    "Vicious Weapon": ["rare"],
    "Vorpal Sword": ["legendary"],
    "Walloping Ammunition (Arrow), 5": ["common"],
    "Walloping Ammunition (Blowgun Needle), 5": ["common"],
    "Walloping Ammunition (Crossbow Bolt), 5": ["common"],
    "Walloping Ammunition (Sling Bullet), 5": ["common"],
    "Wand of Binding": ["rare"],
    "Wand of Conducting": ["common"],
    "Wand of Enemy Detection": ["rare"],
    "Wand of Fear": ["rare"],
    "Wand of Fireballs": ["rare"],
    "Wand of Lightning Bolts": ["rare"],
    "Wand of Magic Detection": ["uncommon"],
    "Wand of Magic Missiles": ["uncommon"],
    "Wand of Paralysis": ["rare"],
    "Wand of Polymorph": ["very rare"],
    "Wand of Pyrotechnics": ["common"],
    "Wand of Scowls": ["common"],
    "Wand of Secrets": ["uncommon"],
    "Wand of Smiles": ["common"],
    "Wand of the War Mage, +1": ["uncommon"],
    "Wand of the War Mage, +2": ["rare"],
    "Wand of the War Mage, +3": ["very rare"],
    "Wand of Web": ["uncommon"],
    "Wand of Wonder": ["rare"],
    "Weapon, +1": ["uncommon"],
    "Weapon, +2": ["rare"],
    "Weapon, +3": ["very rare"],
    "Weapon of Warning": ["uncommon"],
    "Well of Many Worlds": ["legendary"],
    "Wind Fan": ["uncommon"],
    "Winged Boots": ["uncommon"],
    "Wings of Flying": ["rare"],
}

magic_rarities = ["common", "uncommon", "rare", "very rare", "legendary"]

cp_values = dict(zip(magic_rarities,
                     [7500, 30000, 275000, 2750000, 27500000]))
