const { Carro } = require('./carro');

const palio = new Carro('MCU-2207','FIAT','Palio');
const fox = new Carro('QJO-2188','VOLKSWAGEN','FOX');

console.log(palio)
console.log(fox)

fox.dados_veiculo()
fox.acelerar()

palio.dados_veiculo()
palio.acelerar()

const veiculos = [];
veiculos.push(palio, fox)
console.log(veiculos)
