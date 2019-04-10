function metroCard(lastNumberOfDays) {
	if(lastNumberOfDays == 30 || lastNumberOfDays == 28) {
		return [31];
	}
	else if(lastNumberOfDays == 31) {
		return [28, 30, 31];
	}
}