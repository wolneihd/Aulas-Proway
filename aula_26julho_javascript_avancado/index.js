// npm install express
// npm install
// ejs, pug
// npm install i ejs

const { header, form } = require('./componentes');

var express = require('express');
var app = express();

app.set('view engine', 'ejs');

app.get('/', function(req, res) {
    res.send('<h1>Bem-vindo!</h1>');
})

app.get('/home', function(req, res) {
    res.render('../views/home');
})

app.get('/contato', function(req, res) {
    res.render('../views/contato');
})

app.get('/bemvindo/:pagina', function (req,res) {
    let dsPagina = `<h1>Bem-vindo! ${req.params.pagina} </h1>`;
    dsPagina += `
    <a href="/home">Home</a>
    <a href="/home">Home</a>
    <p> lorem ipsum </p>`
    res.send (dsPagina);
})

app.get('/dados/:nome/:idade', function (req,res) {
    let dsPagina = `<h2> ${header()} Seu nome: ${req.params.nome} </h2>`;
    if (req.params.idade) {
        dsPagina += `<h2>idade: ${req.params.idade} </h2>`;
    }
    res.send (dsPagina);
})

app.get('/formAction',function (req,res) {
    let dsNome = req.query['dsNome'];
    let nrIdade = req.query['nrIdade'];
    let dsEmail = req.query['dsMail'];
    let dsPagina = '';
    if (dsNome) {
        dsPagina += `<p>Seu nome é ${dsNome}</p>`
    }
    if (nrIdade) {
        dsPagina += `<p>Sua idade é ${nrIdade}</p>`
    }
    if (dsEmail) {
        dsPagina += `<p>Seu nome é ${dsEmail}</p>`
    }
    res.send(dsPagina);
})

app.get('/cadastro', function (req,res) {
    res.send(form());
})

app.use(express.static('public'));

// monta o servidor e informa o horário:
var currentdate = new Date(); 
app.listen(3000, function(){
    console.log(`Executando em [localhost:3000] \nCtrl+C para abortar o NODE JS.\nBuild-date: ${currentdate}`)
});