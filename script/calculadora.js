function calc_total() {
    var piOrig = parseInt(document.getElementById('piorig').value);
    var corOrig = parseInt(document.getElementById('cororig').value);
    var velOrig = parseInt(document.getElementById('velorig').value);
    var piaoAt = parseInt(document.getElementById('piaoat').value);
    var coroaAt = parseInt(document.getElementById('corat').value);
    velAt = ((velOrig / (piOrig / corOrig)) * (piaoAt / coroaAt)).toFixed(2);
    document.getElementById('velat').value = velAt;
}
