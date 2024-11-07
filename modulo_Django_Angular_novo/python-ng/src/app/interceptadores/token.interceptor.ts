import { HttpInterceptorFn } from '@angular/common/http';
import { AutentificacaoService } from '../services/autentificacao.service';
import { inject } from '@angular/core';
import { enviroment } from '../enviroments/enviroment';

const apiUrl = enviroment.apiUrl;

export const tokenInterceptor: HttpInterceptorFn = (req, next) => {
  const autenticacaoService: AutentificacaoService = inject(AutentificacaoService);
  const token = autenticacaoService.getToken();
  const isCadastroUsuario = `${apiUrl}/cliente/cadastro/` == req.url;

  if (token && isCadastroUsuario == false) {
    const clonaRequisicao = req.clone({
      setHeaders: {
        Authorization: `Bearer ${token}`
      }
    })
    return next(clonaRequisicao);
  }
  return next(req);
};
