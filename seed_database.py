"""Script to seed database."""

from flask import Flask, session
import os
import json
from random import choice, randint
from datetime import datetime
import requests
from model import Spells, Weapons, Inventory_items, Armor, db
import crud
import model
import server

os.system("dropdb creation")
os.system("createdb creation")

model.connect_to_db(server.app)
server.app.app_context().push
# syncing?
model.db.create_all()


def get_spells_from_api():
    """getting spell information for Spells class from the api"""

    api_url = f'http://www.dnd5eapi.co/api/spells'
    response=requests.get(api_url)
    spell_names = response.json()

    for result in spell_names['results']:
        url_of_spell = result['url']

        api_url = f"http://www.dnd5eapi.co{url_of_spell}"
        response=requests.get(api_url)
        spell_info = response.json()

        spells = Spells(
            spell_name = result['name'],
            description =", ".join(spell_info['desc']),
            higher_level =", ".join(spell_info['higher_level']),
            spell_range = spell_info['range'],
            components =", ".join(spell_info['components']),
            cast_time = spell_info['casting_time'],
            spell_level = str(spell_info['level'])
            )
        # session['spell_id'] = spells.spell_id

        db.session.add(spells)
    db.session.commit()

get_spells_from_api()


def get_weapons_from_api():
    """getting weapon information for Weapons class from api"""

    api_url = f'http://www.dnd5eapi.co/api/equipment-categories/weapon'
    response=requests.get(api_url)
    weapon_names = response.json()


    for weapon in weapon_names['equipment']:
        name_of_weapon = weapon['name']
        url_of_weapon = weapon['url']

        api_url = f"http://www.dnd5eapi.co{url_of_weapon}"
        response=requests.get(api_url)
        weapon_info = response.json()

        damage_type = ""
        if "damage" in weapon_info:
            damage_type = weapon_info["damage"]["damage_type"]["name"]

        weapon_range = ""
        if "range" in weapon_info:
            weapon_range = str(weapon_info['range']['normal'])
        
        cost = ""
        if "cost" in weapon_info:
            cost = weapon_info['cost']['quantity']

        weight = ""
        if "weight" in weapon_info:
            weight = weapon_info['weight']

        weapons = Weapons(
            weapon_name = name_of_weapon,
            damage_type = damage_type,
            weapon_range = weapon_range,
            cost = cost,
            weight = weight
        )

        db.session.add(weapons)
    db.session.commit()
    print("weapon_range")

get_weapons_from_api()    


# def get_inventory_gear_from_api():
#     """getting all gear for inventory class from api"""

#     api_url = f'http://www.dnd5eapi.co/api/equipment-categories/adventuring-gear'
#     response=requests.get(api_url)
#     gear_names = response.json()

#     for gear in gear_names['equipment']:
#         name_of_gear = gear['name']
#         url_of_gear = gear['url']

#         api_url = f'http://www.dnd5eapi.co{url_of_gear}'
#         response=requests.get(api_url)
#         gear_info = response.json()

#         inventory = Inventory_items(
#             item_name = name_of_gear,
#             item_type = ,
#             item_weight = ,
#             item_description = ,
#             tracking_cost =
#         )

#         db.session.add(inventory)
#     db.session.commit()

# get_inventory_gear_from_api()


# def get_armor_from_api():
#     """getting armor information for Armor class from api"""

#     api_url = f'http://www.dnd5eapi.co/api/equipment-categories/armor'
#     response=requests.get(api_url)
#     armor_names = response.json()

#     for armor in armor_names['equipment']:
#         name_of_armor = armor['name']
#         url_of_armor = armor['url']

#         api_url = f'http://www.dnd5eapi.co{url_of_armor}'
#         response=requests.get(api_url)
#         armor_info = response.json()

#         armor = Armor(
#             armor_name = name_of_armor,
#             str_minimum =
#             stealth_disadvantage = 
#             cost = 
#             weight = 
#             properties =
#         )

#         db.session.add(armor)
#     db.session.commit()

# get_armor_from_api()




# get name of equipment items with equipment_category url
# weapons = api/equipment-categories/weapon
#  ^ gives nested dictionaries of all weapons
# inventory items = api/equipment-categories/adventuring-gear
#  ^ gives nested dictionaries of all gear
# armor = api/equipment-categoreis/armor
#  ^ gives nested dictionaries of all armor