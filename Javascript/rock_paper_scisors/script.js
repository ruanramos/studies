function computerPlay() {
    const v = Math.floor(Math.random() * 3)
    switch(v) {
        case 0:
            return "rock"
        case 1:
            return "paper"
        case 2:
            return "scisors"
    }
}

function result(player, comp) {
    if (player === "rock" && comp === "rock" || player === "paper" && comp === "paper" || player === "scisors" && comp === "scisors") return "It's a draw!"
    if (player === "rock" && comp === "paper" || player === "paper" && comp === "scisors" || player === "scisors" && comp === "rock") return "You lost!"
    if (player === "rock" && comp === "scisors" || player === "paper" && comp === "rock" || player === "scisors" && comp === "paper") return "You won!"
}

function giveResult(player) {
    const h1 = document.querySelector("h1");
    const comp = computerPlay()
    const r = result(player, comp)
    h1.innerHTML = "You: " + player + "<br>Computer: " + comp + "<br>" + r;
    const playAgainButton = document.createElement('button');
    playAgainButton.innerHTML = "Play Again";
    playAgainButton.addEventListener('click', Play);
    var btns = document.getElementsByClassName("bt");
    
    while(btns.length > 0) {
        btns[0].parentNode.removeChild(btns[0]);
    }

    const container = document.getElementById("container");
    container.appendChild(playAgainButton);
}

function Play() {
    const h1 = document.querySelector("h1");
    h1.innerHTML = "Choose:"
    setPlayerTurn();
}

function setComputerTurn() {
    const h1 = document.querySelector("h1");
    h1.innerHTML = "Computer played " + computerPlay();
    setPlayerTurn();
}

function setPlayerTurn() {
    const rockButton = document.createElement('button');
    rockButton.innerHTML = "rock";
    rockButton.setAttribute("class", "bt");
    const paperButton = document.createElement('button');
    paperButton.innerHTML = "paper";
    paperButton.setAttribute("class", "bt");
    const scisorsButton = document.createElement('button');
    scisorsButton.innerHTML = "scisors";
    scisorsButton.setAttribute("class", "bt");
    const container = document.getElementById('container');
    container.removeChild(container.children[1]);
    container.appendChild(rockButton);
    container.appendChild(paperButton);
    container.appendChild(scisorsButton);
    rockButton.addEventListener('click', function() {
        giveResult("rock");
    });
    paperButton.addEventListener('click', function() {
        giveResult("paper");
    });
    scisorsButton.addEventListener('click', function() {
        giveResult("scisors");
    });
}