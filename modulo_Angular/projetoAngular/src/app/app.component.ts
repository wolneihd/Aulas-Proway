import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  
  listaEstudantes: any[] = [
    {
      nome: "Wolnei Hellmann Dircksen",
      matricula: 1234,
      email: "aluno@proway.com",
      curso: "Angular",
      status: true,
      materias: ['HTML','CSS','Typescript'],
      escola: {
        nome: 'Proway',
        cidade: 'Blumenau'
      }
    },
    {
      nome: "Pedro Alberto",
      matricula: 5678,
      email: "pedro@proway.com",
      curso: "Python",
      status: true,
      materias: ['Log. Prog.'],
      escola: {
        nome: 'Proway',
        cidade: 'Blumenau'
      }
    }
  ];
}
