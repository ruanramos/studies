function killKthBit(n, k) {
  var res = 0;
  var a = parseInt(n, 10).toString(2)
  a[k-1] = 0
  for (var i = a.length - 1; i >= 0; i--) {
  	res += a[i] * Math.pow(2, (a.length - 1) - i);
  }
  return res;
}