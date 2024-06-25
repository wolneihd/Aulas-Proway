'use strict'

$(document).ready(function(){
    var botao = $('#botao');
    var piada = $('#piada');
    
    botao.click(function(){
        var apiUrl = 'https://v2.jokeapi.dev/joke/Any?lang=pt';
        
        $.ajax({
            url: apiUrl,
            type: 'GET',
            success: function(dados) {
                piada.html(`<p>${dados.setup} <br>${dados.delivery}</p>`);
            },
            error: function() {
                piada.html(`<p>Não foi possível consultar a API!</p>`);
            }
        })
    })
});