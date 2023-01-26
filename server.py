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
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

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

@app.route('/user_profile')
def profile_page():
    """where a user can access previously saved sheets"""
    return render_template('user_profile.html')
    # have option to go to character creation page for new character

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



# WEDNESDAY TO DO AFTER LUNCH
# connect lists in this file to html code and correct routes
# make sure when on the character creation page, there are forms to select from these lists
# consider layout for a form with empty "inputs" where all stats and numbers will go