function almostIncreasingSequence(sequence) {
	var sequence1, sorted;
	var copy = sequence.slice(0);
	for (var i = 0; i < copy.length-1; i++) {
		if(copy[i] >= copy[i+1]) {
			var copy2 = copy.slice(0);
			copy2.splice(i, 1);
			for (var j = 0; i < copy2.length-1; i++) {
				if(copy2[j] >= copy2[j+1]) {
					return false;
				}
			}
		}
	}
	return true;
}
/*
	for (var i = 0; i < sequence.length; i++) {
		sequence1 = sequence.slice(0);
		sequence1.splice(i,1);
		for (var j = 0; j < sequence1.length-1; j++) {
			if(sequence1[j] >= sequence1[j+1]) {
				break;
			}
		}
		if(j === sequence1.length-1) return true;
	}
	return false;
}

function compare(a, b) {
    return a-b;
}*/