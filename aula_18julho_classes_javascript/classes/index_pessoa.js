const { Pessoa } = require('./pessoa');

const pessoa_01 = new Pessoa('Wolnei', 'Hellmann Dircksen', 32);

pessoa_01.mostrarNomeCompleto();
pessoa_01.validadeIdade();

const pessoa_02 = new Pessoa('Ana', 'da Silva', 28);

pessoa_02.mostrarNomeCompleto();
pessoa_02.validadeIdade();