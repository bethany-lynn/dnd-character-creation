"""CRUD operations."""

from model import db, User, Character_sheet, Inventory, Spell_slots, Char_spells, Spells, Char_weapons, Weapons, connect_to_db

def create_user(email, password, username):
    """Create and return a new user."""

    user = User(email=email, password=password, username=username)

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)