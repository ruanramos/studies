function isInfiniteProcess(a, b) {
    if((b-a) % 2 == 0 && b >= a) return false;
    return true;
}
