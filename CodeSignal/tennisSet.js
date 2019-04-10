function tennisSet(score1, score2) {
	if(score1 == 7) {
		if(score2 == 5 || score2 == 6) {
			return true;
		}
	}
	else if(score2 == 7) {
		if(score1 == 5 || score1 == 6) {
			return true;
		}
	}
	else if(score1 == 6) {
		if(score2 <= 4) {
			return true;
		}
	}
	else if(score2 == 6) {
		if(score1 <= 4) {
			return true;
		}
	}
	return false;
}
