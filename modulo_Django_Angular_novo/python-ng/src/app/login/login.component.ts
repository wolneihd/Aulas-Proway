import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { PanelModule } from 'primeng/panel';
import { PasswordModule } from 'primeng/password';
import { ToastModule } from 'primeng/toast';
import { AutentificacaoService } from '../services/autentificacao.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    InputTextModule,
    FormsModule,
    ButtonModule,
    ToastModule,
    PasswordModule,
    PanelModule,
  ],
  providers: [MessageService],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  login: string = "";
  senha: string = "";

  constructor(
    // Necessário para poder apresentar mensagem de feeback para o usuário
    private messageService: MessageService,
    // Necessário para poder redirecionar para outra rota
    private router: Router,
    private autentificacaoService: AutentificacaoService
  ) { }

  enviar() {
    this.autentificacaoService.autenticar(this.login, this.senha).subscribe({
      next: dado => {
        console.log(dado);
        this.messageService.add({severity: 'success', summary:"Deu boa", detail: 'Login realizado com sucesso!'});
      },
      error: erro => {
        console.error(erro)
        this.messageService.add({severity: 'error', summary:"Erro", detail: 'Login e/ou senha inválidos!'})
      }
    })
  }

  redirecionarCadastrar() {
    this.router.navigate(["/cadastrar"])
  }
}
