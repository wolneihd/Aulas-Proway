import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { DialogModule } from 'primeng/dialog';
import { InputTextModule } from 'primeng/inputtext';
import { PaginatorModule } from 'primeng/paginator';
import { TableModule } from 'primeng/table';

interface Categoria {
  id: number,
  nome: string
}

@Component({
  selector: 'app-lista-categorias',
  standalone: true,
  imports: [TableModule, ButtonModule, DialogModule, InputTextModule, FormsModule, PaginatorModule],
  templateUrl: './lista-categorias.component.html',
  styleUrl: './lista-categorias.component.css'
})
export class ListaCategoriasComponent {
  nome: string = "";
  categorias!: Categoria[];
  modalApresentada: boolean = false;
  first: number = 0;
  rows: number = 10;

  ngOnInit() {
    this.categorias = [
      {
        id: 1,
        nome: "RPG"
      },
      {
        id: 2,
        nome: "Esporte"
      },
    ]
  }

  abrirModal() {
    this.modalApresentada = true;
  }
}
