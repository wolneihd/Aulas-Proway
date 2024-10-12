from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # importando o arquivo template
    template = loader.get_template(template_name="index.html")
    # renderizar o template
    html = template.render(context={}, request=request)
    response = HttpResponse(content=html)
    return response


def contato(request: HttpRequest) -> HttpResponse:
    return render(request, "contato.html",context={})


def calculadora(request: HttpRequest) -> HttpResponse:
    return render(request, "calculadora.html",context={})

def calcular(request: HttpRequest) -> HttpResponse:
    numero01 = request.GET.get("numero01")
    numero02 = request.GET.get("numero02")
    soma = int(numero01) + int(numero02)
    return render(request, "resultado.html",context={"soma":soma}) 

def notas_aluno(request: HttpRequest) -> HttpResponse:
    return render(request, "aluno.html",context={})

def calcular_media(request: HttpRequest) -> HttpResponse:
    numero01 = request.GET.get("numero01")
    numero02 = request.GET.get("numero02")
    numero03 = request.GET.get("numero03")
    nome = request.GET.get("nome")
    media = (int(numero01) + int(numero02) + int(numero03))/3
    if (media >= 7):
        texto = "aprovado"
    else:
        texto =  "reprovado"
    contexto = {
        "media": media, 
        "nome": nome,
        "texto": texto
    }
    return render(request, "media.html",context=contexto) 