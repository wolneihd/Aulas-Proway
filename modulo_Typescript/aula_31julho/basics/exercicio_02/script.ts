const listaAlunos: any[] = [];

function validar() {
    const id_aluno = document.querySelector<HTMLInputElement>('#idAluno');
    const nome = document.querySelector<HTMLInputElement>('#nome');
    const matricula = getCheckbox();
    const periodo = getSelectbox();
    const notas = getNotas();

    const aluno = {
        id: id_aluno?.value,
        nome: nome?.value,
        matricula: matricula,
        periodo: periodo,
        notas01: notas[0],
        notas02: notas[1],
        notas03: notas[2],
    }

    const newRow = document.getElementById('new-row') as HTMLTableRowElement;
    newRow.innerHTML += `
    <tr>
        <td>${aluno.id}</td>
        <td>${aluno.nome?.toUpperCase()}</td>
        <td>${aluno.matricula ? "ATIVO" : 'NÃO ATIVO'}</td>
        <td>${aluno.periodo.toUpperCase()}</td>
        <td>${aluno.notas01}</td>
        <td>${aluno.notas02}</td>
        <td>${aluno.notas03}</td>   
        <td>${(aluno.notas01 + aluno.notas02 + aluno.notas03) / 3}</td> 
    </tr> 
    `
}

function getCheckbox() {
    const checkbox = document.getElementById('matricula') as HTMLInputElement | null;
    return checkbox?.checked ?? false;
}

function getSelectbox() {
    const selectBox = document.getElementById('periodo') as HTMLInputElement;
    return selectBox.value;
}

function getNotas(): number[] {
    // Obtém os elementos de input
    const nota01 = document.querySelector<HTMLInputElement>('#nota01');
    const nota02 = document.querySelector<HTMLInputElement>('#nota02');
    const nota03 = document.querySelector<HTMLInputElement>('#nota03');

    // Converte os valores dos inputs para números e filtra valores inválidos
    const todas_notas: number[] = [
        nota01?.value,
        nota02?.value,
        nota03?.value
    ]
        .map(value => parseFloat(value || 'NaN')) // Converte para número, substituindo undefined por 'NaN'
        .filter(value => !isNaN(value));          // Remove valores NaN
    return todas_notas;
}