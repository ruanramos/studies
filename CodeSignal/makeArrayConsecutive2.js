function compararNumeros(a, b) {
  return a - b;
}

function makeArrayConsecutive2(statues) {
    statues = statues.sort(compararNumeros);
    var total = 0;
    for (var i = 0; i < statues.length-1; i++) {
    	if(statues[i] + 1 != statues[i+1]) {
    		total += statues[i+1] - statues[i] - 1;
    		console.log(total);
    	}
    }
    return total;
}


