// usando javascript:
var titulo = document.getElementById('titulo').innerHTML;
console.log(titulo);

// usando jquery:
var tituloJquery = $('#titulo').text();
console.log(tituloJquery);

//var paragrafo = $('#paragrafo').text();
//console.log(paragrafo);

function imprimeNome() {
    // .val() pra usar em input
    var nome = $('#nome').val();
    console.log(nome);  
    $("#titulo").css({"background-color": "yellow", 'color': 'blue'});
}

$(document).ready(function(){
    $('#dataNascimento').datepicker();
})

// escrevendo valor no html
$('#saida').text('Oi mundo') 