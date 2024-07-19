const p1 = {
    nome: 'Maria',
    sobrenome: 'da Silva',
    //nomeCompleto: function() => (this.nome, this.sobrenome)
    nomeCompleto: function() {
        return this.nome + ' '+ this.sobrenome;
    } 
}

console.log(p1.nome)
console.log(p1.nomeCompleto());

// array
const frutas = ['maça','uva','pera'];

//--- opção 01
for (var i = 0; i<frutas.length; i++) {
    console.log(frutas[i]);
}
//--- opção 02
frutas.map( f => console.log(f.toUpperCase()));

// array de objetos
const nomes = [
    {
        nome: 'maria',
        idade: 18
    },
    {
        nome: 'joão',
        idade: 20
    }
]

//--- opção 01
for (var i = 0; i<nomes.length; i++) {
    console.log(nomes[i]);
}
//--- opção 02
nomes.map( n => console.log(n.nome));

// outro tipo de notação do objeto (elemento anônimo):

function Book(type, author) {
    this.type = type;
    this.author = author;
    this.getDetails = function () {
        return this.type + " written by " + this.author;
    }
}

var book = new Book("Fiction", "Peter King");
console.log(book.getDetails())
