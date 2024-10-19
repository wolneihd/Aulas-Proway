from django.urls import path
from steamfake import views

# http://127.0.0.1:8000/steamfake/categoria
urlpatterns = [
    path("categoria",views.categoria_index, name="categorias"),
    path("categoria/cadastro",views.categoria_cadastro),
    path("categoria/cadastrar",views.categoria_cadastrar),
    path("categoria/apagar/<int:id>",views.categoria_apagar),
    path("categoria/editar/<int:id>",views.categoria_editar),
    path("categoria/editado/<int:id>",views.categoria_editado),
    path("",views.home),

    path("tag",views.tag_index, name="tags"),
    path("tag/cadastro",views.tag_cadastro),
    path("tag/cadastrar",views.tag_cadastrar),
    path("tag/apagar/<int:id>",views.tag_apagar),
    path("tag/editar/<int:id>",views.tag_editar),
    path("tag/editado/<int:id>",views.tag_editado),

    path("jogo",views.jogo_index, name="jogos"),
    path("jogo/cadastro",views.jogo_cadastro),
    path("jogo/apagar/<int:id>",views.jogo_apagar),
    path("jogo/editar/<int:id>",views.jogo_editar),
]