import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Categoria } from '../models/categoria';
import { HttpClient } from '@angular/common/http';
import { enviroment } from '../enviroments/enviroment';

const apiUrl = enviroment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {

  constructor(private httpClient: HttpClient) { }

  obterTodas(): Observable<Categoria[]> {
    return this.httpClient.get<Categoria[]>(`${apiUrl}/categoria/`)
  }

  cadastrar(nome: string): Observable<any> {
    let dados = {
      nome
    }
    return this.httpClient.post(`${apiUrl}/categoria/`, dados);
  }

  apagar(id: number): Observable<any> {
    return this.httpClient.delete(`${apiUrl}/categoria/${id}/`)
  }

  obterPorId(id: number): Observable<Categoria> {
    return this.httpClient.get<Categoria>(`${apiUrl}/categoria/${id}/`)
  }

  editar(id: number, nome: string): Observable<any> {
    let dados = {
      nome
    }
    return this.httpClient.put(`${apiUrl}/categoria/${id}/`, dados);
  }
}
