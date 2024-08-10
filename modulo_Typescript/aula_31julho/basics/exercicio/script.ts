export class Aluno {
    private nome: string;
    public readonly codigo: number;
    public curso: string;
    public matricula: boolean = false;
    public notas: number[] = [];
    private qtd_notas: number = 4;

    constructor(nome: string, codigo: number, curso: string) {
        this.nome = nome;
        this.codigo = codigo;
        this.curso = curso;
    }

    getNome(): string {
        return this.nome;
    }

    setNome(nome: string) {
        this.nome = nome;
    }

    mostrarNome(): string {
        return `Nome: ${this.getNome()} \nCodigo: ${this.codigo} \nCurso: ${this.curso}`
    }

    setQtdNotas(qtd_notas: number) {
        this.qtd_notas = qtd_notas;
        console.log(`Quantidade de notas alterado para: ${this.qtd_notas}`)
    }

    getQtdNotas(): number {
        return this.qtd_notas;
    }

    gerarMedia(notas: number[]) {
        this.notas = notas;
        if (this.notas.length == this.getQtdNotas()) {
            var media: number = 0;
            this.notas.forEach(nota => {
                media += nota;
            })
            media = media / (this.notas.length);
            if (media >= 8) {
                console.log(`- Aprovado (nota maior ou igual a 8): ${media}`)
            } else if (media > 4 && media < 8) {
                console.log(`- Retido em período de exames (entre 4 e 8): ${media}`)
            } else {
                console.log(`- Reprovado (inferior a 4): ${media}`)
            }
        } else {
            console.log(`- Média somente será gerado com ${this.getQtdNotas()} notas lançadas!`)
        }
    }

    alterarMatricula() {
        this.matricula = !this.matricula;
        console.log(`Matricula alterada para ${this.matricula ? "ATIVA" : "INATIVO"}`);
    }
}

var aluno_01 = new Aluno('Wolnei', 1, "SUPER-DEV");
aluno_01.setNome('Pedro');

console.log(aluno_01.mostrarNome());

// alterar valor matricula:
aluno_01.alterarMatricula();
aluno_01.alterarMatricula();
aluno_01.alterarMatricula();
aluno_01.alterarMatricula();

// função de gerar média:
aluno_01.setQtdNotas(3);
aluno_01.gerarMedia([3, 7, 5, 3, 1]);
aluno_01.gerarMedia([3, 7, 5]);
aluno_01.gerarMedia([1, 2, 5, 4]);