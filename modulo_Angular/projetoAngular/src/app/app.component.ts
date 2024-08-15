import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  codigo: number = 1;
  nome: string = "Wolnei";
  curso: string = "Super DEV";
  status: boolean = true;

  dados: any = {
    nome: "Wolnei",
    idade: 33
  }  
}
