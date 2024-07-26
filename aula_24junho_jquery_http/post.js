$(document).ready(function(){
    var botao = $('#botao');
    botao.click(function(){
        $.ajax({
            url: 'https://jsonplaceholder.typicode.com/posts',
            type: 'GET',
            success: function(dados){
                $('#resultado').html(JSON.stringify(dados[0]));
                console.log(dados);
            },
            error: function() {
                alert('Não foi possível consultar a API!')
            }
        })
    })
})