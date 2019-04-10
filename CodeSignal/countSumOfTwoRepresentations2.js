function countSumOfTwoRepresentations2(n, l, r) {
	var qnt = 0;
	for (var i = l; i <= r; i++) {
		for (var j = l; j <= r ; j++) {
			if(i + j == n && i >= j) {
				qnt++;
                console.log(i, j);
			}
		}
	}
	return qnt;
}
