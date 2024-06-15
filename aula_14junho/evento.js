'use strict'

$(document).ready(function () {
    $('#botao').click(function (event) {
        //event.preventDefault();
        $('#mensagem').text('Botão clicado!');
    });
});

$('#texto').keydown(function (event) {
    if (event.key === 'Enter') {
        var texto = $('#texto').val();
        $('#inputTexto').text(texto);
    }
});

$('#texto').focus(function (event) {
    $(this).css('background-color', 'lightgray');
});

$('#texto').blur(function (event) {
    $(this).css('background-color', 'white');
});

