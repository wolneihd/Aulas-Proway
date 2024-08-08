// exemplo 01
function dizerOla(): void {
    console.log('Void não ter RETURN');
}
dizerOla();

// exemplo 02
var nombre: string = 'Wolnei Hellmann Dircksen';
function nomeCompleto(nombre: string) {
    return `Seu nome completo é ${nombre}`
}
console.log(nomeCompleto(nombre));

// exemplo 03
function obterMes11(): string {
    return 'Novembro';
}
console.log(obterMes11());

// exemplo 04
function somar(a: number, b: number): number {
    return a + b;
}
console.log(somar(10, 20));

// exemplo 05
function boasVindas(escola?: string): void {
    if (escola) {
        console.log(`Bem vindo a ${escola}!`);
    } else {
        console.log('Bem vindo!')
    }
}
boasVindas('SENAI');
boasVindas();

// exemplo 06
function elevarNumero(a: number, b: number = 2): number {
    return a ** b;
}
console.log(elevarNumero(2));
console.log(elevarNumero(2,3));
