"""CRUD operations."""
# create, read, update, delete
# actions to perform on a set of data - creating new, retrieving, uupdating, deleting

from model import db, User, Character_sheet, Inventory, Spell_slots, Char_spells, Spells, Char_weapons, Weapons, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_user_by_email(email):
    """return a user by email"""
    return User.query.filter(User.email == email).first()

def get_users():
    """Return all users."""

    return User.query.all()  

def get_user_by_email(email):
    """return a user by email""" 

    return  User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """return a user by id"""
    return User.query.get(user_id)

def get_language_by_race(dun_race):
    if dun_race == "dragonborn":
        return "common+draconic"
    elif dun_race == "dwarf":
        return "common+dwarvish"
    elif dun_race == "elf":
        return "common+elvish"
    elif dun_race == "gnome":
        return "common+gnomish"
    elif dun_race == "half-elf":
        return "common+elvish"
        # can speak on extra language of choosing
    elif dun_race == "halfling":
        return "common+halfling"
    elif dun_race == "half-orc":
        return "common+orc"
    elif dun_race == "human":
        return "common"
        # can speak one extra language of choosing
    elif dun_race == "tiefling":
        return "common+infernal"

if __name__ == '__main__':
    from server import app
    connect_to_db(app)