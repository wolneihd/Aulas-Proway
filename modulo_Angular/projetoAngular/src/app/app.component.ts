import { Component, OnInit } from '@angular/core';
import { ApiService } from './shared/api.service';
import { Aluno } from './interface/Estudante';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit {
  data: any;
  loading = true;
  error: string | null = null;

  // Lista inicial de estudantes
  listaEstudantes: Aluno[] = [
    {
      nome: "Wolnei Hellmann Dircksen",
      matricula: 1234,
      email: "aluno@proway.com",
      curso: "Angular",
      status: true,
      materias: ['HTML', 'CSS', 'Typescript'],
      escola: {
        nome: 'Proway',
        cidade: 'Blumenau'
      },
      imagemPath: '../../../assets/imagens/imagem-avatar_0.jpg'
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
      },
      imagemPath: '../../../assets/imagens/imagem-avatar_1.jpg'
    },
    {
      nome: "Antônio José",
      matricula: 4321,
      email: "pedro@proway.com",
      curso: "Photoshop",
      status: false,
      materias: ['Photoshop'],
      escola: {
        nome: 'Proway',
        cidade: 'Blumenau'
      },
      imagemPath: '../../../assets/imagens/imagem-avatar_2.jpg'
    }
  ];

  // chatGPT ... estudar código.
  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getData().subscribe({
      next: (response) => {
        console.log(response);
        // Supondo que a estrutura da resposta seja como o exemplo acima
        if (response.results && response.results.length > 0) {
          let novoData = {
            nome: response.results[0].name.first,
            matricula: 1234, 
            email: response.results[0].email, 
            curso: 'Excel Av.', 
            status: true, 
            materias: ['Excel'], 
            escola: {
              nome: 'Escola', 
              cidade: response.results[0].location.city 
            },
            imagemPath: response.results[0].picture.large
          };
          // Adicione os dados transformados à listaEstudantes
          this.listaEstudantes.push(novoData);
        } else {
          console.error('Response does not contain the expected results array:', response);
        }
        this.loading = false;
      },
      error: (err) => {
        this.error = 'An error occurred while fetching data';
        this.loading = false;
      },
    });
  }
}
