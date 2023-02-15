from flask import Flask, request
import requests
# barbarian = {"index":"barbarian","name":"Barbarian","hit_die":12,"proficiency_choices":[{"desc":"Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival","choose":2,"type":"proficiencies","from":{"option_set_type":"options_array","options":[{"option_type":"reference","item":{"index":"skill-animal-handling","name":"Skill: Animal Handling","url":"/api/proficiencies/skill-animal-handling"}},{"option_type":"reference","item":{"index":"skill-athletics","name":"Skill: Athletics","url":"/api/proficiencies/skill-athletics"}},{"option_type":"reference","item":{"index":"skill-intimidation","name":"Skill: Intimidation","url":"/api/proficiencies/skill-intimidation"}},{"option_type":"reference","item":{"index":"skill-nature","name":"Skill: Nature","url":"/api/proficiencies/skill-nature"}},{"option_type":"reference","item":{"index":"skill-perception","name":"Skill: Perception","url":"/api/proficiencies/skill-perception"}},{"option_type":"reference","item":{"index":"skill-survival","name":"Skill: Survival","url":"/api/proficiencies/skill-survival"}}]}}],"proficiencies":[{"index":"light-armor","name":"Light Armor","url":"/api/proficiencies/light-armor"},{"index":"medium-armor","name":"Medium Armor","url":"/api/proficiencies/medium-armor"},{"index":"shields","name":"Shields","url":"/api/proficiencies/shields"},{"index":"simple-weapons","name":"Simple Weapons","url":"/api/proficiencies/simple-weapons"},{"index":"martial-weapons","name":"Martial Weapons","url":"/api/proficiencies/martial-weapons"},{"index":"saving-throw-str","name":"Saving Throw: STR","url":"/api/proficiencies/saving-throw-str"},{"index":"saving-throw-con","name":"Saving Throw: CON","url":"/api/proficiencies/saving-throw-con"}],"saving_throws":[{"index":"str","name":"STR","url":"/api/ability-scores/str"},{"index":"con","name":"CON","url":"/api/ability-scores/con"}],"starting_equipment":[{"equipment":{"index":"explorers-pack","name":"Explorer's Pack","url":"/api/equipment/explorers-pack"},"quantity":1},{"equipment":{"index":"javelin","name":"Javelin","url":"/api/equipment/javelin"},"quantity":4}],"starting_equipment_options":[{"desc":"(a) a greataxe or (b) any martial melee weapon","choose":1,"type":"equipment","from":{"option_set_type":"options_array","options":[{"option_type":"counted_reference","count":1,"of":{"index":"greataxe","name":"Greataxe","url":"/api/equipment/greataxe"}},{"option_type":"choice","choice":{"desc":"any martial melee weapon","choose":1,"type":"equipment","from":{"option_set_type":"equipment_category","equipment_category":{"index":"martial-melee-weapons","name":"Martial Melee Weapons","url":"/api/equipment-categories/martial-melee-weapons"}}}}]}},{"desc":"(a) two handaxes or (b) any simple weapon","choose":1,"type":"equipment","from":{"option_set_type":"options_array","options":[{"option_type":"counted_reference","count":2,"of":{"index":"handaxe","name":"Handaxe","url":"/api/equipment/handaxe"}},{"option_type":"choice","choice":{"desc":"any simple weapon","choose":1,"type":"equipment","from":{"option_set_type":"equipment_category","equipment_category":{"index":"simple-weapons","name":"Simple Weapons","url":"/api/equipment-categories/simple-weapons"}}}}]}}],"class_levels":"/api/classes/barbarian/levels","multi_classing":{"prerequisites":[{"ability_score":{"index":"str","name":"STR","url":"/api/ability-scores/str"},"minimum_score":13}],"proficiencies":[{"index":"shields","name":"Shields","url":"/api/proficiencies/shields"},{"index":"simple-weapons","name":"Simple Weapons","url":"/api/proficiencies/simple-weapons"},{"index":"martial-weapons","name":"Martial Weapons","url":"/api/proficiencies/martial-weapons"}]},"subclasses":[{"index":"berserker","name":"Berserker","url":"/api/subclasses/berserker"}],"url":"/api/classes/barbarian"}
# races = {"count":9,"results":[{"index":"dragonborn","name":"Dragonborn","url":"/api/races/dragonborn"},{"index":"dwarf","name":"Dwarf","url":"/api/races/dwarf"},{"index":"elf","name":"Elf","url":"/api/races/elf"},{"index":"gnome","name":"Gnome","url":"/api/races/gnome"},{"index":"half-elf","name":"Half-Elf","url":"/api/races/half-elf"},{"index":"half-orc","name":"Half-Orc","url":"/api/races/half-orc"},{"index":"halfling","name":"Halfling","url":"/api/races/halfling"},{"index":"human","name":"Human","url":"/api/races/human"},{"index":"tiefling","name":"Tiefling","url":"/api/races/tiefling"}]}
elf = {"index":"elf","name":"Elf","speed":30,"ability_bonuses":[{"ability_score":{"index":"dex","name":"DEX","url":"/api/ability-scores/dex"},"bonus":2}],"age":"Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.","alignment":"Elves love freedom, variety, and self-expression, so they lean strongly toward the gentler aspects of chaos. They value and protect others' freedom as well as their own, and they are more often good than not. The drow are an exception; their exile has made them vicious and dangerous. Drow are more often evil than not.","size":"Medium","size_description":"Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.","starting_proficiencies":[{"index":"skill-perception","name":"Skill: Perception","url":"/api/proficiencies/skill-perception"}],"languages":[{"index":"common","name":"Common","url":"/api/languages/common"},{"index":"elvish","name":"Elvish","url":"/api/languages/elvish"}],"language_desc":"You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among other races. Many bards learn their language so they can add Elvish ballads to their repertoires.","traits":[{"index":"darkvision","name":"Darkvision","url":"/api/traits/darkvision"},{"index":"fey-ancestry","name":"Fey Ancestry","url":"/api/traits/fey-ancestry"},{"index":"trance","name":"Trance","url":"/api/traits/trance"},{"index":"keen-senses","name":"Keen Senses","url":"/api/traits/keen-senses"}],"subraces":[{"index":"high-elf","name":"High Elf","url":"/api/subraces/high-elf"}],"url":"/api/races/elf"}

# acid = {"index":"acid-arrow","name":"Acid Arrow","desc":["A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn."],"higher_level":["When you cast this spell using a spell slot of 3rd level or higher, the damage (both initial and later) increases by 1d4 for each slot level above 2nd."],"range":"90 feet","components":["V","S","M"],"material":"Powdered rhubarb leaf and an adder's stomach.","ritual":false,"duration":"Instantaneous","concentration":false,"casting_time":"1 action","level":2,"attack_type":"ranged","damage":{"damage_type":{"index":"acid","name":"Acid","url":"/api/damage-types/acid"},"damage_at_slot_level":{"2":"4d4","3":"5d4","4":"6d4","5":"7d4","6":"8d4","7":"9d4","8":"10d4","9":"11d4"}},"school":{"index":"evocation","name":"Evocation","url":"/api/magic-schools/evocation"},"classes":[{"index":"wizard","name":"Wizard","url":"/api/classes/wizard"}],"subclasses":[{"index":"lore","name":"Lore","url":"/api/subclasses/lore"},{"index":"land","name":"Land","url":"/api/subclasses/land"}],"url":"/api/spells/acid-arrow"}

# animalfriends = {"higher_level":[],"index":"animal-friendship","name":"Animal Friendship","desc":["This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a wisdom saving throw or be charmed by you for the spell's duration. If you or one of your companions harms the target, the spells ends."],"range":"30 feet","components":["V","S","M"],"material":"A morsel of food.","ritual":false,"duration":"24 hours","concentration":false,"casting_time":"1 action","level":1,"dc":{"dc_type":{"index":"wis","name":"WIS","url":"/api/ability-scores/wis"},"dc_success":"none"},"school":{"index":"enchantment","name":"Enchantment","url":"/api/magic-schools/enchantment"},"classes":[{"index":"bard","name":"Bard","url":"/api/classes/bard"},{"index":"cleric","name":"Cleric","url":"/api/classes/cleric"},{"index":"druid","name":"Druid","url":"/api/classes/druid"},{"index":"ranger","name":"Ranger","url":"/api/classes/ranger"}],"subclasses":[],"url":"/api/spells/animal-friendship"}

