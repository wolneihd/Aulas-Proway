import { CanActivateFn, Router } from '@angular/router';
import { AutentificacaoService } from '../services/autentificacao.service';
import { inject } from '@angular/core';

export const autenticacaoGuard: CanActivateFn = (route, state) => {
  const autentificacaoService = inject(AutentificacaoService);
  const router = inject(Router);

  if (autentificacaoService.isAuthenticated()) {
    return true;
  }
  router.navigate(['login']);
  return false;
};
