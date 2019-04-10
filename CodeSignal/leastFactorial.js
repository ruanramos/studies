function leastFactorial(n) {
	for (var m = 1; m <= n; m++) {
		k = fac(m);
		if(k >= n) return k;
	}
}

function fac(n) {
	if(n <= 1) return 1;
	return fac(n-1) * n;
}