# print(elf.keys())
# print(animalfriends)
# print('these are spell names')
# print(spells["results"])
# print(spells["count"])
# for name in spells["results"]:
#     print(spells["name"])
# print(elf.keys())
# print('elf alignment:')
# print(elf["alignment"])
# print()
# print('elf age:')
# print(elf["age"])
# print()
# print('elf ability bonuses:')
# print(elf["ability_bonuses"])
# print()
# print('elf size:')
# print(elf["size"])
# print()
# print('start profs:')
# print(elf["starting_proficiencies"])
# print()
# print('language:')
# print(elf["languages"])
# print()
# print('elf traits:')
# print(elf["traits"])
# print()
# print('subraces:')
# print(elf["subraces"])
# print()
# print('elf url')
# print(elf["url"])
# print()
# print()
# for data in elf["traits"]:
#     print(data["name"])
# print()
# print()
# print(elf["traits"][:])
# # print(data.keys())
# # print(data["proficiencies"])
# # for dict in data["proficiencies"]:
#     # print(dict["name"])
# print()
# print()
# print("these are the races")
# print(races)
# print()
# print()
# print("these are the keys")
# print(races.keys())
# print()
# print()
# for race in races["results"]:
#     print(race["name"])


# print()
# print('this is elf')
# print(elf)
# print()
# print('this is elf speed')
# print(elf["speed"])
# print()
# print('this is elf age')
# print(elf["age"])
# print()
# print('this is elf languages')
# print(elf["languages"])
# print()
# for data in elf:
#     print(elf["languages"])
# print(elf["language_desc"])

# print(elf["starting_proficiencies"])
# print()
# for data in elf["starting_proficiencies"]:
#     print(data["name"])


                # <div class="col-4">
                #     <section id="skill_proficiencies">
                #         <label for="skill_proficiency_options"> select a skill proficiency </label>
                #         <select id="skill_proficiencies" name="skill_proficiencies">
                #             {% for skill_proficiency in skill_proficiencies %}
                #             <option value="{{ skill_proficiency }}">{{ skill_proficiency }}</option>
                #             {% endfor %}
                #         </select>
                #     </section>
                # </div>


