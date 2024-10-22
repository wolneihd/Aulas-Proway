import { Component } from '@angular/core';
import { TableModule } from 'primeng/table';

interface Categoria {
  id: number,
  nome: string
}

@Component({
  selector: 'app-lista-categorias',
  standalone: true,
  imports: [TableModule],
  templateUrl: './lista-categorias.component.html',
  styleUrl: './lista-categorias.component.css'
})
export class ListaCategoriasComponent {
  categorias!: Categoria[];

  ngOnInit() {
    this.categorias = [
      {
        id:1,
        nome: "RPG"
      },
      {
        id:2,
        nome: "Esporte"
      },
    ]
  }
}
