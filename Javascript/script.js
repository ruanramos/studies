var send_button = document.querySelector("#send_button");
var add_elem_button = document.querySelector("#add_elem_button");
var input_name = document.querySelector("#name");
var p = document.createElement("p");
p.setAttribute("class", "row justify-content-md-center")
var imagesDiv = document.createElement("div");
imagesDiv.setAttribute("class", "col-12");

var count = 0;

if (send_button != null) {
    send_button.addEventListener("click", function () {
        alert("video was added!!!!!!!!");
    });
}

if (add_elem_button != null) {
    add_elem_button.addEventListener("click", clickAndAdd);
}


function clickAndAdd() {
    count++;
    var name = input_name.value.toLowerCase();
    console.log("Count was added! now equals to " + count)

    if (count == 1) {
        document.body.appendChild(p);
        p.textContent = count + " mozin";
        document.body.appendChild(imagesDiv);

    }

    if (input_name != null) {
        if (name.includes("dani")) {
            p.textContent = count + " mozin";
            var img = document.createElement("img");
            img.setAttribute("src", "dani1.jpg");
            img.setAttribute("class", "col-md-auto");
            imagesDiv.appendChild(img);
        }
        else if (name.includes("mozin")) {
            p.textContent = count + " mozin";
            var img = document.createElement("img");
            img.setAttribute("src", "dani2.jpg");
            img.setAttribute("class", "col-md-auto");
            imagesDiv.appendChild(img);
            img.addEventListener("click", function () {
                alert("NÃO FALA COMIGO");
            })
        }
    }
}

