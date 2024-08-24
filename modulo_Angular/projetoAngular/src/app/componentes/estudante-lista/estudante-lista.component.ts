import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Aluno } from '../../interface/Estudante';

@Component({
  selector: 'app-estudante-lista',
  templateUrl: './estudante-lista.component.html',
  styleUrl: './estudante-lista.component.css'
})

export class EstudanteListaComponent {
  @Input()
  lista: Aluno[] = [];

  @Output()
  excluir: EventEmitter<number> = new EventEmitter();
  @Output()
  editar: EventEmitter<number> = new EventEmitter();

  public editarAluno(estudante: any): void {
    //console.log('Enviando editar aluno... ', matricula);
    this.editar.emit(estudante);
  }

  public excluirAluno(matricula: number): void {
    //console.log('Enviando matricular para app.component... ', matricula);
    this.excluir.emit(matricula);
  }
}
