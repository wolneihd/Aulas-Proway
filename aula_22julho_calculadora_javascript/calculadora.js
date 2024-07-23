'use strict'

function somar() {
    var valor_01 = parseFloat($('#valor_01').val());
    var valor_02 = parseFloat($('#valor_02').val());
    var resultado = valor_01 + valor_02;
    $('#resultado').text(resultado);
}

function subtrair() {
    var valor_01 = parseFloat($('#valor_01').val());
    var valor_02 = parseFloat($('#valor_02').val());
    var resultado = valor_01 - valor_02;
    $('#resultado').text(resultado);
}

function multiplicar() {
    var valor_01 = parseFloat($('#valor_01').val());
    var valor_02 = parseFloat($('#valor_02').val());
    var resultado = valor_01 * valor_02;
    $('#resultado').text(resultado);
}

function dividir() {
    var valor_01 = parseFloat($('#valor_01').val());
    var valor_02 = parseFloat($('#valor_02').val());
    if (valor_02 == 0) {
        $('#resultado').text(`Não é possível dividir ${valor_01} por zero!`);
    } else {
        var resultado = valor_01 / valor_02;
        $('#resultado').text(resultado);
    }    
}

function limpar_tela() {
    $('#valor_01').val('');
    $('#valor_02').val('');
}