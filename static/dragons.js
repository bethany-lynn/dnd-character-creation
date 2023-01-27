'use strict';
// these refer to the form(s) and the spans to replace the innerHTML

const characterSelectForm = document.querySelector("form");

const classResult = document.querySelector("#class-result");

const raceResult = document.querySelector("#race-result");

const alignmentResult = document.querySelector("#alignment-result");

const genderResult = document.querySelector("#gender-result");

const eyeResult = document.querySelector("#eye-color-result");

const hairResult = document.querySelector("#hair-color-result");


// create a function for all of the same items in a form, because they have the 
// same submit button. would need more functions if i had
// different buttons
characterSelectForm.addEventListener("submit", function(evt){
    evt.preventDefault();
    // console.log(classSelect.querySelector("#dungeons_classes"))

    const selectedClass = characterSelectForm.querySelector("#dungeons_classes").value;
    classResult.innerHTML = selectedClass

    const selectedRace = characterSelectForm.querySelector("#dungeons_races").value;
    raceResult.innerHTML = selectedRace

    const selectedAlignment = characterSelectForm.querySelector("#dungeons_alignments").value;
    alignmentResult.innerHTML = selectedAlignment

    const selectedGender = characterSelectForm.querySelector("#dungeons_genders").value;
    genderResult.innerHTML = selectedGender

    const selectedEyeColor = characterSelectForm.querySelector("#dungeons_eye_colors").value;
    eyeResult.innerHTML = selectedEyeColor

    const selectedHairColor = characterSelectForm.querySelector("#dungeons_hair_colors").value;
    hairResult.innerHTML = selectedHairColor;

    const characterData = {
        class: selectedClass,
        race: selectedRace,
        alignment: selectedAlignment,
        gender: selectedGender,
        eyeColor: selectedEyeColor,
        hairColor: selectedHairColor,
    };

    // make an http request with fetch (to server)
    fetch('/create_character', {
        method:'POST',
        body: JSON.stringify(characterData),
        headers:{
            'Content-Type': 'application/json',
        },
    })
        .then((response) => response.json())
        .then((serverData) => {
            console.log(serverData)
        })
// variable = variable from above, select at the select-id in the html, add value, change innerhtml
});

// if character picks barbarian, then:
//      50 gp (2d4 and 10gp)
//      prof. bonus +2
//      1st level features: rage, unarmored defense
//      hit points - 12+ const. mod
//      light armor, simple weapons
//      choose two skills: animal handling, athletics, intimidation, nature, perception, survival
//      equip: greataxe or melee weapon, two handaxes or any simple weapon, and an explorers pack and four javelins
//      


//racial traits
//class features : hit points, proficiencies, rage, unarmored defense
//standard array of abilities

