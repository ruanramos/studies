function test() {
    var a = document.getElementById("a");
    console.log(a);

    var btn = document.getElementById("button");
    btn.addEventListener("click", function() {
        a.innerHTML = "CLICOU NÉ SAFADO";
    });
}

test();