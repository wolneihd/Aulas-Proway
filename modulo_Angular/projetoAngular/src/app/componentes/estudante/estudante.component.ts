import { Component, Input } from '@angular/core';
import { Aluno } from '../../interface/Estudante';

@Component({
  selector: 'app-estudante',
  templateUrl: './estudante.component.html',
  styleUrl: './estudante.component.css',
})
export class EstudanteComponent {
  @Input() estudante!: Aluno; 

  funcaoTeste(): void {
    alert(`Você clicou em algum dos cards! ${this.estudante.nome}`)
    console.log(this.estudante);
  }
}
