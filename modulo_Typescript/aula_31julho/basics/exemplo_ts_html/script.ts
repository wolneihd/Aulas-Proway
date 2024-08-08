// função sem parametro e retorno:
function exibirAlerta(): void {
    alert('Alerta exibido com sucesso!');
}

// funcção com parâmetro de retorno:
function exibirNome(): void {
    // opção 01
    const usuario = document.getElementById('nome') as HTMLInputElement;
    alert(`Usuário ativo: ${usuario.value}`)

    // opção 02 >> imprime no body o valor do input.
    const input_nome = document.querySelector<HTMLInputElement>('#nome');
    if (input_nome) {
        const newElement = document.createElement('p');
        newElement.textContent = input_nome.value;
        document.body.appendChild(newElement);
    } else {
        console.error('Não foi possível encontrar os elementos especificados.');
    }
};

function validar(): void {
    var htmlInput = document.querySelector<HTMLInputElement>('#numero');
    var container = document.getElementById('resultado') as HTMLDivElement;
    var numero = Number(htmlInput?.value);
    if (numero % 2 == 0) {
        const newElement = document.createElement('p');
        newElement.textContent = String(numero);
        container.innerHTML = `Este número ${numero} é par!`;
        console.log('teste');
    } else {
        console.log('impar')
    }
}