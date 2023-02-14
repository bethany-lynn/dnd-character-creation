from flask import Flask, request
import requests


equipment = {"count":237,"results":[{"index":"abacus","name":"Abacus","url":"/api/equipment/abacus"},{"index":"acid-vial","name":"Acid (vial)","url":"/api/equipment/acid-vial"},{"index":"alchemists-fire-flask","name":"Alchemist's fire (flask)","url":"/api/equipment/alchemists-fire-flask"},{"index":"alchemists-supplies","name":"Alchemist's Supplies","url":"/api/equipment/alchemists-supplies"},{"index":"alms-box","name":"Alms box","url":"/api/equipment/alms-box"},{"index":"amulet","name":"Amulet","url":"/api/equipment/amulet"},{"index":"animal-feed-1-day","name":"Animal Feed (1 day)","url":"/api/equipment/animal-feed-1-day"},{"index":"antitoxin-vial","name":"Antitoxin (vial)","url":"/api/equipment/antitoxin-vial"},{"index":"arrow","name":"Arrow","url":"/api/equipment/arrow"},{"index":"backpack","name":"Backpack","url":"/api/equipment/backpack"},{"index":"bagpipes","name":"Bagpipes","url":"/api/equipment/bagpipes"},{"index":"ball-bearings-bag-of-1000","name":"Ball bearings (bag of 1,000)","url":"/api/equipment/ball-bearings-bag-of-1000"},{"index":"barding-breastplate","name":"Barding: Breastplate","url":"/api/equipment/barding-breastplate"},{"index":"barding-chain-mail","name":"Barding: Chain mail","url":"/api/equipment/barding-chain-mail"},{"index":"barding-chain-shirt","name":"Barding: Chain shirt","url":"/api/equipment/barding-chain-shirt"},{"index":"barding-half-plate","name":"Barding: Half plate","url":"/api/equipment/barding-half-plate"},{"index":"barding-hide","name":"Barding: Hide","url":"/api/equipment/barding-hide"},{"index":"barding-leather","name":"Barding: Leather","url":"/api/equipment/barding-leather"},{"index":"barding-padded","name":"Barding: Padded","url":"/api/equipment/barding-padded"},{"index":"barding-plate","name":"Barding: Plate","url":"/api/equipment/barding-plate"},{"index":"barding-ring-mail","name":"Barding: Ring mail","url":"/api/equipment/barding-ring-mail"},{"index":"barding-scale-mail","name":"Barding: Scale mail","url":"/api/equipment/barding-scale-mail"},{"index":"barding-splint","name":"Barding: Splint","url":"/api/equipment/barding-splint"},{"index":"barding-studded-leather","name":"Barding: Studded Leather","url":"/api/equipment/barding-studded-leather"},{"index":"barrel","name":"Barrel","url":"/api/equipment/barrel"},{"index":"basket","name":"Basket","url":"/api/equipment/basket"},{"index":"battleaxe","name":"Battleaxe","url":"/api/equipment/battleaxe"},{"index":"bedroll","name":"Bedroll","url":"/api/equipment/bedroll"},{"index":"bell","name":"Bell","url":"/api/equipment/bell"},{"index":"bit-and-bridle","name":"Bit and bridle","url":"/api/equipment/bit-and-bridle"},{"index":"blanket","name":"Blanket","url":"/api/equipment/blanket"},{"index":"block-and-tackle","name":"Block and tackle","url":"/api/equipment/block-and-tackle"},{"index":"block-of-incense","name":"Block of incense","url":"/api/equipment/block-of-incense"},{"index":"blowgun","name":"Blowgun","url":"/api/equipment/blowgun"},{"index":"blowgun-needle","name":"Blowgun needle","url":"/api/equipment/blowgun-needle"},{"index":"book","name":"Book","url":"/api/equipment/book"},{"index":"bottle-glass","name":"Bottle, glass","url":"/api/equipment/bottle-glass"},{"index":"breastplate","name":"Breastplate","url":"/api/equipment/breastplate"},{"index":"brewers-supplies","name":"Brewer's Supplies","url":"/api/equipment/brewers-supplies"},{"index":"bucket","name":"Bucket","url":"/api/equipment/bucket"},{"index":"burglars-pack","name":"Burglar's Pack","url":"/api/equipment/burglars-pack"},{"index":"calligraphers-supplies","name":"Calligrapher's Supplies","url":"/api/equipment/calligraphers-supplies"},{"index":"caltrops","name":"Caltrops","url":"/api/equipment/caltrops"},{"index":"camel","name":"Camel","url":"/api/equipment/camel"},{"index":"candle","name":"Candle","url":"/api/equipment/candle"},{"index":"carpenters-tools","name":"Carpenter's Tools","url":"/api/equipment/carpenters-tools"},{"index":"carriage","name":"Carriage","url":"/api/equipment/carriage"},{"index":"cart","name":"Cart","url":"/api/equipment/cart"},{"index":"cartographers-tools","name":"Cartographer's Tools","url":"/api/equipment/cartographers-tools"},{"index":"case-crossbow-bolt","name":"Case, crossbow bolt","url":"/api/equipment/case-crossbow-bolt"},{"index":"case-map-or-scroll","name":"Case, map or scroll","url":"/api/equipment/case-map-or-scroll"},{"index":"censer","name":"Censer","url":"/api/equipment/censer"},{"index":"chain-10-feet","name":"Chain (10 feet)","url":"/api/equipment/chain-10-feet"},{"index":"chain-mail","name":"Chain Mail","url":"/api/equipment/chain-mail"},{"index":"chain-shirt","name":"Chain Shirt","url":"/api/equipment/chain-shirt"},{"index":"chalk-1-piece","name":"Chalk (1 piece)","url":"/api/equipment/chalk-1-piece"},{"index":"chariot","name":"Chariot","url":"/api/equipment/chariot"},{"index":"chest","name":"Chest","url":"/api/equipment/chest"},{"index":"climbers-kit","name":"Climber's Kit","url":"/api/equipment/climbers-kit"},{"index":"clothes-common","name":"Clothes, common","url":"/api/equipment/clothes-common"},{"index":"clothes-costume","name":"Clothes, costume","url":"/api/equipment/clothes-costume"},{"index":"clothes-fine","name":"Clothes, fine","url":"/api/equipment/clothes-fine"},{"index":"clothes-travelers","name":"Clothes, traveler's","url":"/api/equipment/clothes-travelers"},{"index":"club","name":"Club","url":"/api/equipment/club"},{"index":"cobblers-tools","name":"Cobbler's Tools","url":"/api/equipment/cobblers-tools"},{"index":"component-pouch","name":"Component pouch","url":"/api/equipment/component-pouch"},{"index":"cooks-utensils","name":"Cook's utensils","url":"/api/equipment/cooks-utensils"},{"index":"crossbow-bolt","name":"Crossbow bolt","url":"/api/equipment/crossbow-bolt"},{"index":"crossbow-hand","name":"Crossbow, hand","url":"/api/equipment/crossbow-hand"},{"index":"crossbow-heavy","name":"Crossbow, heavy","url":"/api/equipment/crossbow-heavy"},{"index":"crossbow-light","name":"Crossbow, light","url":"/api/equipment/crossbow-light"},{"index":"crowbar","name":"Crowbar","url":"/api/equipment/crowbar"},{"index":"crystal","name":"Crystal","url":"/api/equipment/crystal"},{"index":"dagger","name":"Dagger","url":"/api/equipment/dagger"},{"index":"dart","name":"Dart","url":"/api/equipment/dart"},{"index":"dice-set","name":"Dice Set","url":"/api/equipment/dice-set"},{"index":"diplomats-pack","name":"Diplomat's Pack","url":"/api/equipment/diplomats-pack"},{"index":"disguise-kit","name":"Disguise Kit","url":"/api/equipment/disguise-kit"},{"index":"donkey","name":"Donkey","url":"/api/equipment/donkey"},{"index":"drum","name":"Drum","url":"/api/equipment/drum"},{"index":"dulcimer","name":"Dulcimer","url":"/api/equipment/dulcimer"},{"index":"dungeoneers-pack","name":"Dungeoneer's Pack","url":"/api/equipment/dungeoneers-pack"},{"index":"elephant","name":"Elephant","url":"/api/equipment/elephant"},{"index":"emblem","name":"Emblem","url":"/api/equipment/emblem"},{"index":"entertainers-pack","name":"Entertainer's Pack","url":"/api/equipment/entertainers-pack"},{"index":"explorers-pack","name":"Explorer's Pack","url":"/api/equipment/explorers-pack"},{"index":"fishing-tackle","name":"Fishing tackle","url":"/api/equipment/fishing-tackle"},{"index":"flail","name":"Flail","url":"/api/equipment/flail"},{"index":"flask-or-tankard","name":"Flask or tankard","url":"/api/equipment/flask-or-tankard"},{"index":"flute","name":"Flute","url":"/api/equipment/flute"},{"index":"forgery-kit","name":"Forgery Kit","url":"/api/equipment/forgery-kit"},{"index":"galley","name":"Galley","url":"/api/equipment/galley"},{"index":"glaive","name":"Glaive","url":"/api/equipment/glaive"},{"index":"glassblowers-tools","name":"Glassblower's Tools","url":"/api/equipment/glassblowers-tools"},{"index":"grappling-hook","name":"Grappling hook","url":"/api/equipment/grappling-hook"},{"index":"greataxe","name":"Greataxe","url":"/api/equipment/greataxe"},{"index":"greatclub","name":"Greatclub","url":"/api/equipment/greatclub"},{"index":"greatsword","name":"Greatsword","url":"/api/equipment/greatsword"},{"index":"halberd","name":"Halberd","url":"/api/equipment/halberd"},{"index":"half-plate-armor","name":"Half Plate Armor","url":"/api/equipment/half-plate-armor"},{"index":"hammer","name":"Hammer","url":"/api/equipment/hammer"},{"index":"hammer-sledge","name":"Hammer, sledge","url":"/api/equipment/hammer-sledge"},{"index":"handaxe","name":"Handaxe","url":"/api/equipment/handaxe"},{"index":"healers-kit","name":"Healer's Kit","url":"/api/equipment/healers-kit"},{"index":"herbalism-kit","name":"Herbalism Kit","url":"/api/equipment/herbalism-kit"},{"index":"hide-armor","name":"Hide Armor","url":"/api/equipment/hide-armor"},{"index":"holy-water-flask","name":"Holy water (flask)","url":"/api/equipment/holy-water-flask"},{"index":"horn","name":"Horn","url":"/api/equipment/horn"},{"index":"horse-draft","name":"Horse, draft","url":"/api/equipment/horse-draft"},{"index":"horse-riding","name":"Horse, riding","url":"/api/equipment/horse-riding"},{"index":"hourglass","name":"Hourglass","url":"/api/equipment/hourglass"},{"index":"hunting-trap","name":"Hunting trap","url":"/api/equipment/hunting-trap"},{"index":"ink-1-ounce-bottle","name":"Ink (1 ounce bottle)","url":"/api/equipment/ink-1-ounce-bottle"},{"index":"ink-pen","name":"Ink pen","url":"/api/equipment/ink-pen"},{"index":"javelin","name":"Javelin","url":"/api/equipment/javelin"},{"index":"jewelers-tools","name":"Jeweler's Tools","url":"/api/equipment/jewelers-tools"},{"index":"jug-or-pitcher","name":"Jug or pitcher","url":"/api/equipment/jug-or-pitcher"},{"index":"keelboat","name":"Keelboat","url":"/api/equipment/keelboat"},{"index":"ladder-10-foot","name":"Ladder (10-foot)","url":"/api/equipment/ladder-10-foot"},{"index":"lamp","name":"Lamp","url":"/api/equipment/lamp"},{"index":"lance","name":"Lance","url":"/api/equipment/lance"},{"index":"lantern-bullseye","name":"Lantern, bullseye","url":"/api/equipment/lantern-bullseye"},{"index":"lantern-hooded","name":"Lantern, hooded","url":"/api/equipment/lantern-hooded"},{"index":"leather-armor","name":"Leather Armor","url":"/api/equipment/leather-armor"},{"index":"leatherworkers-tools","name":"Leatherworker's Tools","url":"/api/equipment/leatherworkers-tools"},{"index":"light-hammer","name":"Light hammer","url":"/api/equipment/light-hammer"},{"index":"little-bag-of-sand","name":"Little bag of sand","url":"/api/equipment/little-bag-of-sand"},{"index":"lock","name":"Lock","url":"/api/equipment/lock"},{"index":"longbow","name":"Longbow","url":"/api/equipment/longbow"},{"index":"longship","name":"Longship","url":"/api/equipment/longship"},{"index":"longsword","name":"Longsword","url":"/api/equipment/longsword"},{"index":"lute","name":"Lute","url":"/api/equipment/lute"},{"index":"lyre","name":"Lyre","url":"/api/equipment/lyre"},{"index":"mace","name":"Mace","url":"/api/equipment/mace"},{"index":"magnifying-glass","name":"Magnifying glass","url":"/api/equipment/magnifying-glass"},{"index":"manacles","name":"Manacles","url":"/api/equipment/manacles"},{"index":"masons-tools","name":"Mason's Tools","url":"/api/equipment/masons-tools"},{"index":"mastiff","name":"Mastiff","url":"/api/equipment/mastiff"},{"index":"maul","name":"Maul","url":"/api/equipment/maul"},{"index":"mess-kit","name":"Mess Kit","url":"/api/equipment/mess-kit"},{"index":"mirror-steel","name":"Mirror, steel","url":"/api/equipment/mirror-steel"},{"index":"morningstar","name":"Morningstar","url":"/api/equipment/morningstar"},{"index":"mule","name":"Mule","url":"/api/equipment/mule"},{"index":"navigators-tools","name":"Navigator's Tools","url":"/api/equipment/navigators-tools"},{"index":"net","name":"Net","url":"/api/equipment/net"},{"index":"oil-flask","name":"Oil (flask)","url":"/api/equipment/oil-flask"},{"index":"orb","name":"Orb","url":"/api/equipment/orb"},{"index":"padded-armor","name":"Padded Armor","url":"/api/equipment/padded-armor"},{"index":"painters-supplies","name":"Painter's Supplies","url":"/api/equipment/painters-supplies"},{"index":"pan-flute","name":"Pan flute","url":"/api/equipment/pan-flute"},{"index":"paper-one-sheet","name":"Paper (one sheet)","url":"/api/equipment/paper-one-sheet"},{"index":"parchment-one-sheet","name":"Parchment (one sheet)","url":"/api/equipment/parchment-one-sheet"},{"index":"perfume-vial","name":"Perfume (vial)","url":"/api/equipment/perfume-vial"},{"index":"pick-miners","name":"Pick, miner's","url":"/api/equipment/pick-miners"},{"index":"pike","name":"Pike","url":"/api/equipment/pike"},{"index":"piton","name":"Piton","url":"/api/equipment/piton"},{"index":"plate-armor","name":"Plate Armor","url":"/api/equipment/plate-armor"},{"index":"playing-card-set","name":"Playing Card Set","url":"/api/equipment/playing-card-set"},{"index":"poison-basic-vial","name":"Poison, basic (vial)","url":"/api/equipment/poison-basic-vial"},{"index":"poisoners-kit","name":"Poisoner's Kit","url":"/api/equipment/poisoners-kit"},{"index":"pole-10-foot","name":"Pole (10-foot)","url":"/api/equipment/pole-10-foot"},{"index":"pony","name":"Pony","url":"/api/equipment/pony"},{"index":"pot-iron","name":"Pot, iron","url":"/api/equipment/pot-iron"},{"index":"potters-tools","name":"Potter's Tools","url":"/api/equipment/potters-tools"},{"index":"pouch","name":"Pouch","url":"/api/equipment/pouch"},{"index":"priests-pack","name":"Priest's Pack","url":"/api/equipment/priests-pack"},{"index":"quarterstaff","name":"Quarterstaff","url":"/api/equipment/quarterstaff"},{"index":"quiver","name":"Quiver","url":"/api/equipment/quiver"},{"index":"ram-portable","name":"Ram, portable","url":"/api/equipment/ram-portable"},{"index":"rapier","name":"Rapier","url":"/api/equipment/rapier"},{"index":"rations-1-day","name":"Rations (1 day)","url":"/api/equipment/rations-1-day"},{"index":"reliquary","name":"Reliquary","url":"/api/equipment/reliquary"},{"index":"ring-mail","name":"Ring Mail","url":"/api/equipment/ring-mail"},{"index":"robes","name":"Robes","url":"/api/equipment/robes"},{"index":"rod","name":"Rod","url":"/api/equipment/rod"},{"index":"rope-hempen-50-feet","name":"Rope, hempen (50 feet)","url":"/api/equipment/rope-hempen-50-feet"},{"index":"rope-silk-50-feet","name":"Rope, silk (50 feet)","url":"/api/equipment/rope-silk-50-feet"},{"index":"rowboat","name":"Rowboat","url":"/api/equipment/rowboat"},{"index":"sack","name":"Sack","url":"/api/equipment/sack"},{"index":"saddle-exotic","name":"Saddle, Exotic","url":"/api/equipment/saddle-exotic"},{"index":"saddle-military","name":"Saddle, Military","url":"/api/equipment/saddle-military"},{"index":"saddle-pack","name":"Saddle, Pack","url":"/api/equipment/saddle-pack"},{"index":"saddle-riding","name":"Saddle, Riding","url":"/api/equipment/saddle-riding"},{"index":"saddlebags","name":"Saddlebags","url":"/api/equipment/saddlebags"},{"index":"sailing-ship","name":"Sailing ship","url":"/api/equipment/sailing-ship"},{"index":"scale-mail","name":"Scale Mail","url":"/api/equipment/scale-mail"},{"index":"scale-merchants","name":"Scale, merchant's","url":"/api/equipment/scale-merchants"},{"index":"scholars-pack","name":"Scholar's Pack","url":"/api/equipment/scholars-pack"},{"index":"scimitar","name":"Scimitar","url":"/api/equipment/scimitar"},{"index":"sealing-wax","name":"Sealing wax","url":"/api/equipment/sealing-wax"},{"index":"shawm","name":"Shawm","url":"/api/equipment/shawm"},{"index":"shield","name":"Shield","url":"/api/equipment/shield"},{"index":"shortbow","name":"Shortbow","url":"/api/equipment/shortbow"},{"index":"shortsword","name":"Shortsword","url":"/api/equipment/shortsword"},{"index":"shovel","name":"Shovel","url":"/api/equipment/shovel"},{"index":"sickle","name":"Sickle","url":"/api/equipment/sickle"},{"index":"signal-whistle","name":"Signal whistle","url":"/api/equipment/signal-whistle"},{"index":"signet-ring","name":"Signet ring","url":"/api/equipment/signet-ring"},{"index":"sled","name":"Sled","url":"/api/equipment/sled"},{"index":"sling","name":"Sling","url":"/api/equipment/sling"},{"index":"sling-bullet","name":"Sling bullet","url":"/api/equipment/sling-bullet"},{"index":"small-knife","name":"Small knife","url":"/api/equipment/small-knife"},{"index":"smiths-tools","name":"Smith's Tools","url":"/api/equipment/smiths-tools"},{"index":"soap","name":"Soap","url":"/api/equipment/soap"},{"index":"spear","name":"Spear","url":"/api/equipment/spear"},{"index":"spellbook","name":"Spellbook","url":"/api/equipment/spellbook"},{"index":"spike-iron","name":"Spike, iron","url":"/api/equipment/spike-iron"},{"index":"splint-armor","name":"Splint Armor","url":"/api/equipment/splint-armor"},{"index":"sprig-of-mistletoe","name":"Sprig of mistletoe","url":"/api/equipment/sprig-of-mistletoe"},{"index":"spyglass","name":"Spyglass","url":"/api/equipment/spyglass"},{"index":"stabling-1-day","name":"Stabling (1 day)","url":"/api/equipment/stabling-1-day"},{"index":"staff","name":"Staff","url":"/api/equipment/staff"},{"index":"string-10-feet","name":"String (10 feet)","url":"/api/equipment/string-10-feet"},{"index":"studded-leather-armor","name":"Studded Leather Armor","url":"/api/equipment/studded-leather-armor"},{"index":"tent-two-person","name":"Tent, two-person","url":"/api/equipment/tent-two-person"},{"index":"thieves-tools","name":"Thieves' Tools","url":"/api/equipment/thieves-tools"},{"index":"tinderbox","name":"Tinderbox","url":"/api/equipment/tinderbox"},{"index":"tinkers-tools","name":"Tinker's Tools","url":"/api/equipment/tinkers-tools"},{"index":"torch","name":"Torch","url":"/api/equipment/torch"},{"index":"totem","name":"Totem","url":"/api/equipment/totem"},{"index":"trident","name":"Trident","url":"/api/equipment/trident"},{"index":"vestments","name":"Vestments","url":"/api/equipment/vestments"},{"index":"vial","name":"Vial","url":"/api/equipment/vial"},{"index":"viol","name":"Viol","url":"/api/equipment/viol"},{"index":"wagon","name":"Wagon","url":"/api/equipment/wagon"},{"index":"wand","name":"Wand","url":"/api/equipment/wand"},{"index":"war-pick","name":"War pick","url":"/api/equipment/war-pick"},{"index":"warhammer","name":"Warhammer","url":"/api/equipment/warhammer"},{"index":"warhorse","name":"Warhorse","url":"/api/equipment/warhorse"},{"index":"warship","name":"Warship","url":"/api/equipment/warship"},{"index":"waterskin","name":"Waterskin","url":"/api/equipment/waterskin"},{"index":"weavers-tools","name":"Weaver's Tools","url":"/api/equipment/weavers-tools"},{"index":"whetstone","name":"Whetstone","url":"/api/equipment/whetstone"},{"index":"whip","name":"Whip","url":"/api/equipment/whip"},{"index":"woodcarvers-tools","name":"Woodcarver's Tools","url":"/api/equipment/woodcarvers-tools"},{"index":"wooden-staff","name":"Wooden staff","url":"/api/equipment/wooden-staff"},{"index":"yew-wand","name":"Yew wand","url":"/api/equipment/yew-wand"}]}


