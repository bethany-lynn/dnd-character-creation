# might need jsonify
# going to use api to fetch information based off of a users selected class and race to fill in specific data 
# for those respective form inputs 

# will need to hard code some dnd info (classes, races, name, etc)

# fetching api requests on the backend will be done in a python file, not in the frontend
# will be using jinja to do so - use the balloonicorn party api lab for reference
# if class == druid, weapons == _____, gp == _____, wisdom == _____, etc
# if race == human, atheltics == _____, etc

# backstory will be a text input field
# alignment can be random or selected from a form

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import *
import crud
from jinja2 import StrictUndefined
import requests
import json
import random

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """view homepage"""

    return render_template('homepage.html')

@app.route("/users", methods=["POST"])
def register_user():
    """create a new user"""


    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("This email is already plundering dungeons and slaying dragons.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Hail and well met, adventurer, your account has been created!")
        return redirect("/create_character")

    return redirect("/")


@app.route('/login', methods=['POST'])
def login():
    """existing accounts can login"""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Your email or password is incorrect, adventurer!")
        return redirect('/')
    else:
        session['user_email'] = user.email
        session['user_id'] = user.user_id
        flash(f'Welcome back, {user.email}!')

    return redirect("/user_profile")

@app.route('/create_character')
def create_page():
    """create a character after logging in or creating an account"""

    dungeons_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk",
                    "paladin", "ranger", "rogue", "sorcerer", "warlock",
                    "wizard"]
    dungeons_races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf",
                    "halfling", "half-orc", "human", "tiefling"]
    dungeons_alignments = ["lawful-good", "neutral-good", "chaotic-good",
                        "lawful-neutral", "neutral", "chaotic-neutral",
                        "lawful-evil", "neutral-evil", "chaotic-evil"]
    dungeons_genders = ["female", "male", "non-binary", "gender fluid", 
                    "agender", "transgender", "other"]
    dungeons_eye_colors = ["brown", "gray", "black", "green", "hazel", 
                    "blue", "orange", "pink", "purple", "red", "white"]
    dungeons_hair_colors = [
                    "chartreuse", "brown", "gray", "black", "green", "mint", "blue", 
                    "copper", "pink", "purple", "red", "silver", 
                    "white", "blonde", "yellow"]

    return render_template('create_character.html', dungeons_classes=dungeons_classes, 
                            dungeons_races=dungeons_races, dungeons_alignments=dungeons_alignments,
                            dungeons_genders=dungeons_genders, dungeons_eye_colors=dungeons_eye_colors,
                            dungeons_hair_colors=dungeons_hair_colors)



@app.route('/create_character', methods =["POST"])
def create_character():
    """where a user can access previously saved sheets after submitting"""


    """requesting from user input forms"""
    char_name = request.form.get('char_name')
    dun_class = request.form.get('dungeons_classes')
    dun_race = request.form.get('dungeons_races')
    alignment = request.form.get('dungeons_alignments')
    gender = request.form.get('dungeons_genders')
    eye_color = request.form.get('dungeons_eye_colors')
    hair_color = request.form.get('dungeons_hair_colors')
    wisdom_stat = request.form.get('wisdom-stat')
    charisma_stat = request.form.get('charisma-stat')
    intelligence_stat = request.form.get('intelligence-stat')
    dexterity_stat = request.form.get('dexterity-stat')
    constitution_stat = request.form.get('constitution-stat')
    strength_stat = request.form.get('strength-stat')
    user_id = session['user_id']

    api_url = f'https://www.dnd5eapi.co/api/classes/{dun_class}'
    response = requests.get(api_url)
    class_stats = response.json()

    api_url = f'https://www.dnd5eapi.co/api/races/{dun_race}'
    response=requests.get(api_url)
    race_stats = response.json()

    """static info from api requests"""
    hit_die = class_stats["hit_die"] 
    walking_speed = race_stats["speed"]
    char_language = crud.get_language_by_race(dun_race)

    """static info not from api"""
    level = 1
    # query selector

    lang_list = char_language.split("+")
  

    """creating a character sheet object"""
    character = Character_sheet(
        user_id = user_id,
        character_name = char_name,
        character_class = dun_class,
        race = dun_race,
        alignment = alignment,
        gender = gender,
        eye_color = eye_color,
        hair_color = hair_color,
        wisdom = wisdom_stat,
        charisma = charisma_stat,
        intelligence = intelligence_stat,      
        dexterity = dexterity_stat,
        constitution = constitution_stat,
        strength = strength_stat,
        char_hit_die = hit_die,
        char_walking_speed = walking_speed,
        language = char_language,
        char_level = level
    )

    """adding and saving character to database"""
    db.session.add(character)
    db.session.commit()
    # new_character = Character_sheet.query.filter(Character_sheet.name == char_name).first()

    # return render_template('character_secondpage.html', new_character=new_character)
    return render_template('character_secondpage.html', character=character)

    # return render_template('character_secondpage.html', race_stats=race_stats, class_stats=class_stats,
    #                      char_name=char_name, dun_class=dun_class, dun_race=dun_race, 
    #                      alignment=alignment, gender=gender, eye_color=eye_color, 
    #                      hair_color=hair_color, wisdom_stat=wisdom_stat,
    #                     charisma_stat=charisma_stat, intelligence_stat=intelligence_stat,
    #                     dexterity_stat=dexterity_stat, constitution_stat=constitution_stat, 
    #                     strength_stat=strength_stat, hit_die=hit_die, 
    #                    walking_speed=walking_speed, char_language=lang_list, 
    #                    level=level)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



# THURSDAY TO-DO LIST
# figure out how players get all stats (random dice roll, dependant on class, etc)

# finish layout of creation page
#       add text boxes for background input
#       consider how to create an account tab to log in and out from tab, and change routes
#       through the tab, instead of a navbar

# have all data input go to a certain column or row (organize info)

# API - if class is wizard, add (____) to spells, wisdom, etc 

# consider layout for a form with empty "inputs" where all stats and numbers will go