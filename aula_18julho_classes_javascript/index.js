const { soma, subtrai, multiplicar, dividir } = require('./calculos')

var retorno = soma(10,20);
console.log('soma',retorno);

retorno = subtrai(20,10);
console.log('subtrai',retorno);

retorno = multiplicar(10,10);
console.log('multiplica',retorno);

retorno = dividir(10,1);
console.log('dividir',retorno)

try {
    var n1 = 10;
    var n2 = 1;
    if (n2 == 0 ) {
        throw new Error ('Não é possível dividir por zero!')
    } else {
        console.log('Divisão (try/catch)', n1/n2)
    }

} catch (erro) {
    console.log(erro.message)
}