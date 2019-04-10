function adjacentElementsProduct(inputArray) {
	var greater = Number.MIN_SAFE_INTEGER;
	var res;	
	for (var i = 0; i < inputArray.length-1; i++) {
		var num1 = inputArray[i];
		var num2 = inputArray[i+1];
		res = num1 * num2;
		if(res > greater) {
			greater = res;
		}
	}
}
