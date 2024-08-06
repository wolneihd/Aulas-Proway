const nomes: string[] = ["Bob"];
nomes.push("Patrick");
nomes.push("Antony", "Jack");
nomes.pop()   // remove o último elemento
nomes.shift() // remove o primeiro elemento 
nomes.unshift("Harry", "Jim") // insere no inicio do array
// imprimir dados
for (var i = 0; i < nomes.length; i++) {
    console.log(`${i} ${nomes[i]}`);
}

const dados: [string, number, boolean] = ["Wolnei", 32, false];
// imprimir dados
for (var i = 0; i < dados.length; i++) {
    console.log(`${i} ${dados[i]} ${typeof (dados[i])}`);
}

const elemento: any[] = [55, "Robert", false];
// imprimir dados
for (var i = 0; i < elemento.length; i++) {
    console.log(`${i} ${elemento[i]} ${typeof (elemento[i])}`);
}

// objeto
const person = {
    firstName: "John",
    lastName: "Doe",
    id: 5566,
    fullName: function () {
        return `Name: ${this.firstName} ${this.lastName}`;
    }
};
console.log(person.fullName());

// Exemplo FOR
const harryPotter: string[] = ["Harry", "Hermione", "Rony", "Draco", "Luna", "Hermione"];
var posicaoArray: number[] = [];
for (i = 0; i < harryPotter.length; i++) {
    if (harryPotter[i] === "Hermione") {
        posicaoArray.push(i);
    }
}
console.log(`Hermione[for]: ${posicaoArray}`)

// Exemplo FOR-EACH
var posicaoArray_2: number[] = [];
harryPotter.forEach((nome, pos) => {
    if (nome === "Hermione") {
        posicaoArray_2.push(pos);
    }
})
console.log(`Hermione[forEach]: ${posicaoArray_2}`)

// outro exemplo forEach
function exibirNome(nome: string, pos: number){
    console.log(`- ${nome} esta na posicao ${pos}`);
}
harryPotter.forEach(exibirNome);

// Quantidade de Hermione:
var quantidadeHermione: number = 0;
harryPotter.forEach((nome) => {
    if (nome === "Hermione") {
        quantidadeHermione++;
    }
})
console.log(`Quantidade nomes Hermione: ${quantidadeHermione}.`)