spells = {"count":319,"results":[{"index":"acid-arrow","name":"Acid Arrow","url":"/api/spells/acid-arrow"},{"index":"acid-splash","name":"Acid Splash","url":"/api/spells/acid-splash"},{"index":"aid","name":"Aid","url":"/api/spells/aid"},{"index":"alarm","name":"Alarm","url":"/api/spells/alarm"},{"index":"alter-self","name":"Alter Self","url":"/api/spells/alter-self"},{"index":"animal-friendship","name":"Animal Friendship","url":"/api/spells/animal-friendship"},{"index":"animal-messenger","name":"Animal Messenger","url":"/api/spells/animal-messenger"},{"index":"animal-shapes","name":"Animal Shapes","url":"/api/spells/animal-shapes"},{"index":"animate-dead","name":"Animate Dead","url":"/api/spells/animate-dead"},{"index":"animate-objects","name":"Animate Objects","url":"/api/spells/animate-objects"},{"index":"antilife-shell","name":"Antilife Shell","url":"/api/spells/antilife-shell"},{"index":"antimagic-field","name":"Antimagic Field","url":"/api/spells/antimagic-field"},{"index":"antipathy-sympathy","name":"Antipathy/Sympathy","url":"/api/spells/antipathy-sympathy"},{"index":"arcane-eye","name":"Arcane Eye","url":"/api/spells/arcane-eye"},{"index":"arcane-hand","name":"Arcane Hand","url":"/api/spells/arcane-hand"},{"index":"arcane-lock","name":"Arcane Lock","url":"/api/spells/arcane-lock"},{"index":"arcane-sword","name":"Arcane Sword","url":"/api/spells/arcane-sword"},{"index":"arcanists-magic-aura","name":"Arcanist's Magic Aura","url":"/api/spells/arcanists-magic-aura"},{"index":"astral-projection","name":"Astral Projection","url":"/api/spells/astral-projection"},{"index":"augury","name":"Augury","url":"/api/spells/augury"},{"index":"awaken","name":"Awaken","url":"/api/spells/awaken"},{"index":"bane","name":"Bane","url":"/api/spells/bane"},{"index":"banishment","name":"Banishment","url":"/api/spells/banishment"},{"index":"barkskin","name":"Barkskin","url":"/api/spells/barkskin"},{"index":"beacon-of-hope","name":"Beacon of Hope","url":"/api/spells/beacon-of-hope"},{"index":"bestow-curse","name":"Bestow Curse","url":"/api/spells/bestow-curse"},{"index":"black-tentacles","name":"Black Tentacles","url":"/api/spells/black-tentacles"},{"index":"blade-barrier","name":"Blade Barrier","url":"/api/spells/blade-barrier"},{"index":"bless","name":"Bless","url":"/api/spells/bless"},{"index":"blight","name":"Blight","url":"/api/spells/blight"},{"index":"blindness-deafness","name":"Blindness/Deafness","url":"/api/spells/blindness-deafness"},{"index":"blink","name":"Blink","url":"/api/spells/blink"},{"index":"blur","name":"Blur","url":"/api/spells/blur"},{"index":"branding-smite","name":"Branding Smite","url":"/api/spells/branding-smite"},{"index":"burning-hands","name":"Burning Hands","url":"/api/spells/burning-hands"},{"index":"call-lightning","name":"Call Lightning","url":"/api/spells/call-lightning"},{"index":"calm-emotions","name":"Calm Emotions","url":"/api/spells/calm-emotions"},{"index":"chain-lightning","name":"Chain Lightning","url":"/api/spells/chain-lightning"},{"index":"charm-person","name":"Charm Person","url":"/api/spells/charm-person"},{"index":"chill-touch","name":"Chill Touch","url":"/api/spells/chill-touch"},{"index":"circle-of-death","name":"Circle of Death","url":"/api/spells/circle-of-death"},{"index":"clairvoyance","name":"Clairvoyance","url":"/api/spells/clairvoyance"},{"index":"clone","name":"Clone","url":"/api/spells/clone"},{"index":"cloudkill","name":"Cloudkill","url":"/api/spells/cloudkill"},{"index":"color-spray","name":"Color Spray","url":"/api/spells/color-spray"},{"index":"command","name":"Command","url":"/api/spells/command"},{"index":"commune","name":"Commune","url":"/api/spells/commune"},{"index":"commune-with-nature","name":"Commune With Nature","url":"/api/spells/commune-with-nature"},{"index":"comprehend-languages","name":"Comprehend Languages","url":"/api/spells/comprehend-languages"},{"index":"compulsion","name":"Compulsion","url":"/api/spells/compulsion"},{"index":"cone-of-cold","name":"Cone of Cold","url":"/api/spells/cone-of-cold"},{"index":"confusion","name":"Confusion","url":"/api/spells/confusion"},{"index":"conjure-animals","name":"Conjure Animals","url":"/api/spells/conjure-animals"},{"index":"conjure-celestial","name":"Conjure Celestial","url":"/api/spells/conjure-celestial"},{"index":"conjure-elemental","name":"Conjure Elemental","url":"/api/spells/conjure-elemental"},{"index":"conjure-fey","name":"Conjure Fey","url":"/api/spells/conjure-fey"},{"index":"conjure-minor-elementals","name":"Conjure Minor Elementals","url":"/api/spells/conjure-minor-elementals"},{"index":"conjure-woodland-beings","name":"Conjure Woodland Beings","url":"/api/spells/conjure-woodland-beings"},{"index":"contact-other-plane","name":"Contact Other Plane","url":"/api/spells/contact-other-plane"},{"index":"contagion","name":"Contagion","url":"/api/spells/contagion"},{"index":"contingency","name":"Contingency","url":"/api/spells/contingency"},{"index":"continual-flame","name":"Continual Flame","url":"/api/spells/continual-flame"},{"index":"control-water","name":"Control Water","url":"/api/spells/control-water"},{"index":"control-weather","name":"Control Weather","url":"/api/spells/control-weather"},{"index":"counterspell","name":"Counterspell","url":"/api/spells/counterspell"},{"index":"create-food-and-water","name":"Create Food and Water","url":"/api/spells/create-food-and-water"},{"index":"create-or-destroy-water","name":"Create or Destroy Water","url":"/api/spells/create-or-destroy-water"},{"index":"create-undead","name":"Create Undead","url":"/api/spells/create-undead"},{"index":"creation","name":"Creation","url":"/api/spells/creation"},{"index":"cure-wounds","name":"Cure Wounds","url":"/api/spells/cure-wounds"},{"index":"dancing-lights","name":"Dancing Lights","url":"/api/spells/dancing-lights"},{"index":"darkness","name":"Darkness","url":"/api/spells/darkness"},{"index":"darkvision","name":"Darkvision","url":"/api/spells/darkvision"},{"index":"daylight","name":"Daylight","url":"/api/spells/daylight"},{"index":"death-ward","name":"Death Ward","url":"/api/spells/death-ward"},{"index":"delayed-blast-fireball","name":"Delayed Blast Fireball","url":"/api/spells/delayed-blast-fireball"},{"index":"demiplane","name":"Demiplane","url":"/api/spells/demiplane"},{"index":"detect-evil-and-good","name":"Detect Evil and Good","url":"/api/spells/detect-evil-and-good"},{"index":"detect-magic","name":"Detect Magic","url":"/api/spells/detect-magic"},{"index":"detect-poison-and-disease","name":"Detect Poison and Disease","url":"/api/spells/detect-poison-and-disease"},{"index":"detect-thoughts","name":"Detect Thoughts","url":"/api/spells/detect-thoughts"},{"index":"dimension-door","name":"Dimension Door","url":"/api/spells/dimension-door"},{"index":"disguise-self","name":"Disguise Self","url":"/api/spells/disguise-self"},{"index":"disintegrate","name":"Disintegrate","url":"/api/spells/disintegrate"},{"index":"dispel-evil-and-good","name":"Dispel Evil and Good","url":"/api/spells/dispel-evil-and-good"},{"index":"dispel-magic","name":"Dispel Magic","url":"/api/spells/dispel-magic"},{"index":"divination","name":"Divination","url":"/api/spells/divination"},{"index":"divine-favor","name":"Divine Favor","url":"/api/spells/divine-favor"},{"index":"divine-word","name":"Divine Word","url":"/api/spells/divine-word"},{"index":"dominate-beast","name":"Dominate Beast","url":"/api/spells/dominate-beast"},{"index":"dominate-monster","name":"Dominate Monster","url":"/api/spells/dominate-monster"},{"index":"dominate-person","name":"Dominate Person","url":"/api/spells/dominate-person"},{"index":"dream","name":"Dream","url":"/api/spells/dream"},{"index":"druidcraft","name":"Druidcraft","url":"/api/spells/druidcraft"},{"index":"earthquake","name":"Earthquake","url":"/api/spells/earthquake"},{"index":"eldritch-blast","name":"Eldritch Blast","url":"/api/spells/eldritch-blast"},{"index":"enhance-ability","name":"Enhance Ability","url":"/api/spells/enhance-ability"},{"index":"enlarge-reduce","name":"Enlarge/Reduce","url":"/api/spells/enlarge-reduce"},{"index":"entangle","name":"Entangle","url":"/api/spells/entangle"},{"index":"enthrall","name":"Enthrall","url":"/api/spells/enthrall"},{"index":"etherealness","name":"Etherealness","url":"/api/spells/etherealness"},{"index":"expeditious-retreat","name":"Expeditious Retreat","url":"/api/spells/expeditious-retreat"},{"index":"eyebite","name":"Eyebite","url":"/api/spells/eyebite"},{"index":"fabricate","name":"Fabricate","url":"/api/spells/fabricate"},{"index":"faerie-fire","name":"Faerie Fire","url":"/api/spells/faerie-fire"},{"index":"faithful-hound","name":"Faithful Hound","url":"/api/spells/faithful-hound"},{"index":"false-life","name":"False Life","url":"/api/spells/false-life"},{"index":"fear","name":"Fear","url":"/api/spells/fear"},{"index":"feather-fall","name":"Feather Fall","url":"/api/spells/feather-fall"},{"index":"feeblemind","name":"Feeblemind","url":"/api/spells/feeblemind"},{"index":"find-familiar","name":"Find Familiar","url":"/api/spells/find-familiar"},{"index":"find-steed","name":"Find Steed","url":"/api/spells/find-steed"},{"index":"find-the-path","name":"Find the Path","url":"/api/spells/find-the-path"},{"index":"find-traps","name":"Find Traps","url":"/api/spells/find-traps"},{"index":"finger-of-death","name":"Finger of Death","url":"/api/spells/finger-of-death"},{"index":"fire-bolt","name":"Fire Bolt","url":"/api/spells/fire-bolt"},{"index":"fire-shield","name":"Fire Shield","url":"/api/spells/fire-shield"},{"index":"fire-storm","name":"Fire Storm","url":"/api/spells/fire-storm"},{"index":"fireball","name":"Fireball","url":"/api/spells/fireball"},{"index":"flame-blade","name":"Flame Blade","url":"/api/spells/flame-blade"},{"index":"flame-strike","name":"Flame Strike","url":"/api/spells/flame-strike"},{"index":"flaming-sphere","name":"Flaming Sphere","url":"/api/spells/flaming-sphere"},{"index":"flesh-to-stone","name":"Flesh to Stone","url":"/api/spells/flesh-to-stone"},{"index":"floating-disk","name":"Floating Disk","url":"/api/spells/floating-disk"},{"index":"fly","name":"Fly","url":"/api/spells/fly"},{"index":"fog-cloud","name":"Fog Cloud","url":"/api/spells/fog-cloud"},{"index":"forbiddance","name":"Forbiddance","url":"/api/spells/forbiddance"},{"index":"forcecage","name":"Forcecage","url":"/api/spells/forcecage"},{"index":"foresight","name":"Foresight","url":"/api/spells/foresight"},{"index":"freedom-of-movement","name":"Freedom of Movement","url":"/api/spells/freedom-of-movement"},{"index":"freezing-sphere","name":"Freezing Sphere","url":"/api/spells/freezing-sphere"},{"index":"gaseous-form","name":"Gaseous Form","url":"/api/spells/gaseous-form"},{"index":"gate","name":"Gate","url":"/api/spells/gate"},{"index":"geas","name":"Geas","url":"/api/spells/geas"},{"index":"gentle-repose","name":"Gentle Repose","url":"/api/spells/gentle-repose"},{"index":"giant-insect","name":"Giant Insect","url":"/api/spells/giant-insect"},{"index":"glibness","name":"Glibness","url":"/api/spells/glibness"},{"index":"globe-of-invulnerability","name":"Globe of Invulnerability","url":"/api/spells/globe-of-invulnerability"},{"index":"glyph-of-warding","name":"Glyph of Warding","url":"/api/spells/glyph-of-warding"},{"index":"goodberry","name":"Goodberry","url":"/api/spells/goodberry"},{"index":"grease","name":"Grease","url":"/api/spells/grease"},{"index":"greater-invisibility","name":"Greater Invisibility","url":"/api/spells/greater-invisibility"},{"index":"greater-restoration","name":"Greater Restoration","url":"/api/spells/greater-restoration"},{"index":"guardian-of-faith","name":"Guardian of Faith","url":"/api/spells/guardian-of-faith"},{"index":"guards-and-wards","name":"Guards and Wards","url":"/api/spells/guards-and-wards"},{"index":"guidance","name":"Guidance","url":"/api/spells/guidance"},{"index":"guiding-bolt","name":"Guiding Bolt","url":"/api/spells/guiding-bolt"},{"index":"gust-of-wind","name":"Gust of Wind","url":"/api/spells/gust-of-wind"},{"index":"hallow","name":"Hallow","url":"/api/spells/hallow"},{"index":"hallucinatory-terrain","name":"Hallucinatory Terrain","url":"/api/spells/hallucinatory-terrain"},{"index":"harm","name":"Harm","url":"/api/spells/harm"},{"index":"haste","name":"Haste","url":"/api/spells/haste"},{"index":"heal","name":"Heal","url":"/api/spells/heal"},{"index":"healing-word","name":"Healing Word","url":"/api/spells/healing-word"},{"index":"heat-metal","name":"Heat Metal","url":"/api/spells/heat-metal"},{"index":"hellish-rebuke","name":"Hellish Rebuke","url":"/api/spells/hellish-rebuke"},{"index":"heroes-feast","name":"Heroes' Feast","url":"/api/spells/heroes-feast"},{"index":"heroism","name":"Heroism","url":"/api/spells/heroism"},{"index":"hideous-laughter","name":"Hideous Laughter","url":"/api/spells/hideous-laughter"},{"index":"hold-monster","name":"Hold Monster","url":"/api/spells/hold-monster"},{"index":"hold-person","name":"Hold Person","url":"/api/spells/hold-person"},{"index":"holy-aura","name":"Holy Aura","url":"/api/spells/holy-aura"},{"index":"hunters-mark","name":"Hunter's Mark","url":"/api/spells/hunters-mark"},{"index":"hypnotic-pattern","name":"Hypnotic Pattern","url":"/api/spells/hypnotic-pattern"},{"index":"ice-storm","name":"Ice Storm","url":"/api/spells/ice-storm"},{"index":"identify","name":"Identify","url":"/api/spells/identify"},{"index":"illusory-script","name":"Illusory Script","url":"/api/spells/illusory-script"},{"index":"imprisonment","name":"Imprisonment","url":"/api/spells/imprisonment"},{"index":"incendiary-cloud","name":"Incendiary Cloud","url":"/api/spells/incendiary-cloud"},{"index":"inflict-wounds","name":"Inflict Wounds","url":"/api/spells/inflict-wounds"},{"index":"insect-plague","name":"Insect Plague","url":"/api/spells/insect-plague"},{"index":"instant-summons","name":"Instant Summons","url":"/api/spells/instant-summons"},{"index":"invisibility","name":"Invisibility","url":"/api/spells/invisibility"},{"index":"irresistible-dance","name":"Irresistible Dance","url":"/api/spells/irresistible-dance"},{"index":"jump","name":"Jump","url":"/api/spells/jump"},{"index":"knock","name":"Knock","url":"/api/spells/knock"},{"index":"legend-lore","name":"Legend Lore","url":"/api/spells/legend-lore"},{"index":"lesser-restoration","name":"Lesser Restoration","url":"/api/spells/lesser-restoration"},{"index":"levitate","name":"Levitate","url":"/api/spells/levitate"},{"index":"light","name":"Light","url":"/api/spells/light"},{"index":"lightning-bolt","name":"Lightning Bolt","url":"/api/spells/lightning-bolt"},{"index":"locate-animals-or-plants","name":"Locate Animals or Plants","url":"/api/spells/locate-animals-or-plants"},{"index":"locate-creature","name":"Locate Creature","url":"/api/spells/locate-creature"},{"index":"locate-object","name":"Locate Object","url":"/api/spells/locate-object"},{"index":"longstrider","name":"Longstrider","url":"/api/spells/longstrider"},{"index":"mage-armor","name":"Mage Armor","url":"/api/spells/mage-armor"},{"index":"mage-hand","name":"Mage Hand","url":"/api/spells/mage-hand"},{"index":"magic-circle","name":"Magic Circle","url":"/api/spells/magic-circle"},{"index":"magic-jar","name":"Magic Jar","url":"/api/spells/magic-jar"},{"index":"magic-missile","name":"Magic Missile","url":"/api/spells/magic-missile"},{"index":"magic-mouth","name":"Magic Mouth","url":"/api/spells/magic-mouth"},{"index":"magic-weapon","name":"Magic Weapon","url":"/api/spells/magic-weapon"},{"index":"magnificent-mansion","name":"Magnificent Mansion","url":"/api/spells/magnificent-mansion"},{"index":"major-image","name":"Major Image","url":"/api/spells/major-image"},{"index":"mass-cure-wounds","name":"Mass Cure Wounds","url":"/api/spells/mass-cure-wounds"},{"index":"mass-heal","name":"Mass Heal","url":"/api/spells/mass-heal"},{"index":"mass-healing-word","name":"Mass Healing Word","url":"/api/spells/mass-healing-word"},{"index":"mass-suggestion","name":"Mass Suggestion","url":"/api/spells/mass-suggestion"},{"index":"maze","name":"Maze","url":"/api/spells/maze"},{"index":"meld-into-stone","name":"Meld Into Stone","url":"/api/spells/meld-into-stone"},{"index":"mending","name":"Mending","url":"/api/spells/mending"},{"index":"message","name":"Message","url":"/api/spells/message"},{"index":"meteor-swarm","name":"Meteor Swarm","url":"/api/spells/meteor-swarm"},{"index":"mind-blank","name":"Mind Blank","url":"/api/spells/mind-blank"},{"index":"minor-illusion","name":"Minor Illusion","url":"/api/spells/minor-illusion"},{"index":"mirage-arcane","name":"Mirage Arcane","url":"/api/spells/mirage-arcane"},{"index":"mirror-image","name":"Mirror Image","url":"/api/spells/mirror-image"},{"index":"mislead","name":"Mislead","url":"/api/spells/mislead"},{"index":"misty-step","name":"Misty Step","url":"/api/spells/misty-step"},{"index":"modify-memory","name":"Modify Memory","url":"/api/spells/modify-memory"},{"index":"moonbeam","name":"Moonbeam","url":"/api/spells/moonbeam"},{"index":"move-earth","name":"Move Earth","url":"/api/spells/move-earth"},{"index":"nondetection","name":"Nondetection","url":"/api/spells/nondetection"},{"index":"pass-without-trace","name":"Pass Without Trace","url":"/api/spells/pass-without-trace"},{"index":"passwall","name":"Passwall","url":"/api/spells/passwall"},{"index":"phantasmal-killer","name":"Phantasmal Killer","url":"/api/spells/phantasmal-killer"},{"index":"phantom-steed","name":"Phantom Steed","url":"/api/spells/phantom-steed"},{"index":"planar-ally","name":"Planar Ally","url":"/api/spells/planar-ally"},{"index":"planar-binding","name":"Planar Binding","url":"/api/spells/planar-binding"},{"index":"plane-shift","name":"Plane Shift","url":"/api/spells/plane-shift"},{"index":"plant-growth","name":"Plant Growth","url":"/api/spells/plant-growth"},{"index":"poison-spray","name":"Poison Spray","url":"/api/spells/poison-spray"},{"index":"polymorph","name":"Polymorph","url":"/api/spells/polymorph"},{"index":"power-word-kill","name":"Power Word Kill","url":"/api/spells/power-word-kill"},{"index":"power-word-stun","name":"Power Word Stun","url":"/api/spells/power-word-stun"},{"index":"prayer-of-healing","name":"Prayer of Healing","url":"/api/spells/prayer-of-healing"},{"index":"prestidigitation","name":"Prestidigitation","url":"/api/spells/prestidigitation"},{"index":"prismatic-spray","name":"Prismatic Spray","url":"/api/spells/prismatic-spray"},{"index":"prismatic-wall","name":"Prismatic Wall","url":"/api/spells/prismatic-wall"},{"index":"private-sanctum","name":"Private Sanctum","url":"/api/spells/private-sanctum"},{"index":"produce-flame","name":"Produce Flame","url":"/api/spells/produce-flame"},{"index":"programmed-illusion","name":"Programmed Illusion","url":"/api/spells/programmed-illusion"},{"index":"project-image","name":"Project Image","url":"/api/spells/project-image"},{"index":"protection-from-energy","name":"Protection From Energy","url":"/api/spells/protection-from-energy"},{"index":"protection-from-evil-and-good","name":"Protection from Evil and Good","url":"/api/spells/protection-from-evil-and-good"},{"index":"protection-from-poison","name":"Protection from Poison","url":"/api/spells/protection-from-poison"},{"index":"purify-food-and-drink","name":"Purify Food and Drink","url":"/api/spells/purify-food-and-drink"},{"index":"raise-dead","name":"Raise Dead","url":"/api/spells/raise-dead"},{"index":"ray-of-enfeeblement","name":"Ray of Enfeeblement","url":"/api/spells/ray-of-enfeeblement"},{"index":"ray-of-frost","name":"Ray of Frost","url":"/api/spells/ray-of-frost"},{"index":"regenerate","name":"Regenerate","url":"/api/spells/regenerate"},{"index":"reincarnate","name":"Reincarnate","url":"/api/spells/reincarnate"},{"index":"remove-curse","name":"Remove Curse","url":"/api/spells/remove-curse"},{"index":"resilient-sphere","name":"Resilient Sphere","url":"/api/spells/resilient-sphere"},{"index":"resistance","name":"Resistance","url":"/api/spells/resistance"},{"index":"resurrection","name":"Resurrection","url":"/api/spells/resurrection"},{"index":"reverse-gravity","name":"Reverse Gravity","url":"/api/spells/reverse-gravity"},{"index":"revivify","name":"Revivify","url":"/api/spells/revivify"},{"index":"rope-trick","name":"Rope Trick","url":"/api/spells/rope-trick"},{"index":"sacred-flame","name":"Sacred Flame","url":"/api/spells/sacred-flame"},{"index":"sanctuary","name":"Sanctuary","url":"/api/spells/sanctuary"},{"index":"scorching-ray","name":"Scorching Ray","url":"/api/spells/scorching-ray"},{"index":"scrying","name":"Scrying","url":"/api/spells/scrying"},{"index":"secret-chest","name":"Secret Chest","url":"/api/spells/secret-chest"},{"index":"see-invisibility","name":"See Invisibility","url":"/api/spells/see-invisibility"},{"index":"seeming","name":"Seeming","url":"/api/spells/seeming"},{"index":"sending","name":"Sending","url":"/api/spells/sending"},{"index":"sequester","name":"Sequester","url":"/api/spells/sequester"},{"index":"shapechange","name":"Shapechange","url":"/api/spells/shapechange"},{"index":"shatter","name":"Shatter","url":"/api/spells/shatter"},{"index":"shield","name":"Shield","url":"/api/spells/shield"},{"index":"shield-of-faith","name":"Shield of Faith","url":"/api/spells/shield-of-faith"},{"index":"shillelagh","name":"Shillelagh","url":"/api/spells/shillelagh"},{"index":"shocking-grasp","name":"Shocking Grasp","url":"/api/spells/shocking-grasp"},{"index":"silence","name":"Silence","url":"/api/spells/silence"},{"index":"silent-image","name":"Silent Image","url":"/api/spells/silent-image"},{"index":"simulacrum","name":"Simulacrum","url":"/api/spells/simulacrum"},{"index":"sleep","name":"Sleep","url":"/api/spells/sleep"},{"index":"sleet-storm","name":"Sleet Storm","url":"/api/spells/sleet-storm"},{"index":"slow","name":"Slow","url":"/api/spells/slow"},{"index":"spare-the-dying","name":"Spare the Dying","url":"/api/spells/spare-the-dying"},{"index":"speak-with-animals","name":"Speak with Animals","url":"/api/spells/speak-with-animals"},{"index":"speak-with-dead","name":"Speak with Dead","url":"/api/spells/speak-with-dead"},{"index":"speak-with-plants","name":"Speak with Plants","url":"/api/spells/speak-with-plants"},{"index":"spider-climb","name":"Spider Climb","url":"/api/spells/spider-climb"},{"index":"spike-growth","name":"Spike Growth","url":"/api/spells/spike-growth"},{"index":"spirit-guardians","name":"Spirit Guardians","url":"/api/spells/spirit-guardians"},{"index":"spiritual-weapon","name":"Spiritual Weapon","url":"/api/spells/spiritual-weapon"},{"index":"stinking-cloud","name":"Stinking Cloud","url":"/api/spells/stinking-cloud"},{"index":"stone-shape","name":"Stone Shape","url":"/api/spells/stone-shape"},{"index":"stoneskin","name":"Stoneskin","url":"/api/spells/stoneskin"},{"index":"storm-of-vengeance","name":"Storm of Vengeance","url":"/api/spells/storm-of-vengeance"},{"index":"suggestion","name":"Suggestion","url":"/api/spells/suggestion"},{"index":"sunbeam","name":"Sunbeam","url":"/api/spells/sunbeam"},{"index":"sunburst","name":"Sunburst","url":"/api/spells/sunburst"},{"index":"symbol","name":"Symbol","url":"/api/spells/symbol"},{"index":"telekinesis","name":"Telekinesis","url":"/api/spells/telekinesis"},{"index":"telepathic-bond","name":"Telepathic Bond","url":"/api/spells/telepathic-bond"},{"index":"teleport","name":"Teleport","url":"/api/spells/teleport"},{"index":"teleportation-circle","name":"Teleportation Circle","url":"/api/spells/teleportation-circle"},{"index":"thaumaturgy","name":"Thaumaturgy","url":"/api/spells/thaumaturgy"},{"index":"thunderwave","name":"Thunderwave","url":"/api/spells/thunderwave"},{"index":"time-stop","name":"Time Stop","url":"/api/spells/time-stop"},{"index":"tiny-hut","name":"Tiny Hut","url":"/api/spells/tiny-hut"},{"index":"tongues","name":"Tongues","url":"/api/spells/tongues"},{"index":"transport-via-plants","name":"Transport via Plants","url":"/api/spells/transport-via-plants"},{"index":"tree-stride","name":"Tree Stride","url":"/api/spells/tree-stride"},{"index":"true-polymorph","name":"True Polymorph","url":"/api/spells/true-polymorph"},{"index":"true-resurrection","name":"True Resurrection","url":"/api/spells/true-resurrection"},{"index":"true-seeing","name":"True Seeing","url":"/api/spells/true-seeing"},{"index":"true-strike","name":"True Strike","url":"/api/spells/true-strike"},{"index":"unseen-servant","name":"Unseen Servant","url":"/api/spells/unseen-servant"},{"index":"vampiric-touch","name":"Vampiric Touch","url":"/api/spells/vampiric-touch"},{"index":"vicious-mockery","name":"Vicious Mockery","url":"/api/spells/vicious-mockery"},{"index":"wall-of-fire","name":"Wall of Fire","url":"/api/spells/wall-of-fire"},{"index":"wall-of-force","name":"Wall of Force","url":"/api/spells/wall-of-force"},{"index":"wall-of-ice","name":"Wall of Ice","url":"/api/spells/wall-of-ice"},{"index":"wall-of-stone","name":"Wall of Stone","url":"/api/spells/wall-of-stone"},{"index":"wall-of-thorns","name":"Wall of Thorns","url":"/api/spells/wall-of-thorns"},{"index":"warding-bond","name":"Warding Bond","url":"/api/spells/warding-bond"},{"index":"water-breathing","name":"Water Breathing","url":"/api/spells/water-breathing"},{"index":"water-walk","name":"Water Walk","url":"/api/spells/water-walk"},{"index":"web","name":"Web","url":"/api/spells/web"},{"index":"weird","name":"Weird","url":"/api/spells/weird"},{"index":"wind-walk","name":"Wind Walk","url":"/api/spells/wind-walk"},{"index":"wind-wall","name":"Wind Wall","url":"/api/spells/wind-wall"},{"index":"wish","name":"Wish","url":"/api/spells/wish"},{"index":"word-of-recall","name":"Word of Recall","url":"/api/spells/word-of-recall"},{"index":"zone-of-truth","name":"Zone of Truth","url":"/api/spells/zone-of-truth"}]}

