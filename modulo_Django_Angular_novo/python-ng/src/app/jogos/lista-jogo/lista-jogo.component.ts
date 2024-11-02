import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { ImageModule } from 'primeng/image';
import { TableModule } from 'primeng/table';
import { JogoService } from '../../services/jogo.service';
import { JogoLista } from '../../models/jogo-lista';

// ng g c jogos/lista-jogo
@Component({
  selector: 'app-lista-jogo',
  standalone: true,
  imports: [
    TableModule,
    ImageModule,
    ButtonModule,
  ],
  templateUrl: './lista-jogo.component.html',
  styleUrl: './lista-jogo.component.css'
})
export class ListaJogoComponent {
  jogos!: JogoLista[];
  // ng g c jogos/cadastro-jogo
  constructor(private router: Router, private jogoService: JogoService){}

  ngOnInit(){
   this.jogoService.obterParaLista().subscribe({
    next: jogos => this.jogos = jogos,
    error: erro => {
      console.error(erro)
      alert("Não foi possível carregar a lista de jogos!")
    }
   })
  }

  acessarCadastro(){
    this.router.navigate(["/jogos/cadastro"]);
  }
}
