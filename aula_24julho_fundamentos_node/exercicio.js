var nome = prompt('Digite o seu nome:')

var paragrafo = document.getElementById('nome');
paragrafo.innerHTML = `<p>Bem vindo<p id='negrito'>${nome.toUpperCase()}</p>!</p>`;

paragrafo.style.backgroundColor = 'black';
paragrafo.style.color = 'white';
paragrafo.style.fontSize = '25px';
paragrafo.style.textAlign = 'center';

var negrito = document.getElementById('negrito');
negrito.style.fontWeight = 'bold';
