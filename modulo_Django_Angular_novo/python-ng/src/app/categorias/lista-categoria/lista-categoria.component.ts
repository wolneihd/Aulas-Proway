import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { DialogModule } from 'primeng/dialog';
import { InputTextModule } from 'primeng/inputtext';
import { TableModule } from 'primeng/table';
import { CategoriaService } from '../../services/categoria.service';
import { NavbarComponent } from '../../navbar/navbar.component';
import { MessageService } from 'primeng/api';
import { ToastModule } from 'primeng/toast';

interface Categoria {
  id: number,
  nome: string
}

@Component({
  selector: 'app-lista-categoria',
  standalone: true,
  imports: [TableModule, ButtonModule, DialogModule, InputTextModule, FormsModule, NavbarComponent, ToastModule],
  templateUrl: './lista-categoria.component.html',
  styleUrl: './lista-categoria.component.css',
  providers: [MessageService]
})
export class ListaCategoriaComponent {
  nome: string = "";
  categorias!: Categoria[];
  modalApresentada: boolean = false;

  constructor(private categoriaService: CategoriaService, private messageService: MessageService) { }

  ngOnInit() {
    this.carregarCategorias()
  }

  carregarCategorias() {
    this.categoriaService.obterTodas().subscribe({
      next: categorias => this.categorias = categorias,
      error: erro => {
        console.error(erro);
        this.apresentarMensagemErro("Não foi possivel carregar a lista de categorias!")
      }
    })
  }

  abrirModal() {
    this.modalApresentada = true;
  }

  salvar() {
    this.categoriaService.cadastrar(this.nome).subscribe({
      next: () => {
        this.apresentarMensagemSucesso("Cadastrado com sucesso")
        this.modalApresentada = false;
        this.nome = "";
        this.carregarCategorias()
      },
      error: erro => {
        console.error(erro);
        this.apresentarMensagemErro("Erro ao cadastrar")
      }
    })
  }

  apagar(id: number) {
    this.categoriaService.apagar(id).subscribe({
      next: () => {
        this.apresentarMensagemSucesso("Excluído com sucesso")
        this.carregarCategorias()
      },
      error: erro => {
        console.error(erro);
        this.apresentarMensagemErro("Erro ao excluir")
      }
    })
  }

  apresentarMensagemSucesso(mensagem: string) {
    this.messageService.add({ severity: 'success', summary: 'Sucesso', detail: mensagem });
  }

  apresentarMensagemErro(mensagem: string) {
    this.messageService.add({ severity: 'error', summary: 'Erro', detail: mensagem });
  }
}
