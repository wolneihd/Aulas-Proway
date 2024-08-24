import { Component, Input } from '@angular/core';
import { Aluno } from '../../interface/Estudante';

@Component({
  selector: 'app-student-form',
  templateUrl: './student-form.component.html',
  styleUrl: './student-form.component.css'
})
export class StudentFormComponent {

  @Input()
  estudante: Aluno = {
    nome: '',
    matricula: 0,
    email: '',
    curso: '',
    status: false,
    materias: [],
    escola: undefined,
    imagemPath: ''
  };
}
