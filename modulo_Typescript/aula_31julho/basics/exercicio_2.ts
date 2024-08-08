const dias: number[] = [1,3,2,7,9,5];

dias.forEach(dia => {
    switch (dia) {
        case 1:
            console.log(dia, '\x1b[31m- Domingo - restaurante fechado.\x1b[0m')
            break;
        case 2:
            console.log(dia, '\x1b[32m- Segunda-feira - Pizza de Peperoni.\x1b[0m')
            break;
        case 3:
            console.log(dia, '\x1b[32m- Terça-feira - Pizza Margherita.\x1b[0m')
            break;
        case 4:
            console.log(dia, '\x1b[32m- Quarta-feira - Pizza de Calabresa.\x1b[0m')
            break;
        case 5:
            console.log(dia, '\x1b[32m- Quinta-feira - Pizza Napolitana.\x1b[0m')
            break;
        case 6:
            console.log(dia, '\x1b[32m- Sexta-feira - Pizza de Chocolate.\x1b[0m')
            break;
        case 7:
            console.log(dia, '\x1b[32m- Sábado - Pizza de filé com cheddar.\x1b[0m')
            break;
        default:
            console.log(dia, '\x1b[31m- Dia da semana inválido.\x1b[0m')
            break;
    }
})