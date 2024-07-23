// exemplo FOR
for (i=0;i<10;i++){
    console.log(i, 'for');
}

// exemplo WHILE
var numero = 0;
while (true) {
    console.log(numero, 'while');
    numero++;
    if (numero == 10) {
        break;
    }
}

// exemplo SWITCH:
var opcao = parseInt(prompt("Digite o valor"))
console.log(opcao, typeof opcao, 'switch case')
switch (opcao) {
    case 1:
        console.log('Você digitou 1');
        break;
    case 2:
        console.log('Você digitou 2');
        break;
    default:
        console.log('Você digitou outra coisa');
}