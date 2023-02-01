# barbarian = {"index":"barbarian","name":"Barbarian","hit_die":12,"proficiency_choices":[{"desc":"Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival","choose":2,"type":"proficiencies","from":{"option_set_type":"options_array","options":[{"option_type":"reference","item":{"index":"skill-animal-handling","name":"Skill: Animal Handling","url":"/api/proficiencies/skill-animal-handling"}},{"option_type":"reference","item":{"index":"skill-athletics","name":"Skill: Athletics","url":"/api/proficiencies/skill-athletics"}},{"option_type":"reference","item":{"index":"skill-intimidation","name":"Skill: Intimidation","url":"/api/proficiencies/skill-intimidation"}},{"option_type":"reference","item":{"index":"skill-nature","name":"Skill: Nature","url":"/api/proficiencies/skill-nature"}},{"option_type":"reference","item":{"index":"skill-perception","name":"Skill: Perception","url":"/api/proficiencies/skill-perception"}},{"option_type":"reference","item":{"index":"skill-survival","name":"Skill: Survival","url":"/api/proficiencies/skill-survival"}}]}}],"proficiencies":[{"index":"light-armor","name":"Light Armor","url":"/api/proficiencies/light-armor"},{"index":"medium-armor","name":"Medium Armor","url":"/api/proficiencies/medium-armor"},{"index":"shields","name":"Shields","url":"/api/proficiencies/shields"},{"index":"simple-weapons","name":"Simple Weapons","url":"/api/proficiencies/simple-weapons"},{"index":"martial-weapons","name":"Martial Weapons","url":"/api/proficiencies/martial-weapons"},{"index":"saving-throw-str","name":"Saving Throw: STR","url":"/api/proficiencies/saving-throw-str"},{"index":"saving-throw-con","name":"Saving Throw: CON","url":"/api/proficiencies/saving-throw-con"}],"saving_throws":[{"index":"str","name":"STR","url":"/api/ability-scores/str"},{"index":"con","name":"CON","url":"/api/ability-scores/con"}],"starting_equipment":[{"equipment":{"index":"explorers-pack","name":"Explorer's Pack","url":"/api/equipment/explorers-pack"},"quantity":1},{"equipment":{"index":"javelin","name":"Javelin","url":"/api/equipment/javelin"},"quantity":4}],"starting_equipment_options":[{"desc":"(a) a greataxe or (b) any martial melee weapon","choose":1,"type":"equipment","from":{"option_set_type":"options_array","options":[{"option_type":"counted_reference","count":1,"of":{"index":"greataxe","name":"Greataxe","url":"/api/equipment/greataxe"}},{"option_type":"choice","choice":{"desc":"any martial melee weapon","choose":1,"type":"equipment","from":{"option_set_type":"equipment_category","equipment_category":{"index":"martial-melee-weapons","name":"Martial Melee Weapons","url":"/api/equipment-categories/martial-melee-weapons"}}}}]}},{"desc":"(a) two handaxes or (b) any simple weapon","choose":1,"type":"equipment","from":{"option_set_type":"options_array","options":[{"option_type":"counted_reference","count":2,"of":{"index":"handaxe","name":"Handaxe","url":"/api/equipment/handaxe"}},{"option_type":"choice","choice":{"desc":"any simple weapon","choose":1,"type":"equipment","from":{"option_set_type":"equipment_category","equipment_category":{"index":"simple-weapons","name":"Simple Weapons","url":"/api/equipment-categories/simple-weapons"}}}}]}}],"class_levels":"/api/classes/barbarian/levels","multi_classing":{"prerequisites":[{"ability_score":{"index":"str","name":"STR","url":"/api/ability-scores/str"},"minimum_score":13}],"proficiencies":[{"index":"shields","name":"Shields","url":"/api/proficiencies/shields"},{"index":"simple-weapons","name":"Simple Weapons","url":"/api/proficiencies/simple-weapons"},{"index":"martial-weapons","name":"Martial Weapons","url":"/api/proficiencies/martial-weapons"}]},"subclasses":[{"index":"berserker","name":"Berserker","url":"/api/subclasses/berserker"}],"url":"/api/classes/barbarian"}
# races = {"count":9,"results":[{"index":"dragonborn","name":"Dragonborn","url":"/api/races/dragonborn"},{"index":"dwarf","name":"Dwarf","url":"/api/races/dwarf"},{"index":"elf","name":"Elf","url":"/api/races/elf"},{"index":"gnome","name":"Gnome","url":"/api/races/gnome"},{"index":"half-elf","name":"Half-Elf","url":"/api/races/half-elf"},{"index":"half-orc","name":"Half-Orc","url":"/api/races/half-orc"},{"index":"halfling","name":"Halfling","url":"/api/races/halfling"},{"index":"human","name":"Human","url":"/api/races/human"},{"index":"tiefling","name":"Tiefling","url":"/api/races/tiefling"}]}
elf = {"index":"elf","name":"Elf","speed":30,"ability_bonuses":[{"ability_score":{"index":"dex","name":"DEX","url":"/api/ability-scores/dex"},"bonus":2}],"age":"Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.","alignment":"Elves love freedom, variety, and self-expression, so they lean strongly toward the gentler aspects of chaos. They value and protect others' freedom as well as their own, and they are more often good than not. The drow are an exception; their exile has made them vicious and dangerous. Drow are more often evil than not.","size":"Medium","size_description":"Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.","starting_proficiencies":[{"index":"skill-perception","name":"Skill: Perception","url":"/api/proficiencies/skill-perception"}],"languages":[{"index":"common","name":"Common","url":"/api/languages/common"},{"index":"elvish","name":"Elvish","url":"/api/languages/elvish"}],"language_desc":"You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among other races. Many bards learn their language so they can add Elvish ballads to their repertoires.","traits":[{"index":"darkvision","name":"Darkvision","url":"/api/traits/darkvision"},{"index":"fey-ancestry","name":"Fey Ancestry","url":"/api/traits/fey-ancestry"},{"index":"trance","name":"Trance","url":"/api/traits/trance"},{"index":"keen-senses","name":"Keen Senses","url":"/api/traits/keen-senses"}],"subraces":[{"index":"high-elf","name":"High Elf","url":"/api/subraces/high-elf"}],"url":"/api/races/elf"}


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


