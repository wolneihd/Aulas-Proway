// exemplo 01
function dizerOla() {
    console.log('Void não ter RETURN');
}
dizerOla();
// exemplo 02
var nombre = 'Wolnei Hellmann Dircksen';
function nomeCompleto(nombre) {
    return "Seu nome completo \u00E9 ".concat(nombre);
}
console.log(nomeCompleto(nombre));
// exemplo 03
function obterMes11() {
    return 'Novembro';
}
console.log(obterMes11());
// exemplo 04
function somar(a, b) {
    return a + b;
}
console.log(somar(10, 20));
// exemplo 05
function boasVindas(escola) {
    if (escola) {
        console.log("Bem vindo a ".concat(escola, "!"));
    }
    else {
        console.log('Bem vindo!');
    }
}
boasVindas('SENAI');
boasVindas();
// exemplo 06
function elevarNumero(a, b) {
    if (b === void 0) { b = 2; }
    return Math.pow(a, b);
}
console.log(elevarNumero(2));
console.log(elevarNumero(2, 3));
