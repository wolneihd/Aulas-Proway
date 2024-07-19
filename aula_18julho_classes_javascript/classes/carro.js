class Carro {
    constructor(placa, marca, modelo) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
    }

    acelerar() {
        console.log(`O carro ${this.modelo} está acelerando!`);
    }   

    dados_veiculo() {
        console.log(`
            placa: ${this.placa}
            marca: ${this.marca}
            modelo: ${this.modelo}
        `)
    }
}

module.exports = {Carro}