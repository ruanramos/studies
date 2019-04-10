function matrixElementsSum(matrix) {
    total = 0;
    var columns = [];
    for (var i = 0; i < matrix.length; i++) {
    	for (var j = 0; j < matrix[i].length; j++) {
    		if(matrix[i][j] == 0) {
    				columns.push(j);
    		}
    		else {
    			if(!columns.includes(j)) {
    				total += matrix[i][j];
    			}
    		}
    	}
        console.log(columns);
    }
    return total;
}
