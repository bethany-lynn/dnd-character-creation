"""Script to seed database."""

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

    api_url = f'http://www.dnd5eapi.co/api/spells'
    response=requests.get(api_url)
    spell_names = response.json()
    print('this is spell names')
    # print(spell_names)

    for result in spell_names['results']:
        print(result['name'])
        spells = Spells(
            spell_name = result['name']
            )
        # character.character_spells.append(spells)
        # somehow make new char.spells instance
        db.session.add(spells)

    db.session.commit()
    
get_spells_from_api()

# Load creation data from JSON file
# with open('data/creation.json') as f:
#     creation_data = json.loads(f.read())

# create sample user
# add to db
# give char sheet for user
# add to db
# should use magic
# call api for all spells (api_info)
#   returns huge object
# populate spells table with info
# check that its working - psql
# start hooking spells to sheets
# 