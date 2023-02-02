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

    return redirect("/create_character")
    # change this to redirect to user_profile when that route is complete

@app.route('/user_profile')
def user_profile():
    # flash message to welcome user back to the adventure
    # route to create character in create_character route
    # list all created characters with links to see their sheets in finalalized_character route
    # log out button to route to homepage /
    # navbar?
    return redirect('/')

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
    # user_id = session['user_id']
    

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

    """assigning language to a variable by splitting"""
    lang_list = char_language.split("+")

    """conditionals to get character skills based off of their modifiers"""
    if int(constitution_stat) > 11:
        constitution_mod = (int(constitution_stat) - 10) // 2
        hit_points = hit_die + random.choice(range(1, hit_die + 1)) + constitution_mod
    else:
        constitution_mod = 0
        hit_points = hit_die + random.choice(range(1, hit_die + 1)) + constitution_mod

    if int(wisdom_stat) > 11:
        animal_hand = (int(wisdom_stat) - 10) //2
        insight_stat = (int(wisdom_stat) - 10) //2
        medicine_stat = (int(wisdom_stat) - 10) //2
        perception_stat = (int(wisdom_stat) - 10) //2
        survival_stat = (int(wisdom_stat) - 10) //2
    else:
        animal_hand = 0
        insight_stat = 0
        medicine_stat = 0
        perception_stat = 0
        survival_stat = 0

    if int(charisma_stat) > 11:
        persuasion_stat = (int(charisma_stat) - 10) //2
        performance_stat = (int(charisma_stat) - 10) //2
        intimidation_stat = (int(charisma_stat) - 10) //2
        deception_stat = (int(charisma_stat) - 10) //2
    else:
        persuasion_stat = 0
        performance_stat = 0
        intimidation_stat = 0
        deception_stat = 0

    if int(intelligence_stat) > 11:
        religion_stat = (int(intelligence_stat) - 10) //2
        nature_stat = (int(intelligence_stat) - 10) //2
        history_stat = (int(intelligence_stat) - 10) //2
        arcana_stat = (int(intelligence_stat) - 10) //2
        investigation_stat = (int(intelligence_stat) - 10) //2
    else:
        religion_stat = 0
        nature_stat = 0
        history_stat = 0
        arcana_stat = 0
        investigation_stat = 0

    if int(dexterity_stat) > 11:
        acrobatics_stat = (int(dexterity_stat) - 10) //2
        sleight_of_hand_stat = (int(dexterity_stat) - 10) //2
        stealth_stat = (int(dexterity_stat) - 10) //2
    else:
        acrobatics_stat = 0
        sleight_of_hand_stat = 0
        stealth_stat = 0

    if int(strength_stat) > 11:
        athletics_stat = (int(strength_stat) - 10) //2
    else:
        athletics_stat = 0

    """creating a character sheet object"""
    character = Character_sheet(
        # user_id = user_id,
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
        current_hit_points = hit_points,
        total_hit_points = hit_points,
        animal_handling = animal_hand,
        insight = insight_stat,
        medicine = medicine_stat,
        perception = perception_stat,
        survival = survival_stat,
        persuasion = persuasion_stat,
        performance = performance_stat,
        intimidation = intimidation_stat,
        deception = deception_stat,
        religion = religion_stat,
        nature = nature_stat,
        history = history_stat,
        arcana = arcana_stat,
        investigation = investigation_stat,
        athletics = athletics_stat,
        acrobatics = acrobatics_stat,
        sleight_of_hand = sleight_of_hand_stat, 
        stealth = stealth_stat
    )

    """adding and saving character to database"""
    db.session.add(character)
    db.session.commit()


    db.session.refresh(character)
    print()
    print("this is character id")
    print(character.character_id)
    session['character_id'] = character.character_id
    # may need to modify ^ ?

    
    # if dun_class == "bard" or "cleric" or "druid" or "sorcerer" or "wizard" or "warlock" or :
    #     return redirect('spellslots.html')
    #     # if dun_class in []

    return render_template('character_secondpage.html', character=character, char_language=lang_list)


@app.route('/character_skills')
def assign_skills():

    character_id = session['character_id']
    # unsure if this is correct ^ test and modify maybe
    # this is correct
    # yay! :) 

    character = crud.get_character_by_id(character_id)
    print()
    print('this is a character')
    print(character)
    return render_template('character_thirdpage.html', character=character)



@app.route('/spellslots')
def get_spellslots_from_class():

    # user can select 4 cantrips
    # user can pick 2 spells
    # commit to character sheet table 
    return render_template('character_secondpage.html')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



# next tasks:
# assign character level to sheet, start at 1
# limit check boxes to two or three clicks depending on class
# add event listener

# tomorrow?
# work on classes that get spell slots
# if class ____ : add a form with spells to select from
# add another form for cantrips?

# update thirdpage to display info from secondpage form (selected skills)
# update thirdpage to displau info from spell slot form