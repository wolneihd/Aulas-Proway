class Pessoa {
    constructor(nome,sobrenome,idade) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.idade = idade;
    }

    mostrarNomeCompleto() {
        console.log(`Nome completo: ${this.nome} ${this.sobrenome}`); 
    }

    validadeIdade() {
        if (this.idade < 18) {
            console.log(`${this.nome} é MENOR de idade. Ele(a) tem ${this.idade} anos!`)
        } else {
            console.log(`${this.nome} é MAIOR de idade. Ele(a) tem ${this.idade} anos!`)
        }
    }
}

module.exports = {Pessoa}