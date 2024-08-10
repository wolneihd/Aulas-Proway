"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Aluno = void 0;
var Aluno = /** @class */ (function () {
    function Aluno(nome, codigo, curso) {
        this.matricula = false;
        this.notas = [];
        this.qtd_notas = 4;
        this.nome = nome;
        this.codigo = codigo;
        this.curso = curso;
    }
    Aluno.prototype.getNome = function () {
        return this.nome;
    };
    Aluno.prototype.setNome = function (nome) {
        this.nome = nome;
    };
    Aluno.prototype.mostrarNome = function () {
        return "Nome: ".concat(this.getNome(), " \nCodigo: ").concat(this.codigo, " \nCurso: ").concat(this.curso);
    };
    Aluno.prototype.setQtdNotas = function (qtd_notas) {
        this.qtd_notas = qtd_notas;
        console.log("Quantidade de notas alterado para: ".concat(this.qtd_notas));
    };
    Aluno.prototype.getQtdNotas = function () {
        return this.qtd_notas;
    };
    Aluno.prototype.gerarMedia = function (notas) {
        this.notas = notas;
        if (this.notas.length == this.getQtdNotas()) {
            var media = 0;
            this.notas.forEach(function (nota) {
                media += nota;
            });
            media = media / (this.notas.length);
            if (media >= 8) {
                console.log("- Aprovado (nota maior ou igual a 8): ".concat(media));
            }
            else if (media > 4 && media < 8) {
                console.log("- Retido em per\u00EDodo de exames (entre 4 e 8): ".concat(media));
            }
            else {
                console.log("- Reprovado (inferior a 4): ".concat(media));
            }
        }
        else {
            console.log("- M\u00E9dia somente ser\u00E1 gerado com ".concat(this.getQtdNotas(), " notas lan\u00E7adas!"));
        }
    };
    Aluno.prototype.alterarMatricula = function () {
        this.matricula = !this.matricula;
        console.log("Matricula alterada para ".concat(this.matricula ? "ATIVA" : "INATIVO"));
    };
    return Aluno;
}());
exports.Aluno = Aluno;
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