# print('these are the names of all of the spells')
animals = {"index":"animal-messenger",
           "name":"Animal Messenger",
           "desc":["By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as \"a man or woman dressed in the uniform of the town guard\" or \"a red-haired dwarf wearing a pointed hat.\" You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.","When the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell."],
           "higher_level":["If you cast this spell using a spell slot of 3nd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd."],
           "range":"30 feet",
           "components":["V","S","M"],
           "material":"A morsel of food.",
           "duration":"24 hours",
           "casting_time":"1 action",
           "level":2,
           "school":{"index":"enchantment",
                     "name":"Enchantment","url":
                     "/api/magic-schools/enchantment"},
           "classes":[{"index":"bard","name":"Bard","url":"/api/classes/bard"},{"index":"druid","name":"Druid","url":"/api/classes/druid"},{"index":"ranger","name":"Ranger","url":"/api/classes/ranger"}],
           "subclasses":[{"index":"lore","name":"Lore","url":"/api/subclasses/lore"}],
           "url":"/api/spells/animal-messenger"}

# print(animals.keys())
# keys = name, desc(description), higher_level, range, components, material, duration, casting_time, level, school, classes, subclasses, url


# print("name: ")
# print(animals["name"])
# # this is a string

# print("description: ")
# print(animals["desc"])
# # this is a list? in brackets

