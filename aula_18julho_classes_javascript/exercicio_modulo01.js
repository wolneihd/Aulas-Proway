// Exercicio 01

function nomeCompleto(nome, sobrenome) {
    console.log(nome + ' ' + sobrenome);
    console.log(`${nome} ${sobrenome}`)
}

// Exercicio 02

function validarIdade(idade) {
    if (idade >= 18) {
        console.log('Esta pessoa é MAIOR de idade!')
    } else {
        console.log("Esta pessoa é MENOR de idade!")
    }
}

// Exericio 03

function aumentoSalarial(salario, aumento) {
    // aumento em %
    converterPorcentagem = 1 + (aumento / 100);
    console.log(`Seu salário R$ ${salario} com ${aumento}% de aumento é agora R$`, salario * converterPorcentagem);
}

// Exericio 04

function faturamentoBruto(valor_produto, qtd_vendas) {
    console.log(`Valor unitário: ${valor_produto} - Total de vendas: ${qtd_vendas}`);
    console.log('Seu faturamento foi de R$', valor_produto * qtd_vendas);
}

// Exportando os módulos:

module.exports = { nomeCompleto, validarIdade, aumentoSalarial, faturamentoBruto }