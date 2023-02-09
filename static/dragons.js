// dice roll functions with disabling
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
    let stat = button.getAttribute("name");
    results[stat] = total;

    // results[stat] = total;
    // sessionStorage.setItem('results', JSON.stringify(results));
    fetch('http://localhost:5000/save_results', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(results)
    })
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error(error));
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

// event listener for skills check boxes
// const skillForms = document.querySelectorAll('.skill-form');
// console.log(skillForms)


// skillForms.forEach((skillForm) => {
//     const skillCheckboxes = skillForm.querySelectorAll('input[type=checkbox]');
//     let selectedCount = 0;
//     console.log(skillCheckboxes);
//     console.log("hi");

//     skillCheckboxes.forEach((checkbox) => {
//         checkbox.addEventListener('change', (event) => {
//             if (selectedCount === 2) {
//                 skillCheckboxes.forEach((cb) => {
//                     if (!cb.checked) {
//                         cb.setAttribute('disabled', true);
//                     }
//                 });
//             } else {
//                 selectedCount += 1;
//             }
//         });
//     });
// });
