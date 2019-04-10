function phoneCall(min1, min2_10, min11, s) {
    var total = 0;
    if(s - min1 > 0) {
        total += 1;
        s -= min1;
    }
    if(s - 9*min2_10 > 0) {
        total += 9;
        s -= 9*min2_10;
    } else {
        total += Math.floor(s / min2_10);
        s -= Math.floor(s / min2_10) * min2_10;
        return total;
    }
    total += Math.floor(s / min11);
    return total;
}
