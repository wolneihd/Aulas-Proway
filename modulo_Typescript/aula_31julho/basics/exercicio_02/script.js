var listaAlunos = [];
var idAluno = 0;
function validar() {
    var _a;
    //const id_aluno = document.querySelector<HTMLInputElement>('#idAluno');
    var nome = document.querySelector('#nome');
    var matricula = getCheckbox();
    var periodo = getSelectbox();
    var notas = getNotas();
    idAluno++;
    var aluno = {
        id: idAluno,
        nome: nome === null || nome === void 0 ? void 0 : nome.value,
        matricula: matricula,
        periodo: periodo,
        notas01: notas[0],
        notas02: notas[1],
        notas03: notas[2],
    };
    console.log(aluno);
    var newRow = document.getElementById('new-row');
    newRow.innerHTML += "\n    <tr>\n        <td>".concat(aluno.id, "</td>\n        <td>").concat((_a = aluno.nome) === null || _a === void 0 ? void 0 : _a.toUpperCase(), "</td>\n        <td>").concat(aluno.matricula ? "ATIVO" : 'NÃO ATIVO', "</td>\n        <td>").concat(aluno.periodo.toUpperCase(), "</td>\n        <td>").concat(aluno.notas01, "</td>\n        <td>").concat(aluno.notas02, "</td>\n        <td>").concat(aluno.notas03, "</td>   \n        <td>").concat((aluno.notas01 + aluno.notas02 + aluno.notas03) / 3, "</td> \n    </tr> \n    ");
}
function getCheckbox() {
    var _a;
    var checkbox = document.getElementById('matricula');
    return (_a = checkbox === null || checkbox === void 0 ? void 0 : checkbox.checked) !== null && _a !== void 0 ? _a : false;
}
function getSelectbox() {
    var selectBox = document.getElementById('periodo');
    return selectBox.value;
}
function getNotas() {
    // Obtém os elementos de input
    var nota01 = document.querySelector('#nota01');
    var nota02 = document.querySelector('#nota02');
    var nota03 = document.querySelector('#nota03');
    // Converte os valores dos inputs para números e filtra valores inválidos
    var todas_notas = [
        nota01 === null || nota01 === void 0 ? void 0 : nota01.value,
        nota02 === null || nota02 === void 0 ? void 0 : nota02.value,
        nota03 === null || nota03 === void 0 ? void 0 : nota03.value
    ]
        .map(function (value) { return parseFloat(value || 'NaN'); }) // Converte para número, substituindo undefined por 'NaN'
        .filter(function (value) { return !isNaN(value); }); // Remove valores NaN
    return todas_notas;
}
