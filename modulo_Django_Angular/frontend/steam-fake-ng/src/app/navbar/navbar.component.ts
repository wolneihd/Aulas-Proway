import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MenubarModule } from 'primeng/menubar';
import { Router } from '@angular/router';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [MenubarModule, CommonModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent implements OnInit{
  items: MenuItem[] | undefined;

  constructor(private router: Router) {}

  ngOnInit() {
      this.items = [
          {
              label: 'Jogos',
              icon: 'pi pi-align-justify',
              items: [
                  {
                      label: 'Categorias',
                      route: '/categorias'
                  },
                  {
                      label: 'Jogos',
                      route: '/jogos'
                  }
              ]
          }
      ];
  }
}
