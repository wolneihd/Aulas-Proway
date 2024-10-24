import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { ListaCategoriasComponent } from './categorias/lista-categorias/lista-categorias.component';
import { CadastroUsuarioComponent } from './usuarios/cadastro-usuario/cadastro-usuario.component';

export const routes: Routes = [
    { path: "", redirectTo: "login", pathMatch: "full" },
    { path: "home", component: HomeComponent },
    { path: "login", component: LoginComponent },
    { path: "categorias", component: ListaCategoriasComponent },
    { path: "cadastrar", component: CadastroUsuarioComponent },
    { path: "**", redirectTo: "login" },
];
