import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { PasswordModule } from 'primeng/password';
import { RippleModule } from 'primeng/ripple';
import { ToastModule } from 'primeng/toast';
import { PanelModule } from 'primeng/panel';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [InputTextModule, FormsModule, ButtonModule, ToastModule, RippleModule, PasswordModule, PanelModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  providers: [MessageService]
})
export class LoginComponent {
  login: string = "";
  senha: string = "";

  constructor(
    private messageService: MessageService,
    private router: Router,
  ) { }

  enviar() {
    if (this.login == "admin" && this.senha == "1234") {
      this.router.navigate(["/home"]);
    } else {
      this.messageService.add({ severity: 'error', summary: 'Erro', detail: 'Login ou senha inválida'});
    }
  }

  redirecionarCadastrar() {
    this.router.navigate(["/cadastrar"])
  }
}
