// npm install express
// npm install
// ejs, pug
// npm install i ejs

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
    res.render('../views/home');
})

app.listen(3000, function(){
    console.log('Executando em [localhost:3000] \nCtrl+C para abortar o NODE JS.')
});