let nome: string = 'Wolnei Hellmann Dircksen';
let codigo: number = 123456;
let cadastro: boolean = true;

var currentDate = new Date();
var mes = currentDate.getMonth() + 1;

let texto_mes: string = '';
switch (mes) {
    case 1:
        texto_mes = 'janeiro'
        break;
    case 2:
        texto_mes = 'fevereiro'
        break;
    case 3:
        texto_mes = 'março'
        break;
    case 4:
        texto_mes = 'abril'
        break;
    case 5:
        texto_mes = 'maio'
        break;
    case 6:
        texto_mes = 'junho'
        break;
    case 7:
        texto_mes = 'julho'
        break;
    case 8:
        texto_mes = 'agosto'
        break;
    case 9:
        texto_mes = 'setembro'
        break;
    case 10:
        texto_mes = 'outubro'
        break;
    case 11:
        texto_mes = 'novembro'
        break;
    case 12:
        texto_mes = 'dezembro'
        break;
}

console.log(`\nOlá, meu nome é ${nome}.`);
console.log(`Meu código de aluno ${codigo}.`);
console.log(`Atualmente estou estudando no SUPERDEV? ${true ? "Verdadeiro" : "Falso"}`);
console.log(`Sabendo que estamos no mês ${mes}, posso dizer que é ${texto_mes}.\n`)