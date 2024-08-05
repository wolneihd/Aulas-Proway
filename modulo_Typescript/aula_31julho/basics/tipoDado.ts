const nomes: string[] = ["Bob"];
nomes.push("Patrick");
nomes.push("Antony");
nomes.pop()
// imprimir dados
for (var i = 0; i < nomes.length; i++) {
    console.log(nomes[i]);
}

const dados: [string, number, boolean] = ["Wolnei", 32, false];
// imprimir dados
for (var i = 0; i < dados.length; i++) {
    console.log(`${i} ${dados[i]} ${typeof(dados[i])}`);
}

const elemento: any[] = [55,"Robert",false];
// imprimir dados
for (var i = 0; i < elemento.length; i++) {
    console.log(`${i} ${elemento[i]} ${typeof(elemento[i])}`);
}