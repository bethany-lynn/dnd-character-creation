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

}

const buttons = document.querySelectorAll('.roll_dice');
let results = {};

buttons.forEach(button => {
    button.addEventListener('click', () => {
      const rolls = 4;
      const keep = 3;
      rollDie(rolls, keep, button);
    });
  });

function saveResults() {
    const jsonString = JSON.stringify(results);
    console.log(jsonString)
}



// may need to edit or remove lines:
// 12, 15, 16, 31, 32, 33, etc