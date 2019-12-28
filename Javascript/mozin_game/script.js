var turn = 0;


function initDivs() {
    for (let index = 0; index < 3; index++) {
        createLine(index);
    }
}

function createLine(number) {
    const newLine = document.createElement('div');
    newLine.classList.add('line')
    const container = document.getElementById("container");
    
    for (let index = 0; index < 3; index++) {
        const newDiv = document.createElement('div');
        newDiv.classList.add("div");
        newDiv.style.height = "300px";
        if (number === 0) {
            newDiv.setAttribute("id", 'top-line');
        } else if (number === 2) {
            newDiv.setAttribute("id", 'bottom-line');
        }
        newDiv.addEventListener('mouseover', function() {
            changeColor(this, "lightgreen");
        })
        newDiv.addEventListener('mouseleave', function() {
            changeColor(this, "white");
        })
        newDiv.addEventListener('click', function() {
            clickHandler(turn, newDiv);
        })
        if (index === 1) {
            newDiv.classList.add('center-column');
        }
        newLine.appendChild(newDiv);
        container.appendChild(newLine);
    }
}

function changeColor(div, color) {
    div.style.backgroundColor  = color;
}

function clickHandler(t, div) {
    if (t % 2 === 0) {
        const imgRuan = document.createElement('IMG');
        imgRuan.setAttribute('src', 'ruan.jpeg');
        imgRuan.setAttribute('id', 'image');
        div.appendChild(imgRuan);
    } else {
        const imgMozin = document.createElement('IMG');
        imgMozin.setAttribute('src', 'mozin.jpg');
        imgMozin.setAttribute('id', 'image');
        div.appendChild(imgMozin);
    }
    turn++;
}

initDivs();