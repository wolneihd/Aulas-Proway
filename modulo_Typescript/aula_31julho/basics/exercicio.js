var nome = 'Wolnei Hellmann Dircksen';
var codigo = 123456;
var cadastro = true;
var currentDate = new Date();
var mes = currentDate.getMonth() + 1;
var texto_mes = '';
switch (mes) {
    case 1:
        texto_mes = 'janeiro';
        break;
    case 2:
        texto_mes = 'fevereiro';
        break;
    case 3:
        texto_mes = 'março';
        break;
    case 4:
        texto_mes = 'abril';
        break;
    case 5:
        texto_mes = 'maio';
        break;
    case 6:
        texto_mes = 'junho';
        break;
    case 7:
        texto_mes = 'julho';
        break;
    case 8:
        texto_mes = 'agosto';
        break;
    case 9:
        texto_mes = 'setembro';
        break;
    case 10:
        texto_mes = 'outubro';
        break;
    case 11:
        texto_mes = 'novembro';
        break;
    case 12:
        texto_mes = 'dezembro';
        break;
}
console.log("\nOl\u00E1, meu nome \u00E9 ".concat(nome, "."));
console.log("Meu c\u00F3digo de aluno ".concat(codigo, "."));
console.log("Atualmente estou estudando no SUPERDEV? ".concat(true ? "Verdadeiro" : "Falso"));
console.log("Sabendo que estamos no m\u00EAs ".concat(mes, ", posso dizer que \u00E9 ").concat(texto_mes, ".\n"));
