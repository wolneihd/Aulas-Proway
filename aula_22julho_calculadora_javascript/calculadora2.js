'use strict'

var valor_tela = '';
var valor_01;
var valor_02;
var operacao;

// operações matemáticas:
function somar() {
    operacao = '+';
    if (valor_01 == undefined) {
        valor_01 = $('#valor').val()
        $('#tela-provisoria').text(`${valor_01} + `);
        valor_tela = '';
        $('#valor').val('');
    } else {
        valor_02 = $('#valor').val();
        var resultado = parseInt(valor_01) + parseInt(valor_02);
        if (valor_02 != '') {
            $('#tela-provisoria').text(`${valor_01} ${operacao} ${valor_02} = ${resultado}`);
            valor_tela = '';
            valor_01 = resultado;
            $('#valor').val(valor_tela);
        } else {
            $('#tela-provisoria').text(`${valor_01} + `);
        }
    }
}

function subtrair() {
    operacao = '-';
    if (valor_01 == undefined) {
        valor_01 = $('#valor').val()
        $('#tela-provisoria').text(`${valor_01} - `);
        valor_tela = '';
        $('#valor').val('');
    } else {
        valor_02 = $('#valor').val();
        var resultado = parseInt(valor_01) - parseInt(valor_02);
        if (valor_02 != '') {
            $('#tela-provisoria').text(`${valor_01} ${operacao} ${valor_02} = ${resultado}`);
            valor_tela = '';
            valor_01 = resultado;
            $('#valor').val(valor_tela);
        } else {
            $('#tela-provisoria').text(`${valor_01} - `);
        }
    }
}

function multiplicar() {
    operacao = '*';
    if (valor_01 == undefined) {
        valor_01 = $('#valor').val()
        $('#tela-provisoria').text(`${valor_01} x `);
        valor_tela = '';
        $('#valor').val('');
    } else {
        valor_02 = $('#valor').val();
        var resultado = parseInt(valor_01) * parseInt(valor_02);
        if (valor_02 != '') {
            $('#tela-provisoria').text(`${valor_01} x ${valor_02} = ${resultado}`);
            valor_tela = '';
            valor_01 = resultado;
            $('#valor').val(valor_tela);
        } else {
            $('#tela-provisoria').text(`${valor_01} x `);
        }
    }
}

function dividir() {
    operacao = '/';
    if (valor_01 == undefined) {
        valor_01 = $('#valor').val()
        $('#tela-provisoria').text(`${valor_01} / `);
        valor_tela = '';
        $('#valor').val('');
    } else {
        valor_02 = $('#valor').val();
        if (parseInt(valor_02) == 0) {
            alert('Não é possível dividir por zero!')
            limpar();
        } else {
            valor_02 = $('#valor').val();
            var resultado = parseInt(valor_01) / parseInt(valor_02);
            if (valor_02 != '') {
                $('#tela-provisoria').text(`${valor_01} ${operacao} ${valor_02} = ${resultado}`);
                valor_tela = '';
                valor_01 = resultado;
                $('#valor').val(valor_tela);
            } else {
                $('#tela-provisoria').text(`${valor_01} / `);
            }
        }
    }
}

function limpar() {
    $('#valor').val('');
    valor_01 = undefined;
    $('#tela-provisoria').text('');
    valor_tela = '';
    operacao = '';
}

function resultado() {
    valor_02 = $('#valor').val();
    if (valor_02 == '') {
        console.log('campo vazio')
        alert('Campo vazio, impossivel fazer a conta!');
        limpar()
    }
    switch (operacao) {
        case '+':
            var resultado = parseInt(valor_01) + parseInt(valor_02);
            $('#tela-provisoria').text(`${valor_01} ${operacao} ${valor_02} = ${resultado}`);
            $('#valor').val('');
            valor_tela = '';
            valor_01 = resultado;
            break;
        case '-':
            var resultado = parseInt(valor_01) - parseInt(valor_02);
            $('#tela-provisoria').text(`${valor_01} ${operacao} ${valor_02} = ${resultado}`);
            $('#valor').val('');
            valor_01 = resultado;
            valor_tela = '';
            break;
        case '*':
            var resultado = parseInt(valor_01) * parseInt(valor_02);
            $('#tela-provisoria').text(`${valor_01} x ${valor_02} = ${resultado}`);
            $('#valor').val('');
            valor_01 = resultado;
            valor_tela = '';
            break;
        case '/':
            if (parseInt(valor_02) == 0) {
                alert('Não é possível dividir por zero!')
                limpar();
            } else {
                var resultado = parseInt(valor_01) / parseInt(valor_02);
                $('#tela-provisoria').text(`${valor_01} ${operacao} ${valor_02} = ${resultado}`);
                $('#valor').val('');
                valor_01 = resultado;
                valor_tela = '';
            }
            break;
    }

}

// PEGA VALORES DOS BOTÕES:

function getValue_1() {
    valor_tela = valor_tela + '1';
    $('#valor').val(valor_tela);
}

function getValue_2() {
    valor_tela = valor_tela + '2';
    $('#valor').val(valor_tela);
}

function getValue_3() {
    valor_tela = valor_tela + '3';
    $('#valor').val(valor_tela);
}

function getValue_4() {
    valor_tela = valor_tela + '4';
    $('#valor').val(valor_tela);
}

function getValue_5() {
    valor_tela = valor_tela + '5';
    $('#valor').val(valor_tela);
}

function getValue_6() {
    valor_tela = valor_tela + '6';
    $('#valor').val(valor_tela);
}

function getValue_7() {
    valor_tela = valor_tela + '7';
    $('#valor').val(valor_tela);
}

function getValue_8() {
    valor_tela = valor_tela + '8';
    $('#valor').val(valor_tela);
}

function getValue_9() {
    valor_tela = valor_tela + '9';
    $('#valor').val(valor_tela);
}

function getValue_0() {
    valor_tela = valor_tela + '0';
    $('#valor').val(valor_tela);
}