# print("equipment keys")
# print (equipment.keys())
# # # keys: count, results

# # print("equipment results")
# # print(equipment['results'])

# print("equipment count")
# print(equipment['count'])
# # 237

# print("these are the names of all equipment items")
# for item in equipment['results']:
#     print(item['name'])

# print("these are results keys")
# for item in equipment['results']:
#     print(item.keys())
#     # index, name, url

blowgun = {
 "desc": [],
 "special": [],
 "index": "blowgun",
 "name": "Blowgun",
 "equipment_category": {
  "index": "weapon",
  "name": "Weapon",
  "url": "/api/equipment-categories/weapon"
 },
 "weapon_category": "Martial",
 "weapon_range": "Ranged",
 "category_range": "Martial Ranged",
 "cost": {
  "quantity": 10,
  "unit": "gp"
 },
 "damage": {
  "damage_dice": "1",
  "damage_type": {
   "index": "piercing",
   "name": "Piercing",
   "url": "/api/damage-types/piercing"
  }
 },
 "range": {
  "normal": 25,
  "long": 100
 },
 "weight": 1,
 "properties": [
  {
   "index": "ammunition",
   "name": "Ammunition",
   "url": "/api/weapon-properties/ammunition"
  },
  {
   "index": "loading",
   "name": "Loading",
   "url": "/api/weapon-properties/loading"
  }
 ],
 "url": "/api/equipment/blowgun",
 "contents": []
}

abacus = {
 "desc": [],
 "special": [],
 "index": "abacus",
 "name": "Abacus",
 "equipment_category": {
  "index": "adventuring-gear",
  "name": "Adventuring Gear",
  "url": "/api/equipment-categories/adventuring-gear"
 },
 "gear_category": {
  "index": "standard-gear",
  "name": "Standard Gear",
  "url": "/api/equipment-categories/standard-gear"
 },
 "cost": {
  "quantity": 2,
  "unit": "gp"
 },
 "weight": 2,
 "url": "/api/equipment/abacus",
 "contents": [],
 "properties": []
}

sheild = {
 "desc": [],
 "special": [],
 "index": "shield",
 "name": "Shield",
 "equipment_category": {
  "index": "armor",
  "name": "Armor",
  "url": "/api/equipment-categories/armor"
 },
 "armor_category": "Shield",
 "armor_class": {
  "base": 2,
  "dex_bonus": false
 },
 "str_minimum": 0,
 "stealth_disadvantage": false,
 "weight": 6,
 "cost": {
  "quantity": 10,
  "unit": "gp"
 },
 "url": "/api/equipment/shield",
 "contents": [],
 "properties": []
}