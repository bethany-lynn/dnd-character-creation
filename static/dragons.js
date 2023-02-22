let results = {
    wisdom: 0,
    charisma: 0,
    intelligence: 0,
    dexterity: 0,
    constitution: 0,
    strength: 0
};

// selecting the class with roll_dice in html
const buttons = document.querySelectorAll('.roll_dice');

// adding event listener to button clicks
buttons.forEach(button => {
    button.addEventListener('click', () => {
      const rolls = 4;
      const keep = 3;
      const diceResult = rollDie(rolls, keep, button);  
      const selector = `#${button.name}-stat`; 
      document.querySelector(selector).value=diceResult   
    });
});


// dice roll functions with disabling
// roll 4 times, keep 3 highest rolls, average results
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
    // const newElement = document.createElement("span");
    // newElement.innerHTML = total;
    // button.insertAdjacentElement("afterend", newElement);
    
    button.setAttribute("disabled", true);
    let stat = button.getAttribute("name");
    results[stat] = total;

    return total;   
}

// disabling check boxes after 2 clicks
const skillForms = document.querySelectorAll('.skill-form');
console.log(skillForms)


skillForms.forEach((skillForm) => {
    const skillCheckboxes = skillForm.querySelectorAll('input[type=checkbox]');
    let selectedCount = 0;
    console.log(skillCheckboxes);
    console.log("hi");

    skillCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => {
            if (selectedCount === 1) {
                skillCheckboxes.forEach((cb) => {
                    if (!cb.checked) {
                        cb.setAttribute('disabled', true);
                    }
                });
            } else {
                selectedCount += 1;
            }
        });
    });
});