# print("higher level: ")
# print(animals["higher_level"])
# # again in brackets

# print("spell range: ")
# print(animals["range"])
# # this is a string

# print("components: ")
# print(animals["components"])
# # list in brackets

# print("material: ")
# print(animals["material"])
# # string

# print("duration: ")
# print(animals["duration"])
# # string

# print("casting time: ")
# print(animals["casting_time"])
# # string

# print("level: ")
# print(animals["level"])
# print(type(animals['level']))
# # integer


# print("school: ")
# print(animals["school"])
# # dictionary

# print("classes: ")
# print(animals["classes"])
# # list of dictionaries

# print("subclasses: ")
# print(animals["subclasses"])
# list of dictionaries


# for name in animals['school']:
#     print(name["name"])

# for result in spells['results']:
#     print(result['name'])

equipment = {"count":237,
             "results":[
    {"index":
     "abacus",
     "name":"Abacus",
     "url":"/api/equipment/abacus"},
     {"index":"acid-vial",
      "name":"Acid (vial)",
      "url":"/api/equipment/acid-vial"},
      {"index":"alchemists-fire-flask",
       "name":"Alchemist's fire (flask)",
       "url":"/api/equipment/alchemists-fire-flask"},
       {"index":"alchemists-supplies",
        "name":"Alchemist's Supplies",
        "url":"/api/equipment/alchemists-supplies"},
        {"index":"alms-box",
         "name":"Alms box",
         "url":"/api/equipment/alms-box"},
         {"index":"amulet",
          "name":"Amulet",
          "url":"/api/equipment/amulet"},
          {"index":"animal-feed-1-day",
           "name":"Animal Feed (1 day)",
           "url":"/api/equipment/animal-feed-1-day"},
           {"index":"antitoxin-vial",
            "name":"Antitoxin (vial)",
            "url":"/api/equipment/antitoxin-vial"},
            {"index":"arrow",
             "name":"Arrow",
             "url":"/api/equipment/arrow"},
             {"index":"backpack",
              "name":"Backpack",
              "url":"/api/equipment/backpack"},
              {"index":"bagpipes",
               "name":"Bagpipes",
               "url":"/api/equipment/bagpipes"},
               {"index":"ball-bearings-bag-of-1000",
                "name":"Ball bearings (bag of 1,000)","url":"/api/equipment/ball-bearings-bag-of-1000"},{"index":"barding-breastplate","name":"Barding: Breastplate","url":"/api/equipment/barding-breastplate"},{"index":"barding-chain-mail","name":"Barding: Chain mail","url":"/api/equipment/barding-chain-mail"},{"index":"barding-chain-shirt","name":"Barding: Chain shirt","url":"/api/equipment/barding-chain-shirt"},{"index":"barding-half-plate","name":"Barding: Half plate","url":"/api/equipment/barding-half-plate"},{"index":"barding-hide","name":"Barding: Hide","url":"/api/equipment/barding-hide"},{"index":"barding-leather","name":"Barding: Leather","url":"/api/equipment/barding-leather"},{"index":"barding-padded","name":"Barding: Padded","url":"/api/equipment/barding-padded"},{"index":"barding-plate","name":"Barding: Plate","url":"/api/equipment/barding-plate"},{"index":"barding-ring-mail","name":"Barding: Ring mail","url":"/api/equipment/barding-ring-mail"},{"index":"barding-scale-mail","name":"Barding: Scale mail","url":"/api/equipment/barding-scale-mail"},{"index":"barding-splint","name":"Barding: Splint","url":"/api/equipment/barding-splint"},{"index":"barding-studded-leather","name":"Barding: Studded Leather","url":"/api/equipment/barding-studded-leather"},{"index":"barrel","name":"Barrel","url":"/api/equipment/barrel"},{"index":"basket","name":"Basket","url":"/api/equipment/basket"},{"index":"battleaxe","name":"Battleaxe","url":"/api/equipment/battleaxe"},{"index":"bedroll","name":"Bedroll","url":"/api/equipment/bedroll"},{"index":"bell","name":"Bell","url":"/api/equipment/bell"},{"index":"bit-and-bridle","name":"Bit and bridle","url":"/api/equipment/bit-and-bridle"},{"index":"blanket","name":"Blanket","url":"/api/equipment/blanket"},{"index":"block-and-tackle","name":"Block and tackle","url":"/api/equipment/block-and-tackle"},{"index":"block-of-incense","name":"Block of incense","url":"/api/equipment/block-of-incense"},{"index":"blowgun","name":"Blowgun","url":"/api/equipment/blowgun"},{"index":"blowgun-needle","name":"Blowgun needle","url":"/api/equipment/blowgun-needle"},{"index":"book","name":"Book","url":"/api/equipment/book"},{"index":"bottle-glass","name":"Bottle, glass","url":"/api/equipment/bottle-glass"},{"index":"breastplate","name":"Breastplate","url":"/api/equipment/breastplate"},{"index":"brewers-supplies","name":"Brewer's Supplies","url":"/api/equipment/brewers-supplies"},{"index":"bucket","name":"Bucket","url":"/api/equipment/bucket"},{"index":"burglars-pack","name":"Burglar's Pack","url":"/api/equipment/burglars-pack"},{"index":"calligraphers-supplies","name":"Calligrapher's Supplies","url":"/api/equipment/calligraphers-supplies"},{"index":"caltrops","name":"Caltrops","url":"/api/equipment/caltrops"},{"index":"camel","name":"Camel","url":"/api/equipment/camel"},{"index":"candle","name":"Candle","url":"/api/equipment/candle"},{"index":"carpenters-tools","name":"Carpenter's Tools","url":"/api/equipment/carpenters-tools"},{"index":"carriage","name":"Carriage","url":"/api/equipment/carriage"},{"index":"cart","name":"Cart","url":"/api/equipment/cart"},{"index":"cartographers-tools","name":"Cartographer's Tools","url":"/api/equipment/cartographers-tools"},{"index":"case-crossbow-bolt","name":"Case, crossbow bolt","url":"/api/equipment/case-crossbow-bolt"},{"index":"case-map-or-scroll","name":"Case, map or scroll","url":"/api/equipment/case-map-or-scroll"},{"index":"censer","name":"Censer","url":"/api/equipment/censer"},{"index":"chain-10-feet","name":"Chain (10 feet)","url":"/api/equipment/chain-10-feet"},{"index":"chain-mail","name":"Chain Mail","url":"/api/equipment/chain-mail"},{"index":"chain-shirt","name":"Chain Shirt","url":"/api/equipment/chain-shirt"},{"index":"chalk-1-piece","name":"Chalk (1 piece)","url":"/api/equipment/chalk-1-piece"},{"index":"chariot","name":"Chariot","url":"/api/equipment/chariot"},{"index":"chest","name":"Chest","url":"/api/equipment/chest"},{"index":"climbers-kit","name":"Climber's Kit","url":"/api/equipment/climbers-kit"},{"index":"clothes-common","name":"Clothes, common","url":"/api/equipment/clothes-common"},{"index":"clothes-costume","name":"Clothes, costume","url":"/api/equipment/clothes-costume"},{"index":"clothes-fine","name":"Clothes, fine","url":"/api/equipment/clothes-fine"},{"index":"clothes-travelers","name":"Clothes, traveler's","url":"/api/equipment/clothes-travelers"},{"index":"club","name":"Club","url":"/api/equipment/club"},{"index":"cobblers-tools","name":"Cobbler's Tools","url":"/api/equipment/cobblers-tools"},{"index":"component-pouch","name":"Component pouch","url":"/api/equipment/component-pouch"},{"index":"cooks-utensils","name":"Cook's utensils","url":"/api/equipment/cooks-utensils"},{"index":"crossbow-bolt","name":"Crossbow bolt","url":"/api/equipment/crossbow-bolt"},{"index":"crossbow-hand","name":"Crossbow, hand","url":"/api/equipment/crossbow-hand"},{"index":"crossbow-heavy","name":"Crossbow, heavy","url":"/api/equipment/crossbow-heavy"},{"index":"crossbow-light","name":"Crossbow, light","url":"/api/equipment/crossbow-light"},{"index":"crowbar","name":"Crowbar","url":"/api/equipment/crowbar"},{"index":"crystal","name":"Crystal","url":"/api/equipment/crystal"},{"index":"dagger","name":"Dagger","url":"/api/equipment/dagger"},{"index":"dart","name":"Dart","url":"/api/equipment/dart"},{"index":"dice-set","name":"Dice Set","url":"/api/equipment/dice-set"},{"index":"diplomats-pack","name":"Diplomat's Pack","url":"/api/equipment/diplomats-pack"},{"index":"disguise-kit","name":"Disguise Kit","url":"/api/equipment/disguise-kit"},{"index":"donkey","name":"Donkey","url":"/api/equipment/donkey"},{"index":"drum","name":"Drum","url":"/api/equipment/drum"},{"index":"dulcimer","name":"Dulcimer","url":"/api/equipment/dulcimer"},{"index":"dungeoneers-pack","name":"Dungeoneer's Pack","url":"/api/equipment/dungeoneers-pack"},{"index":"elephant","name":"Elephant","url":"/api/equipment/elephant"},{"index":"emblem","name":"Emblem","url":"/api/equipment/emblem"},{"index":"entertainers-pack","name":"Entertainer's Pack","url":"/api/equipment/entertainers-pack"},{"index":"explorers-pack","name":"Explorer's Pack","url":"/api/equipment/explorers-pack"},{"index":"fishing-tackle","name":"Fishing tackle","url":"/api/equipment/fishing-tackle"},{"index":"flail","name":"Flail","url":"/api/equipment/flail"},{"index":"flask-or-tankard","name":"Flask or tankard","url":"/api/equipment/flask-or-tankard"},{"index":"flute","name":"Flute","url":"/api/equipment/flute"},{"index":"forgery-kit","name":"Forgery Kit","url":"/api/equipment/forgery-kit"},{"index":"galley","name":"Galley","url":"/api/equipment/galley"},{"index":"glaive","name":"Glaive","url":"/api/equipment/glaive"},{"index":"glassblowers-tools","name":"Glassblower's Tools","url":"/api/equipment/glassblowers-tools"},{"index":"grappling-hook","name":"Grappling hook","url":"/api/equipment/grappling-hook"},{"index":"greataxe","name":"Greataxe","url":"/api/equipment/greataxe"},{"index":"greatclub","name":"Greatclub","url":"/api/equipment/greatclub"},{"index":"greatsword","name":"Greatsword","url":"/api/equipment/greatsword"},{"index":"halberd","name":"Halberd","url":"/api/equipment/halberd"},{"index":"half-plate-armor","name":"Half Plate Armor","url":"/api/equipment/half-plate-armor"},{"index":"hammer","name":"Hammer","url":"/api/equipment/hammer"},{"index":"hammer-sledge","name":"Hammer, sledge","url":"/api/equipment/hammer-sledge"},{"index":"handaxe","name":"Handaxe","url":"/api/equipment/handaxe"},{"index":"healers-kit","name":"Healer's Kit","url":"/api/equipment/healers-kit"},{"index":"herbalism-kit","name":"Herbalism Kit","url":"/api/equipment/herbalism-kit"},{"index":"hide-armor","name":"Hide Armor","url":"/api/equipment/hide-armor"},{"index":"holy-water-flask","name":"Holy water (flask)","url":"/api/equipment/holy-water-flask"},{"index":"horn","name":"Horn","url":"/api/equipment/horn"},{"index":"horse-draft","name":"Horse, draft","url":"/api/equipment/horse-draft"},{"index":"horse-riding","name":"Horse, riding","url":"/api/equipment/horse-riding"},{"index":"hourglass","name":"Hourglass","url":"/api/equipment/hourglass"},{"index":"hunting-trap","name":"Hunting trap","url":"/api/equipment/hunting-trap"},{"index":"ink-1-ounce-bottle","name":"Ink (1 ounce bottle)","url":"/api/equipment/ink-1-ounce-bottle"},{"index":"ink-pen","name":"Ink pen","url":"/api/equipment/ink-pen"},{"index":"javelin","name":"Javelin","url":"/api/equipment/javelin"},{"index":"jewelers-tools","name":"Jeweler's Tools","url":"/api/equipment/jewelers-tools"},{"index":"jug-or-pitcher","name":"Jug or pitcher","url":"/api/equipment/jug-or-pitcher"},{"index":"keelboat","name":"Keelboat","url":"/api/equipment/keelboat"},{"index":"ladder-10-foot","name":"Ladder (10-foot)","url":"/api/equipment/ladder-10-foot"},{"index":"lamp","name":"Lamp","url":"/api/equipment/lamp"},{"index":"lance","name":"Lance","url":"/api/equipment/lance"},{"index":"lantern-bullseye","name":"Lantern, bullseye","url":"/api/equipment/lantern-bullseye"},{"index":"lantern-hooded","name":"Lantern, hooded","url":"/api/equipment/lantern-hooded"},{"index":"leather-armor","name":"Leather Armor","url":"/api/equipment/leather-armor"},{"index":"leatherworkers-tools","name":"Leatherworker's Tools","url":"/api/equipment/leatherworkers-tools"},{"index":"light-hammer","name":"Light hammer","url":"/api/equipment/light-hammer"},{"index":"little-bag-of-sand","name":"Little bag of sand","url":"/api/equipment/little-bag-of-sand"},{"index":"lock","name":"Lock","url":"/api/equipment/lock"},{"index":"longbow","name":"Longbow","url":"/api/equipment/longbow"},{"index":"longship","name":"Longship","url":"/api/equipment/longship"},{"index":"longsword","name":"Longsword","url":"/api/equipment/longsword"},{"index":"lute","name":"Lute","url":"/api/equipment/lute"},{"index":"lyre","name":"Lyre","url":"/api/equipment/lyre"},{"index":"mace","name":"Mace","url":"/api/equipment/mace"},{"index":"magnifying-glass","name":"Magnifying glass","url":"/api/equipment/magnifying-glass"},{"index":"manacles","name":"Manacles","url":"/api/equipment/manacles"},{"index":"masons-tools","name":"Mason's Tools","url":"/api/equipment/masons-tools"},{"index":"mastiff","name":"Mastiff","url":"/api/equipment/mastiff"},{"index":"maul","name":"Maul","url":"/api/equipment/maul"},{"index":"mess-kit","name":"Mess Kit","url":"/api/equipment/mess-kit"},{"index":"mirror-steel","name":"Mirror, steel","url":"/api/equipment/mirror-steel"},{"index":"morningstar","name":"Morningstar","url":"/api/equipment/morningstar"},{"index":"mule","name":"Mule","url":"/api/equipment/mule"},{"index":"navigators-tools","name":"Navigator's Tools","url":"/api/equipment/navigators-tools"},{"index":"net","name":"Net","url":"/api/equipment/net"},{"index":"oil-flask","name":"Oil (flask)","url":"/api/equipment/oil-flask"},{"index":"orb","name":"Orb","url":"/api/equipment/orb"},{"index":"padded-armor","name":"Padded Armor","url":"/api/equipment/padded-armor"},{"index":"painters-supplies","name":"Painter's Supplies","url":"/api/equipment/painters-supplies"},{"index":"pan-flute","name":"Pan flute","url":"/api/equipment/pan-flute"},{"index":"paper-one-sheet","name":"Paper (one sheet)","url":"/api/equipment/paper-one-sheet"},{"index":"parchment-one-sheet","name":"Parchment (one sheet)","url":"/api/equipment/parchment-one-sheet"},{"index":"perfume-vial","name":"Perfume (vial)","url":"/api/equipment/perfume-vial"},{"index":"pick-miners","name":"Pick, miner's","url":"/api/equipment/pick-miners"},{"index":"pike","name":"Pike","url":"/api/equipment/pike"},{"index":"piton","name":"Piton","url":"/api/equipment/piton"},{"index":"plate-armor","name":"Plate Armor","url":"/api/equipment/plate-armor"},{"index":"playing-card-set","name":"Playing Card Set","url":"/api/equipment/playing-card-set"},{"index":"poison-basic-vial","name":"Poison, basic (vial)","url":"/api/equipment/poison-basic-vial"},{"index":"poisoners-kit","name":"Poisoner's Kit","url":"/api/equipment/poisoners-kit"},{"index":"pole-10-foot","name":"Pole (10-foot)","url":"/api/equipment/pole-10-foot"},{"index":"pony","name":"Pony","url":"/api/equipment/pony"},{"index":"pot-iron","name":"Pot, iron","url":"/api/equipment/pot-iron"},{"index":"potters-tools","name":"Potter's Tools","url":"/api/equipment/potters-tools"},{"index":"pouch","name":"Pouch","url":"/api/equipment/pouch"},{"index":"priests-pack","name":"Priest's Pack","url":"/api/equipment/priests-pack"},{"index":"quarterstaff","name":"Quarterstaff","url":"/api/equipment/quarterstaff"},{"index":"quiver","name":"Quiver","url":"/api/equipment/quiver"},{"index":"ram-portable","name":"Ram, portable","url":"/api/equipment/ram-portable"},{"index":"rapier","name":"Rapier","url":"/api/equipment/rapier"},{"index":"rations-1-day","name":"Rations (1 day)","url":"/api/equipment/rations-1-day"},{"index":"reliquary","name":"Reliquary","url":"/api/equipment/reliquary"},{"index":"ring-mail","name":"Ring Mail","url":"/api/equipment/ring-mail"},{"index":"robes","name":"Robes","url":"/api/equipment/robes"},{"index":"rod","name":"Rod","url":"/api/equipment/rod"},{"index":"rope-hempen-50-feet","name":"Rope, hempen (50 feet)","url":"/api/equipment/rope-hempen-50-feet"},{"index":"rope-silk-50-feet","name":"Rope, silk (50 feet)","url":"/api/equipment/rope-silk-50-feet"},{"index":"rowboat","name":"Rowboat","url":"/api/equipment/rowboat"},{"index":"sack","name":"Sack","url":"/api/equipment/sack"},{"index":"saddle-exotic","name":"Saddle, Exotic","url":"/api/equipment/saddle-exotic"},{"index":"saddle-military","name":"Saddle, Military","url":"/api/equipment/saddle-military"},{"index":"saddle-pack","name":"Saddle, Pack","url":"/api/equipment/saddle-pack"},{"index":"saddle-riding","name":"Saddle, Riding","url":"/api/equipment/saddle-riding"},{"index":"saddlebags","name":"Saddlebags","url":"/api/equipment/saddlebags"},{"index":"sailing-ship","name":"Sailing ship","url":"/api/equipment/sailing-ship"},{"index":"scale-mail","name":"Scale Mail","url":"/api/equipment/scale-mail"},{"index":"scale-merchants","name":"Scale, merchant's","url":"/api/equipment/scale-merchants"},{"index":"scholars-pack","name":"Scholar's Pack","url":"/api/equipment/scholars-pack"},{"index":"scimitar","name":"Scimitar","url":"/api/equipment/scimitar"},{"index":"sealing-wax","name":"Sealing wax","url":"/api/equipment/sealing-wax"},{"index":"shawm","name":"Shawm","url":"/api/equipment/shawm"},{"index":"shield","name":"Shield","url":"/api/equipment/shield"},{"index":"shortbow","name":"Shortbow","url":"/api/equipment/shortbow"},{"index":"shortsword","name":"Shortsword","url":"/api/equipment/shortsword"},{"index":"shovel","name":"Shovel","url":"/api/equipment/shovel"},{"index":"sickle","name":"Sickle","url":"/api/equipment/sickle"},{"index":"signal-whistle","name":"Signal whistle","url":"/api/equipment/signal-whistle"},{"index":"signet-ring","name":"Signet ring","url":"/api/equipment/signet-ring"},{"index":"sled","name":"Sled","url":"/api/equipment/sled"},{"index":"sling","name":"Sling","url":"/api/equipment/sling"},{"index":"sling-bullet","name":"Sling bullet","url":"/api/equipment/sling-bullet"},{"index":"small-knife","name":"Small knife","url":"/api/equipment/small-knife"},{"index":"smiths-tools","name":"Smith's Tools","url":"/api/equipment/smiths-tools"},{"index":"soap","name":"Soap","url":"/api/equipment/soap"},{"index":"spear","name":"Spear","url":"/api/equipment/spear"},{"index":"spellbook","name":"Spellbook","url":"/api/equipment/spellbook"},{"index":"spike-iron","name":"Spike, iron","url":"/api/equipment/spike-iron"},{"index":"splint-armor","name":"Splint Armor","url":"/api/equipment/splint-armor"},{"index":"sprig-of-mistletoe","name":"Sprig of mistletoe","url":"/api/equipment/sprig-of-mistletoe"},{"index":"spyglass","name":"Spyglass","url":"/api/equipment/spyglass"},{"index":"stabling-1-day","name":"Stabling (1 day)","url":"/api/equipment/stabling-1-day"},{"index":"staff","name":"Staff","url":"/api/equipment/staff"},{"index":"string-10-feet","name":"String (10 feet)","url":"/api/equipment/string-10-feet"},{"index":"studded-leather-armor","name":"Studded Leather Armor","url":"/api/equipment/studded-leather-armor"},{"index":"tent-two-person","name":"Tent, two-person","url":"/api/equipment/tent-two-person"},{"index":"thieves-tools","name":"Thieves' Tools","url":"/api/equipment/thieves-tools"},{"index":"tinderbox","name":"Tinderbox","url":"/api/equipment/tinderbox"},{"index":"tinkers-tools","name":"Tinker's Tools","url":"/api/equipment/tinkers-tools"},{"index":"torch","name":"Torch","url":"/api/equipment/torch"},{"index":"totem","name":"Totem","url":"/api/equipment/totem"},{"index":"trident","name":"Trident","url":"/api/equipment/trident"},{"index":"vestments","name":"Vestments","url":"/api/equipment/vestments"},{"index":"vial","name":"Vial","url":"/api/equipment/vial"},{"index":"viol","name":"Viol","url":"/api/equipment/viol"},{"index":"wagon","name":"Wagon","url":"/api/equipment/wagon"},{"index":"wand","name":"Wand","url":"/api/equipment/wand"},{"index":"war-pick","name":"War pick","url":"/api/equipment/war-pick"},{"index":"warhammer","name":"Warhammer","url":"/api/equipment/warhammer"},{"index":"warhorse","name":"Warhorse","url":"/api/equipment/warhorse"},{"index":"warship","name":"Warship","url":"/api/equipment/warship"},{"index":"waterskin","name":"Waterskin","url":"/api/equipment/waterskin"},{"index":"weavers-tools","name":"Weaver's Tools","url":"/api/equipment/weavers-tools"},{"index":"whetstone","name":"Whetstone","url":"/api/equipment/whetstone"},{"index":"whip","name":"Whip","url":"/api/equipment/whip"},{"index":"woodcarvers-tools","name":"Woodcarver's Tools","url":"/api/equipment/woodcarvers-tools"},{"index":"wooden-staff","name":"Wooden staff","url":"/api/equipment/wooden-staff"},{"index":"yew-wand","name":"Yew wand","url":"/api/equipment/yew-wand"}]}

