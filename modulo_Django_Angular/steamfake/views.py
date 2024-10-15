from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from steamfake.models import Categoria

# Create your views here.
# http://127.0.0.1:8000/steamfake/categoria
def categoria_index(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    dados = {
        "categorias": categorias
    }
    return render(request, "categorias/index.html", context=dados)

def categoria_cadastro(request: HttpRequest) -> HttpResponse:
    return render(request, "categorias/cadastro.html")

def categoria_cadastrar(request: HttpRequest) -> HttpResponse:
    nome = request.POST.get("nome")
    categoria = Categoria(nome=nome)
    categoria.save()
    return redirect("categorias")

def categoria_apagar(request: HttpRequest, id:int) -> HttpResponse:
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect("categorias")