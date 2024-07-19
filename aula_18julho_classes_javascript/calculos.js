function soma(n1,n2){
    return n1+n2;
}

function subtrai(n1,n2){
    return n1-n2;
}

function multiplicar(n1,n2){
    return n1*n2;
}

function dividir(n1,n2){
    if (n2==0) {
        return 'Não é possível dividir por zero!'
    } else {
        return n1/n2;
    }
}

module.exports = {soma, subtrai, multiplicar, dividir}

