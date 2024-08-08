var nomes = ["Bob"];
nomes.push("Patrick");
nomes.push("Antony", "Jack");
nomes.pop(); // remove o último elemento
nomes.shift(); // remove o primeiro elemento 
nomes.unshift("Harry", "Jim"); // insere no inicio do array
// imprimir dados
for (var i = 0; i < nomes.length; i++) {
    console.log("".concat(i, " ").concat(nomes[i]));
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
// objeto
var person = {
    firstName: "John",
    lastName: "Doe",
    id: 5566,
    fullName: function () {
        return "Name: ".concat(this.firstName, " ").concat(this.lastName);
    }
};
console.log(person.fullName());
// Exemplo FOR
var harryPotter = ["Harry", "Hermione", "Rony", "Draco", "Luna", "Hermione"];
var posicaoArray = [];
for (i = 0; i < harryPotter.length; i++) {
    if (harryPotter[i] === "Hermione") {
        posicaoArray.push(i);
    }
}
console.log("Hermione[for]: ".concat(posicaoArray));
// Exemplo FOR-EACH
var posicaoArray_2 = [];
harryPotter.forEach(function (nome, pos) {
    if (nome === "Hermione") {
        posicaoArray_2.push(pos);
    }
});
console.log("Hermione[forEach]: ".concat(posicaoArray_2));
// outro exemplo forEach
function exibirNome(nome, pos) {
    console.log("- ".concat(nome, " esta na posicao ").concat(pos));
}
harryPotter.forEach(exibirNome);
// Quantidade de Hermione:
var quantidadeHermione = 0;
var posicaoHermione = [];
harryPotter.forEach(function (nome, pos) {
    if (nome === "Hermione") {
        quantidadeHermione++;
        posicaoHermione.push(pos);
    }
});
console.log("Quantidade nomes Hermione: ".concat(quantidadeHermione, " - nas posi\u00E7\u00F5es: ").concat(posicaoHermione.toString(), "."));
