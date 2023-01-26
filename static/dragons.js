'use strict';
// these refer to the form(s) and the spans to replace the innerHTML

const classSelect = document.querySelector("form");
const classResult = document.querySelector("#class-result");

const raceSelect = document.querySelector("form");
const raceResult = document.querySelector("#race-result");

const alignmentSelect = document.querySelector("form");
const alignmentResult = document.querySelector("#alignment-result");

const genderSelect = document.querySelector("form");
const genderResult = document.querySelector("#gender-result");

const eyeSelect = document.querySelector("form");
const eyeResult = document.querySelector("#eye-color-result");

const hairSelect = document.querySelector("form");
const hairResult = document.querySelector("#hair-color-result");


// create a function for all of the same items in a form, because they have the 
// same submit button. would need more functions if i had
// different buttons
hairSelect.addEventListener("submit", function(evt){
    evt.preventDefault();
    
    const selectedClass = classSelect.querySelector("#dungeons_classes").value;
    classResult.innerHTML = selectedClass

    const selectedRace = raceSelect.querySelector("#dungeons_races").value;
    raceResult.innerHTML = selectedRace

    const selectedAlignment = alignmentSelect.querySelector("#dungeons_alignments").value;
    alignmentResult.innerHTML = selectedAlignment

    const selectedGender = genderSelect.querySelector("#dungeons_genders").value;
    genderResult.innerHTML = selectedGender

    const selectedEyeColor = eyeSelect.querySelector("#dungeons_eye_colors").value;
    eyeResult.innerHTML = selectedEyeColor

    const selectedHairColor = hairSelect.querySelector("#dungeons_hair_colors").value;
    hairResult.innerHTML = selectedHairColor;
// variable = variable from above, select at the select-id in the html, add value, change innerhtml
});

