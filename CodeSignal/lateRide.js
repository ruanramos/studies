function lateRide(n) {
    var hora;
    var minuto;
    hora = Math.floor(n/60);
    minuto = n%60;
    return Math.floor(hora / 10) + hora % 10 + Math.floor(minuto / 10) + minuto % 10
}
