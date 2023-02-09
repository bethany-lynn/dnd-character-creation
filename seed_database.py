"""Script to seed database."""

from flask import Flask, session
import os
import json
from random import choice, randint
from datetime import datetime
import requests
from model import Spells, db
import crud
import model
import server

os.system("dropdb creation")
os.system("createdb creation")

model.connect_to_db(server.app)
model.db.create_all()


def get_spells_from_api():
    """getting spell information from the api"""
    api_url = f'http://www.dnd5eapi.co/api/spells'
    response=requests.get(api_url)
    spell_names = response.json()

    for result in spell_names['results']:
        name_of_spell = result['name']

        api_url = f"http://www.dnd5eapi.co/api/spells/{name_of_spell}"
        response=requests.get(api_url)
        spell_info = response.json()

        print(result['name'])
        spells = Spells(
            spell_name = result['name'],
            description = spell_info['desc'],
            higher_level = spell_info['higher_level'],
            spell_range = spell_info['range'],
            components = spell_info['components'],
            cast_time = spell_info['casting_time'],
            spell_level = spell_info['level']
            )

        db.session.add(spells)

    db.session.commit()


get_spells_from_api()

