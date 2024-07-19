// EXERCICIO 01

//--- opção 01
var pessoa = {
    nome: 'Pedro',
    sobrenome: 'Henrique',
    mostrarNome: function() {
        return this.nome + ' ' + this.sobrenome;
    }
}

console.log(pessoa.mostrarNome());

//--- opção 02
function nomeCompleto(nome, sobrenome) {
    return nome + ' ' + sobrenome;
}

console.log(nomeCompleto('Wolnei', 'Dircksen'));

// EXERCICIO 02

function validarIdade(idade){
    if (idade >= 18) {
        console.log('Esta pessoa é MAIOR de idade!')
    } else {
        console.log("Esta pessoa é MENOR de idade!")
    }
}

validarIdade(5);
validarIdade(21);
validarIdade(18);

// EXERCICIO 03

function aumentoSalaria(salario, aumento) {
    return salario + aumento;
}

var novo_salario = aumentoSalaria(3200,500);
console.log(novo_salario);

// EXERCICIO 04

function faturamentoBruto(valor_unitario, qtd_vendas) {
    return 'Seu fatumaneto foi de ', valor_unitario * qtd_vendas;
}

total_vendas = faturamentoBruto(2.5,250);
console.log(total_vendas);