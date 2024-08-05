var nomes = ["Bob"];
nomes.push("Patrick");
nomes.push("Antony");
nomes.pop();
// imprimir dados
for (var i = 0; i < nomes.length; i++) {
    console.log(nomes[i]);
}
var dados = ["Wolnei", 32, false];
// imprimir dados
for (var i = 0; i < dados.length; i++) {
    console.log("".concat(i, " ").concat(dados[i], " ").concat(typeof (dados[i])));
}
var elemento = [55, "Robert", false];
// imprimir dados
for (var i = 0; i < elemento.length; i++) {
    console.log("".concat(i, " ").concat(elemento[i], " ").concat(typeof (elemento[i])));
}
