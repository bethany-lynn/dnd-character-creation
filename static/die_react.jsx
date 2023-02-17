function getRandomNum(upperLimit) {
    return Math.ceil(Math.random() * upperLimit);
  }

function Die(props) {
    const [diceValue, setDiceValue] = React.useState(' ');
  
    function roll() {
      const rollResult = getRandomNum(props.sides);
      setDiceValue(rollResult);
    }
  
    return (
      <button type="button" className="die" onClick={roll}>
        <i>{props.sides}</i><br/>
        <b>{diceValue}</b>
      </button>
    );
  }

ReactDOM.render(
    <div>
        <Die sides="4" />
        <Die sides="6" />
        <Die sides="8" />
        <Die sides="10" />
        <Die sides="12" />
        <Die sides="20" />
        <Die sides="100" />
    </div>, 
    document.querySelector('#root')
);