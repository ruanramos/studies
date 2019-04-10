function knapsackLight(value1, weight1, value2, weight2, maxW) {
	var greater, lower, total = 0;
	var wei1, wei2;
	if(value1 > value2) {
		greater = value1;
		lower = value2;
		wei1 = weight1;
		wei2 = weight2;
	}
	else {
		greater = value2;
		lower = value1;
		wei1 = weight2;
		wei2 = weight1;
	}
	if(maxW - wei1 >= 0) {
		maxW -= wei1;
		total += greater;
	}
	if(maxW - wei2 >= 0) {
		total += lower;
	}
	return total;
}
