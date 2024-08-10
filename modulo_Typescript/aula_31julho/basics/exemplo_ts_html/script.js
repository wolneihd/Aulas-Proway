// função sem parametro e retorno:
function exibirAlerta() {
    alert('Alerta exibido com sucesso!');
}
// funcção com parâmetro de retorno:
function exibirNome() {
    // opção 01
    var usuario = document.getElementById('nome');
    alert("Usu\u00E1rio ativo: ".concat(usuario.value));
    // opção 02 >> imprime no body o valor do input.
    var input_nome = document.querySelector('#nome');
    var mostrarTexto = document.getElementById('mostrarTexto');
    if (input_nome) {
        console.log(input_nome);
        mostrarTexto.innerHTML = "Seu nome \u00E9 ".concat(input_nome.value);
    }
    else {
        mostrarTexto.innerHTML = "Campo nome est\u00E1 vazio!";
    }
}
;
function validar() {
    var htmlInput = document.getElementById('numero');
    var container = document.getElementById('resultado');
    var numero = Number(htmlInput === null || htmlInput === void 0 ? void 0 : htmlInput.value);
    if (numero % 2 == 0) {
        container.innerHTML = "Este n\u00FAmero ".concat(numero, " \u00E9 par!");
        container.style.backgroundColor = 'green';
        container.style.textAlign = 'right';
        container.style.fontSize = '35px';
    }
    else {
        container.innerHTML = "Este n\u00FAmero ".concat(numero, " \u00E9 impar!");
        container.style.backgroundColor = 'red';
        container.style.textAlign = 'left';
        container.style.fontSize = '35px';
    }
}
