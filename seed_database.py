"""Script to seed database."""

from flask import Flask, session
import os
import json
from random import choice, randint
from datetime import datetime
import requests
from model import Spells, Weapons, db
import crud
import model
import server

os.system("dropdb creation")
os.system("createdb creation")

model.connect_to_db(server.app)
model.db.create_all()


def get_spells_from_api():
    """getting spell information for Spells class from the api"""

    api_url = f'http://www.dnd5eapi.co/api/spells'
    response=requests.get(api_url)
    spell_names = response.json()

    for result in spell_names['results']:
        # name_of_spell = result['name']
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

        db.session.add(spells)
    db.session.commit()

    session['spell_id'] = spells.spell_id

get_spells_from_api()


def get_weapons_from_api():
    """getting weapon information for Weapons class from api"""

    api_url = f'http://www.dnd5eapi.co/api/equipment'
    response=requests.get(api_url)
    weapon_names = response.json()


    for result in weapon_names['results']:
        name_of_weapon = result['name']
        url_of_weapon = result['url']

        api_url = f"http://www.dnd5eapi.co{url_of_weapon}"
        response=requests.get(api_url)
        weapon_info = response.json()

        weapons = Weapons(
            weapon_name = result['name'],
            damage_type = weapon_info["damage"]["damage_type"]["name"],
            weapon_range =str(weapon_info['range']['normal']),
            cost = str(weapon_info['cost']['quantity']),
            weight = str(weapon_info['weight'])
        )

        db.session.add(weapons)
    db.session.commit()
    print("weapon_range")

get_weapons_from_api()    
