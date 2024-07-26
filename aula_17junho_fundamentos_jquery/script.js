'use strict'

$(document).ready(function(){
    $('#addParagrafo').click(function(){
        var paragrafo = $('<p>Novo Parágrafo</p>')
        paragrafo.attr({
            'class':'novo_elemento',
            'id': 'elemento_novo'
        })
        $('#conteudo').append(paragrafo);
    })
    $('#addTitulo').click(function(){
        $('#conteudo').append('<h2 class="novo_elemento">Novo Titulo</h2>');
    })
    $('#addDiv').click(function(){
        $('#conteudo').append('<div class="novo_elemento">Nova DIV</div>');
    })
    $('#limparDIV').click(function(){
        $('.novo_elemento').remove();
    })
    $('#buscar').click(function(){
        var numero_pokemon = $('#numero_pokemon').val();
        numero_pokemon = parseInt(numero_pokemon);
        console.log(numero_pokemon, typeof numero_pokemon)
        $('#imagem').attr('src',`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${numero_pokemon}.png`);
    })
});

