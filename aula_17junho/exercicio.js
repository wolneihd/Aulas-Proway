'use strict'

$(document).ready(function(){
    $('#addParagrafo').click(function(){
        var paragrafo = $('<p>Novo Parágrafo</p>')
        paragrafo.attr({
            'class':'novo_elemento'
        })
        $('#container').append(paragrafo);
    })

    $('#addh2').click(function(){
        var novo_h2 = $('<h2>Novo H2</h2>')
        novo_h2.attr({
            'class':'novo_elemento'
        })
        $('#container').append(novo_h2);
    })

    $('#calcularAno').click(function(){
        var idade = parseInt($('#idade').val());
        var anoAtual = new Date().getFullYear(); 
        var resposta = $(`<p>Você nasceu em ${anoAtual-idade}!<p>`)
        resposta.attr({
            'class':'novo_elemento'
        })
        $('#container').append(resposta);
    })

    var numero = 0;
    $('#calcularIMC').click(function(){
        var peso = parseFloat($('#peso').val());
        var altura = parseFloat($('#altura').val());
        var imc = peso / (altura * altura);
        var texto_imc = $(`<p class='imc${numero}'>Seu IMC é ${imc.toFixed(2)} - ${textoImc(imc)}!<p>`)
        //$('.imc').text(texto_imc);
        $('.imc').append(texto_imc);
        if (imc < 18.5) {
            $(`.imc${numero}`).css('backgroundColor','red');
        } else if (imc >= 18.5 && imc < 24.9) {
            $(`.imc${numero}`).css('backgroundColor','green');
        } else if (imc >= 25 && imc < 29.9) {
            $(`.imc${numero}`).css('backgroundColor','yellow');
        } else {
            $(`.imc${numero}`).css('backgroundColor','red');
        }
        numero++;
    })
});

function textoImc(imc) {
    if (imc < 18.5) {
        return 'Baixo peso';
    } else if (imc >= 18.5 && imc < 24.9) {
        return 'Peso Saudável';
    } else if (imc > 25 && imc < 29.9) {
        return 'Sobrepeso';
    } else {
        return 'Obesidade';
    }
}

/*
$(document).ready(function () {
    $('#calcula-imc').click(function () {
        $('#resultado-imc').empty()

        var peso = parseFloat($('#peso').val());
        var altura = parseFloat($('#altura').val());

        var imc = peso / (altura * altura);
        imc = imc.toFixed(2)

        var resultadoImc =
            $('<h2>' + imc + '</h2>');

        if (imc < 18.5) {
            resultadoImc.attr('class', 'vermelho')
        } else if (imc >= 18.5 && imc < 25) {
            resultadoImc.attr('class', 'verde')
        } else if (imc >= 25 && imc < 30) {
            resultadoImc.attr('class', 'amarelo')
        } else if (imc >= 30) {
            resultadoImc.attr('class', 'laranja');
        }

        $('#resultado-imc').append(resultadoImc)
    })
});
*/


