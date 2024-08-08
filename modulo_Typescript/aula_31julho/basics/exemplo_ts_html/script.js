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
    if (input_nome) {
        var newElement = document.createElement('p');
        newElement.textContent = input_nome.value;
        document.body.appendChild(newElement);
    }
    else {
        console.error('Não foi possível encontrar os elementos especificados.');
    }
}
;
function validar() {
    var htmlInput = document.querySelector('#numero');
    var container = document.getElementById('resultado');
    var numero = Number(htmlInput === null || htmlInput === void 0 ? void 0 : htmlInput.value);
    if (numero % 2 == 0) {
        var newElement = document.createElement('p');
        newElement.textContent = String(numero);
        container.innerHTML = "Este n\u00FAmero ".concat(numero, " \u00E9 par!");
        console.log('teste');
    }
    else {
        console.log('impar');
    }
}