# equipment = {"count":237,
#              "results":[
#     {"index":
#      "abacus",
#      "name":"Abacus",
#      "url":"/api/equipment/abacus"},
#      {"index":"acid-vial",
#       "name":"Acid (vial)",
#       "url":"/api/equipment/acid-vial"},
#       {"index":"alchemists-fire-flask",
#        "name":"Alchemist's fire (flask)",
#        "url":"/api/equipment/alchemists-fire-flask"},
#        {"index":"alchemists-supplies",
#         "name":"Alchemist's Supplies",
#         "url":"/api/equipment/alchemists-supplies"},
#         {"index":"alms-box",
#          "name":"Alms box",
#          "url":"/api/equipment/alms-box"},
#          {"index":"amulet",
#           "name":"Amulet",
#           "url":"/api/equipment/amulet"},
#           {"index":"animal-feed-1-day",
#            "name":"Animal Feed (1 day)",
#            "url":"/api/equipment/animal-feed-1-day"},
#            {"index":"antitoxin-vial",
#             "name":"Antitoxin (vial)",
#             "url":"/api/equipment/antitoxin-vial"},

# print(equipment.keys())
# print(equipment['results'])

for result in equipment['results']:
    print (result["name"])
# for result in equipment['results']:
#     print (result['url'])



