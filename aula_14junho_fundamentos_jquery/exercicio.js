// Exercicio 01

$(document).ready(function () {
    $('#btn_exercicio01').click(function (event) {
        $('#texto01').text('Novo Texto Atualizado!');
    });
});

// Exercicio 02

$(document).ready(function () {
    $('#btn_exercicio02').click(function (event) {
        var valor = $('#texto_input_02').val();
        $('#texto02').text(valor);
    });
});

// exericio 03

$(".item_lista").hover(
    function (event) {
        $(this).css('color', 'red');
    }, function () {
        $(this).css('color', 'black');
    }
);

// exericio 04

$('#input_04').focus(function (event) {
    $(this).css('background-color', '#ffffcc');
});

$('#input_04').blur(function (event) {
    $(this).css('background-color', 'white');
});

// Exericio 05

$(document).ready(function() {
    $('#form').submit(function (event) {
        event.preventDefault();
        var valor = $('#texto_05').val();
        $('#mostraValor').text(valor);
        console.log(valor);
    });
});