import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { enviroment } from '../enviroments/enviroment';

export interface LoginReponse {
  access: string;
  refresh: string;
}

const apiUrl = enviroment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class AutentificacaoService {

  constructor(private httpClient: HttpClient) { }

  autenticar(login: string, senha: string): Observable<LoginReponse>{
    return this.httpClient.post<LoginReponse>(`${apiUrl}/login/`, { username: login, password: senha })
  }

  salvarToken(access: string, refresh: string) {
    localStorage.setItem("access", access);
    localStorage.setItem("refresh", refresh);
  }

  isAuthenticated(): boolean {
    const token = localStorage.getItem("access");
    return !!token;
  }

  getToken(): string | null {
    return localStorage.getItem("access");
  }
}
