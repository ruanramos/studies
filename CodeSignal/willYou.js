function willYou(young, beautiful, loved) {
	if( (young && beautiful && !loved) || (young && beautiful && loved) ||
	 (loved && !young && !beautiful) || (loved && young && !beautiful) || (loved && !young && !beautiful) 
	 || (loved && !young && beautiful)) {
		return false;
	}
	return true;
}
