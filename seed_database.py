"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb creation")
os.system("createdb creation")

model.connect_to_db(server.app)
model.db.create_all()

# Load creation data from JSON file
with open('data/creation.json') as f:
    creation_data = json.loads(f.read())