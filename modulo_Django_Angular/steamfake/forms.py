from django import forms

from steamfake.models import Categoria

class JogoForm(forms.Form):
    nome = forms.CharField(
        max_length=50, 
        min_length=3, 
        label="Nome do Jogo",
        widget=forms.TextInput(attrs={
            "class":"input"
        })
    )
    valor = forms.DecimalField(
        max_digits=9, 
        decimal_places=2,
        label="Valor",
        widget=forms.NumberInput(attrs={
            "class":"input",
            "step":"0.01"
        })
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecionar a categoria",
    )
    data_lancamento = forms.DateField(
        label="Data de Lançamento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class":"input"
            }
        )
    )
    desenvolvedora = forms.CharField(
        label="Desenvolvedora", 
        min_length=2, 
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            "class":"input"
        })
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":'textarea',
            }
        ), 
        label='Descrição', 
        required=False,

    )
    foto_capa = forms.ImageField(label="Foto da Capa", required=False)

class JogoEditarForm(forms.Form):
    nome = forms.CharField(
        max_length=50, 
        min_length=3, 
        label="Nome do Jogo",
        widget=forms.TextInput(attrs={
            "class":"input"
        })
    )
    valor = forms.DecimalField(
        max_digits=9, 
        decimal_places=2,
        label="Valor",
        widget=forms.NumberInput(attrs={
            "class":"input",
            "step":"0.01"
        })
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecionar a categoria",
    )
    data_lancamento = forms.DateField(
        label="Data de Lançamento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class":"input"
            }
        )
    )
    desenvolvedora = forms.CharField(
        label="Desenvolvedora", 
        min_length=2, 
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            "class":"input"
        })
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":'textarea',
            }
        ), 
        label='Descrição', 
        required=False,

    )
    foto_capa = forms.ImageField(label="Foto da Capa", required=False)