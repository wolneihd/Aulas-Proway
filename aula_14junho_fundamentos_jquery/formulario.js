'use strict'

$(document).ready(function() {
    $('#dataNascimento').datepicker({
        format: 'dd/mm/yyyy',
        language: 'pt-BR',
        dayNamesMin: ['D','S','T','Q','Q','S','S']
    });

    $('#formulario').submit(function(event){
        event.preventDefault();
        /*
        var nome = $('#nome').val();
        var email = $('#email').val();
        var dataNascimento = $('#dataNascimento').val();
        var pessoa = {
            'nome': nome,
            'email': email,
            'dataNascimento': dataNascimento
        }
        console.log(pessoa.nome);
        console.log(pessoa.email);
        console.log(pessoa.dataNascimento);
        */
        var dadosFormulario = $('#formulario').serialize();
        console.log(dadosFormulario);
    });
});