longsword = {"desc":[],
             "special":[],
             "index":"longsword",
             "name":"Longsword",
             "equipment_category":
             {"index":"weapon","name":"Weapon","url":"/api/equipment-categories/weapon"},
             "weapon_category":"Martial","weapon_range":"Melee","category_range":"Martial Melee",
             "cost":{"quantity":15,"unit":"gp"},
             "damage": {"damage_dice":"1d8",
              "damage_type":
              {"index":"slashing",
               "name":"Slashing",
               "url":"/api/damage-types/slashing"}},
             "range":{"normal":5},
             "weight":3,
             "properties":
             [{"index":"versatile","name":"Versatile","url":"/api/weapon-properties/versatile"}],
             "two_handed_damage":{"damage_dice":"1d10","damage_type":{"index":"slashing","name":"Slashing","url":"/api/damage-types/slashing"}},
             "url":"/api/equipment/longsword","contents":[]}

# print('longsword keys')
# print(longsword.keys())

# desc, special, index, name, equipment category, weapon category, weapon range,
# category range, cost, damage, range, weight, properties, two handed damage, 
# url, contents

# things in my table:
# name - yes - str
# type - yes - str
# durability - no?
# range - yes - int
# attack save - no?
# cost - yes - int
# weight - yes - int
# properties - yes - str

print("longsword name:") 
print(longsword['name'])
# # string

print("longsword damage: ")
print(longsword['damage'])
# # dict

for damage in longsword['damage']:
    print("this is for loop damage")
    print(damage)

def get_damage_type_name(damage):
    return damage["damage"]["damage_type"]["name"]
print("get damage type name: ")
print(get_damage_type_name(longsword))
# # slashing

print("this is the damage type type: ")
print (type(longsword["damage"]["damage_type"]["name"]))
# slashing again, both work

print("this is the longsword range and range type: ")
print(longsword['range']['normal'])
print (type(longsword['range']['normal']))
# 5 - integer

print("this is longsword category range: ")
print(longsword['category_range']) 
# - dont need currently

print("this is longsword cost amount and type: ")
print(longsword['cost']['quantity'])
# # amount of gp
print(type(longsword['cost']['quantity']))
# # int

print("this is longsword unit of cost and type: ")
print(longsword['cost']['unit'])
# # gp
print(type(longsword['cost']['unit']))
# # str

print("this is longsword weight and type: ")
print(longsword['weight'])
print(type(longsword['weight']))
# 3 - int

print("this is longsword propertires: ")
for prop in longsword["properties"]:
    print(prop["name"])
    print(type(prop['name']))
# versatile - str