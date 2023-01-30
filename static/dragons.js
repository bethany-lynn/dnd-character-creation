let results = {
    wisdom: 0,
    charisma: 0,
    intelligence: 0,
    dexterity: 0,
    constitution: 0,
    strength: 0
};

function rollDie(numRolls, numToKeep, button) {
    let rolls = []
    for (let i = 0; i < numRolls; i++) {
        rolls.push(Math.floor(Math.random() * 6) + 1);
    }
    rolls.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < numToKeep; i++) {
        total += rolls[i];
    }
    const newElement = document.createElement("span");
    newElement.innerHTML = total;
    button.insertAdjacentElement("afterend", newElement);
    button.setAttribute("disabled", true);
    let stat = button.getAttribute("data-stat");
    results[stat] = total;

    results[stat] = total;
    sessionStorage.setItem('results', JSON.stringify(results));

}

const buttons = document.querySelectorAll('.roll_dice');
// let storedResults = JSON.parse(sessionStorage.getItem('results'));

buttons.forEach(button => {
    button.addEventListener('click', () => {
      const rolls = 4;
      const keep = 3;
      rollDie(rolls, keep, button);
    });
});



const submitButton = document.querySelector("#submit_button");
submitButton.addEventListener("click", () => {
document.querySelector("#wisdom").innerHTML = results.wisdom;
document.querySelector("#charisma").innerHTML = results.charisma;
document.querySelector("#intelligence").innerHTML = results.intelligence;
document.querySelector("#dexterity").innerHTML = results.dexterity;
document.querySelector("#constitution").innerHTML = results.constitution;
document.querySelector("#strength").innerHTML = results.strength;
});



// may need to edit or remove lines:
// 12, 15, 16, 31, 32, 33, etc