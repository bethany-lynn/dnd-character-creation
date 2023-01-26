'use strict';


// const hairColorSelect = document.querySelector("#dungeons_hair_colors");
// const hairColorResult = document.querySelector("#hair-color-result");

const hairSelect = document.querySelector("#hair-color form");
const hairResult = document.querySelector("#hair-color-result");

hairSelect.addEventListener("submit", function(evt){
    evt.preventDefault();
    
    const selectedHairColor = hairSelect.querySelector("#dungeons_hair_colors").value;
    hairResult.innerHTML = selectedHairColor;
});
