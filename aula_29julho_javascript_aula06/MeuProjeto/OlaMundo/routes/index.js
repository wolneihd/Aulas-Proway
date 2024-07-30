var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Home' });
});

router.get('/historia', function(req, res, next) {
  res.render('index', { title: 'História',text:"Conheça a nossa história" });
});

router.get('/pratica', function(req, res, next) {
  res.render('cadastro');
});

router.get('/pokedex', function(req, res, next) {
  res.render('pokedex');
});

module.exports = router;
