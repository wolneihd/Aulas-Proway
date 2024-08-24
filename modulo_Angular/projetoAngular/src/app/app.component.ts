import { Component, OnInit } from '@angular/core';
import { ApiService } from './shared/api.service';
import { Aluno } from './interface/Estudante';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  data: any;
  loading = true;
  error: string | null = null;
  btnMostrar: boolean = true;

  // action button:
  inverterMostrador(): void {
    this.btnMostrar = !this.btnMostrar;
  }

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
      matricula: 6002,
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
    },
    {
      "nome": "Ana Paula Silva",
      "matricula": 5678,
      "email": "ana.silva@proway.com",
      "curso": "React",
      "status": true,
      "materias": ["JavaScript", "React", "Node.js"],
      "escola": {
        "nome": "Proway",
        "cidade": "São Paulo"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_1.jpg"
    },
    {
      "nome": "Carlos Eduardo Santos",
      "matricula": 9101,
      "email": "carlos.santos@proway.com",
      "curso": "Vue.js",
      "status": false,
      "materias": ["JavaScript", "Vue.js", "Webpack"],
      "escola": {
        "nome": "Proway",
        "cidade": "Curitiba"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_2.jpg"
    },
    {
      "nome": "Mariana Oliveira",
      "matricula": 1121,
      "email": "mariana.oliveira@proway.com",
      "curso": "Node.js",
      "status": true,
      "materias": ["Node.js", "Express", "MongoDB"],
      "escola": {
        "nome": "Proway",
        "cidade": "Porto Alegre"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_0.jpg"
    },
    {
      "nome": "Lucas Fernandes",
      "matricula": 3141,
      "email": "lucas.fernandes@proway.com",
      "curso": "Angular",
      "status": true,
      "materias": ["HTML", "CSS", "Angular"],
      "escola": {
        "nome": "Proway",
        "cidade": "Recife"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_1.jpg"
    },
    {
      "nome": "Beatriz Almeida",
      "matricula": 5161,
      "email": "beatriz.almeida@proway.com",
      "curso": "Python",
      "status": false,
      "materias": ["Python", "Django", "Flask"],
      "escola": {
        "nome": "Proway",
        "cidade": "Fortaleza"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_2.jpg"
    },
    {
      "nome": "Eduardo Lima",
      "matricula": 7181,
      "email": "eduardo.lima@proway.com",
      "curso": "C#",
      "status": true,
      "materias": ["C#", ".NET", "SQL Server"],
      "escola": {
        "nome": "Proway",
        "cidade": "Salvador"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_1.jpg"
    },
    {
      "nome": "Juliana Costa",
      "matricula": 9202,
      "email": "juliana.costa@proway.com",
      "curso": "Java",
      "status": true,
      "materias": ["Java", "Spring", "Hibernate"],
      "escola": {
        "nome": "Proway",
        "cidade": "Belo Horizonte"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_0.jpg"
    },
    {
      "nome": "Gabriel Pereira",
      "matricula": 2233,
      "email": "gabriel.pereira@proway.com",
      "curso": "Swift",
      "status": false,
      "materias": ["Swift", "iOS Development", "Xcode"],
      "escola": {
        "nome": "Proway",
        "cidade": "Brasília"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_2.jpg"
    },
    {
      "nome": "Fernanda Martins",
      "matricula": 4455,
      "email": "fernanda.martins@proway.com",
      "curso": "Ruby on Rails",
      "status": true,
      "materias": ["Ruby", "Rails", "SQL"],
      "escola": {
        "nome": "Proway",
        "cidade": "Goiânia"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_1.jpg"
    },
    {
      "nome": "Ricardo Gomes",
      "matricula": 6677,
      "email": "ricardo.gomes@proway.com",
      "curso": "PHP",
      "status": true,
      "materias": ["PHP", "Laravel", "MySQL"],
      "escola": {
        "nome": "Proway",
        "cidade": "Manaus"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_1.jpg"
    },
    {
      "nome": "Cláudia Ribeiro",
      "matricula": 8899,
      "email": "claudia.ribeiro@proway.com",
      "curso": "JavaScript",
      "status": false,
      "materias": ["JavaScript", "React", "Node.js"],
      "escola": {
        "nome": "Proway",
        "cidade": "Natal"
      },
      "imagemPath": "../../../assets/imagens/imagem-avatar_2.jpg"
    }
  ];

  backupLista: Aluno[] = this.listaEstudantes;
  novalistaEstudantes: Aluno[] = [];

  //Logic Select-box:
  onSelectChange(event: Event): void {
    const selectElement = event.target as HTMLSelectElement;
    const selectedValue = selectElement.value;
    if (selectedValue == 'aprovados') {
      console.log('trazer aprovados!')
      this.gerarAprovados();
    } else if (selectedValue == 'reprovados') {
      this.gerarReprovados();
    } else {
      this.listaEstudantes = this.backupLista;
    }
  }

  gerarAprovados() {
    this.listaEstudantes = this.backupLista;
    this.novalistaEstudantes = [];
    for (var i = 0; i < this.listaEstudantes.length; i++) {
      if (this.listaEstudantes[i].status == true) {
        this.novalistaEstudantes.push(this.listaEstudantes[i])
      }
    }
    this.listaEstudantes = this.novalistaEstudantes;
  }

  gerarReprovados() {
    this.listaEstudantes = this.backupLista;
    this.novalistaEstudantes = [];
    for (var i = 0; i < this.listaEstudantes.length; i++) {
      if (this.listaEstudantes[i].status == false) {
        this.novalistaEstudantes.push(this.listaEstudantes[i])
      }
    }
    this.listaEstudantes = this.novalistaEstudantes;
  }

  //excluir aluno:
  excluirAluno(matricula: number) {
    const indexAluno = this.backupLista.findIndex(estudante => {
      return estudante.matricula == matricula;
    })
    console.log('Excluindo.. ', this.backupLista[indexAluno]);
    if (indexAluno >= 0) {
      this.backupLista.splice(indexAluno, 1);
    }
    this.listaEstudantes = this.backupLista;
  }

  //editar aluno:
  aluno: Aluno = {
    nome: '',
    matricula: 0,
    email: '',
    curso: '',
    status: false,
    materias: [],
    escola: undefined,
    imagemPath: ''
  }
  editarAluno(estudante: any) {
    console.log('Recebido no app.component EDITAR...', estudante);
    this.aluno = estudante;
  }

  /*
  OUTRA OPÇÃO DE LISTAR APROVADOS E REPROVADOS:

  exibirReprovados(): void {
    this.listaEstudantes = this.backupLista;
    this.listaEstudantes = this.listaEstudantes.filter( estudante => {
      return estudante.status == false;
    })
  }
  */

  // chatGPT ... estudar código.
  constructor(private apiService: ApiService) { }

  /*
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
  */
}
