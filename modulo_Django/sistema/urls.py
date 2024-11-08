from django.urls import path
from sistema import views

urlpatterns = [
    path("/home", views.index),
    path("/", views.index),
    path("/contato", views.contato),
    path("/calculadora", views.calculadora),
    path("/calcular", views.calcular),
    path("/aluno", views.notas_aluno),
    path("/media", views.calcular_media),
]