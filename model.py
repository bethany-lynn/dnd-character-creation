"""Models for character creation app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users_table"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))

    character_sheet = db.relationship("Character_sheet", back_populates="user")

    def __repr__(self):
        return f'<User: {self.user_id}, email: {self.email}, username: {self.username}>'

class Character_sheet(db.Model):
    """A character sheet"""

    __tablename__ = "character_sheet"

    character_id = db.Column(db.Integer,
                             autoincrement=True,
                             primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users_table.user_id"))

    character_name = db.Column(db.String(50))
    character_class = db.Column(db.String(50))
    race = db.Column(db.String(50))

    alignment = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))

    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    strength = db.Column(db.Integer)

    char_walking_speed = db.Column(db.Integer)
    language = db.Column(db.String(50))
    char_hit_die = db.Column(db.Integer)

    current_hit_points = db.Column(db.Integer)
    total_hit_points = db.Column(db.Integer)
    char_level = db.Column(db.Integer, default=1)

    animal_handling = db.Column(db.Integer)
    acrobatics = db.Column(db.Integer)
    arcana = db.Column(db.Integer, default=0)
    athletics = db.Column(db.Integer)
    deception = db.Column(db.Integer, default=0)
    history = db.Column(db.Integer, default=0)
    insight = db.Column(db.Integer)
    intimidation = db.Column(db.Integer, default=0)
    investigation = db.Column(db.Integer, default=0)
    medicine = db.Column(db.Integer)
    nature = db.Column(db.Integer, default=0)    
    perception = db.Column(db.Integer)
    performance = db.Column(db.Integer, default=0)
    persuasion = db.Column(db.Integer, default=0)
    religion = db.Column(db.Integer, default=0)
    sleight_of_hand = db.Column(db.Integer, default=0)
    stealth = db.Column(db.Integer, default=0)
    survival = db.Column(db.Integer)
    inspiration = db.Column(db.Boolean, default=False)
   # done ^
    
# currently saved in database per character, though
    proficiency_bonus = db.Column(db.Integer)
    # starts at 2, determined by level.
    passive_wisdom = db.Column(db.Integer)
    passive_perception = db.Column(db.Integer)
    passive_insight = db.Column(db.Integer)
    # wisdom modifier + 10 ^
    experience = db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    # background = db.Column(db.Text)
    initiative = db.Column(db.Integer)
    condition = db.Column(db.Integer)

    user = db.relationship("User", back_populates="character_sheet")
    inventory_table = db.relationship("Inventory", back_populates="character_sheet")
    spell_slots = db.relationship("Spell_slots", back_populates="character_sheet")
    character_spells = db.relationship("Char_spells", back_populates="character_sheet")
    character_weapons = db.relationship("Char_weapons", back_populates="character_sheet")

    def __repr__(self):
        return f'<character: {self.character_name}>'
    
    # def __iter__(self):
    #     yield 'character_name', self.character_name
    #     yield 'user_id', self.user_id

class Inventory(db.Model):
    """A character's starting bag"""

    __tablename__ = "inventory_table"

    inventory_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character_sheet.character_id"))
    inventory_item_id = db.Column(db.Integer, db.ForeignKey("inventory_items.inventory_item_id"))

    character_sheet = db.relationship("Character_sheet", back_populates="inventory_table")
    inventory_items = db.relationship("Inventory_items", back_populates="inventory_table")

    def __repr__(self):
        return f'<>'

class Inventory_items(db.Model):
    """The contents of the character's bag"""

    __tablename__ = "inventory_items"

    inventory_item_id = db.Column(db.Integer,
                                 autoincrement=True,
                                primary_key=True)
    item_name = db.Column(db.String(50))
    item_type = db.Column(db.String(50))
    item_weight = db.Column(db.Integer)    
    item_description = db.Column(db.String(50))
    tracking_cost = db.Column(db.Integer)

    inventory_table = db.relationship("Inventory", back_populates="inventory_items")
    
    def __repr__(self):
        return f'<>'

class Spell_slots(db.Model):
    """Spell slots for characters with casting abilities"""

    __tablename__ = "spell_slots"

    spell_slot_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character_sheet.character_id"))
    spell_level = db.Column(db.Integer)
    num_of_slots = db.Column(db.Integer)
    currently_user = db.Column(db.Integer)

    character_sheet = db.relationship("Character_sheet", back_populates="spell_slots")    

    def __repr__(self):
        return f'<>'

class Char_spells(db.Model):
    """Spells for a given character"""

    __tablename__ = "character_spells"

    char_spells_id = db.Column(db.Integer,
                               autoincrement=True,
                               primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character_sheet.character_id"))
    char_spell_id = db.Column(db.Integer, db.ForeignKey("spells_table.spell_id"))

    character_sheet = db.relationship("Character_sheet", back_populates="character_spells")    
    spells = db.relationship("Spells", back_populates="character_spells")

    def __repr__(self):
        return f'<>'

class Spells(db.Model):
    """Information needed for all spells - levels, types, etc"""

    __tablename__ = "spells_table"
    
    spell_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    spell_name = db.Column(db.String)
    description = db.Column(db.Text)
    higher_level = db.Column(db.String)
    spell_range = db.Column(db.String)
    components = db.Column(db.String)
    material = db.Column(db.String)
    duration = db.Column(db.Integer) 
    cast_time = db.Column(db.String)       
    spell_level = db.Column(db.String)
    school = db.Column(db.String)
    classes = db.Column(db.Integer)
    subclasses = db.Column(db.String)

    character_spells = db.relationship("Char_spells", back_populates="spells")

    def __repr__(self):
        return f'<>'

class Char_weapons(db.Model):
    """Weapons for a given character"""

    __tablename__ = "character_weapons"
    
    char_weapon_id = db.Column(db.Integer,
                               autoincrement=True,
                               primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character_sheet.character_id"))
    weapon_id = db.Column(db.Integer, db.ForeignKey("weapons_table.weapon_id"))

    character_sheet = db.relationship("Character_sheet", back_populates="character_weapons")
    weapons_table = db.relationship("Weapons", back_populates="character_weapons")

    
    def __repr__(self):
        return f'<>'

class Weapons(db.Model):
    """Weapon information"""

    __tablename__ = "weapons_table"

    weapon_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)
    weapon_name = db.Column(db.String(50))
    damage_type = db.Column(db.String(50))
    weapon_range = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    properties = db.Column(db.Integer)

    character_weapons = db.relationship("Char_weapons", back_populates="weapons_table")

    def __repr__(self):
        return f'<>'

def connect_to_db(flask_app, db_uri="postgresql:///creation", echo=False):
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


#------------------------------------------------------------------------------------#
# things to do TUESDAY JAN 23:


# add all templates to folder
# figure out one query string with AJAX