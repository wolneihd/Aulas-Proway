import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { EstudanteComponent } from './componentes/estudante/estudante.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

import { HttpClientModule } from '@angular/common/http';
import { EstudanteListaComponent } from './componentes/estudante-lista/estudante-lista.component';
import {MatIconModule} from '@angular/material/icon';
import { StudentFormComponent } from './componentes/student-form/student-form.component'
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    EstudanteComponent,
    EstudanteListaComponent,
    StudentFormComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatIconModule,
    FormsModule
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
