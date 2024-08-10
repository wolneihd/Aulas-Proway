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
    var mostrarTexto = document.getElementById('mostrarTexto') as HTMLDivElement;
    if (input_nome) {
        console.log(input_nome);
        mostrarTexto.innerHTML = `Seu nome é ${input_nome.value}`;
    } else {
        mostrarTexto.innerHTML = `Campo nome está vazio!`;
    }
};

function validar(): void {
    var htmlInput = document.getElementById('numero') as HTMLInputElement;
    var container = document.getElementById('resultado') as HTMLDivElement;
    var numero = Number(htmlInput?.value);
    if (numero % 2 == 0) {
        container.innerHTML = `Este número ${numero} é par!`;
        container.style.backgroundColor = 'green';
        container.style.textAlign = 'right';
        container.style.fontSize = '35px';
    } else {
        container.innerHTML = `Este número ${numero} é impar!`;
        container.style.backgroundColor = 'red';
        container.style.textAlign = 'left';
        container.style.fontSize = '35px';
    }
}