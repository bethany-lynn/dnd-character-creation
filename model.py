"""Models for character creation app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class User(db.Model):
    """A user"""

    __tablename__ = "users_page"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))

    character_sheet = db.relationship("Character_sheet", back_populates="user")

    def __repr__(self):
        return f'<User: {self.user_if}, email: {self.email}, username: {self.username}>'

class Character_sheet(db.Model):
    """A character sheet"""

    __tablename__ = "character_sheet"

    user = db.relationship("User", back_populates="character_sheet")
    character_bag = db.relationship("Char_bag", back_populates="character_sheet")
    spell_slots = db.relationship("Spell_slots", back_populates="character_sheet")
    spells = db.relationship("Spells", back_populates="character_sheet")
    character_weapons = db.relationship("Char_weapons", back_populates="character_sheet")
    # Char_weapons


class Char_bag(db.model):
    """A character's starting bag"""

class Bag_items(db.model):
    """The contents of the character's bag"""

class Spell_slots(db.model):
    """Spell slots for characters with casting abilities"""

class Char_spells(db.Model):
    """Spells for a given character"""

class Spells(db.Model):
    """Information needed for all spells - levels, types, etc"""

class Char_weapons(db.Model):
    """Weapons for a given character"""

class Weapons(db.Model):
    """Weapon information"""

def connect_to_db(flask_app, db_uri="postgresql:///creation", echo=True):
    """seting up a connection to a postgreSQL database using a SQLAlchemy library"""
    # flask_app -> application instance used to configure database connection
    # db_uri -> string that represents the database connection URL
    # echo -> boolean value to determine whether SQLA should print statements
    #       its executing. default value is True

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    # set to the value of the db_uri argument
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    # set to value of echo argument
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # disables SQLA's modification tracking feature
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)