'use strict'

$(document).ready(function() {
    var botao  = $('#botao');
    var infoUsuario = $('#infoUsuario');

    botao.click(function() {
        // atrelando função no click do botão:
        // infoUsuario.append('<p>teste</p>');

        var numero = parseInt($('#numero').val());
        var apiUrl = `https://jsonplaceholder.typicode.com/users/${numero}`;

        $.ajax({
            url: apiUrl,
            type: 'GET',
            success: function(dados) {
                console.log(dados);
                infoUsuario.html(`<p>${dados.name} is from ${dados['address'].city}.</p>`);
            },
            error: function() {
                alert('Impossível fazer a requisição de API!')
            }
        });

        
    })
});