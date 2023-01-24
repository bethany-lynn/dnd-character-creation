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


if __name__ == '__main__':
    from server import app
    connect_to_db(app)