// exercicio 01

function somar() {
    var num1 = parseInt($('#num1').val());
    var num2 = parseInt($('#num2').val());
    console.log(typeof num1, typeof num2);
    var query = 'O resultado da soma é ' + (num1 + num2) + '.';
    $('#resultado').text(query);
}

// exercicio 02

function parImpar() {
    var numero = parseInt($('#numero').val());
    if (numero % 2 == 0) {
        $('#resultado_02').text("O número é par.");
        //console.log('par');
    } else {
        $('#resultado_02').text("O número é ímpar.");
        //console.log('impar');
    }

}

// exercicio 03

function converter() {
    var celcius = parseInt($('#temperatura').val());
    var fahrenheit = (celcius * (9 / 5)) + 32;
    var query = `A conversão de ${celcius} °C em Fahrenheit é ${fahrenheit} °F.`
    $('#tempConvertido').text(query);
}

// Estelização via Jquery

$('.exercicio').css({ "border-weight": "1px", "border-style": "solid", "padding": "10px", "border-radius": "10px", 'margin': "10px", 'font-size': '25px'});
$('.titulo').css({ "background-color": "lightgray", "padding": "10px", "border-radius": "8px" , "text-align": 'center','font-weight':'bold'});
$('.botao').css({ "background-color": "#007bff", 'color':'white', "border-radius": "8px", "height": "40px", "width": "200px", 'font-size': '30px' });
$('.botao').hover(
    function(){$(this).css({"background-color": "#0056b3"})}, 
    function(){$(this).css({"background-color": "#007bff"})}
);
$('.input').css({ "border-radius": "8px", "height": "40px", "width": "150px", 'font-size': '30px' });