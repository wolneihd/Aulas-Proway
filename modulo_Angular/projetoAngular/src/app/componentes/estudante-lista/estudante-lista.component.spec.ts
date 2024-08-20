import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EstudanteListaComponent } from './estudante-lista.component';

describe('EstudanteListaComponent', () => {
  let component: EstudanteListaComponent;
  let fixture: ComponentFixture<EstudanteListaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EstudanteListaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EstudanteListaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
