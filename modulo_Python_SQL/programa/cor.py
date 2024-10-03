import questionary
import os
from repositorios.cor_repositorio import get_all_colors, insert_color, update_color, delete_color
from rich.console import Console
from rich.table import Table

def limpar_tela():
    os.system("cls")

def menu_cores():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Cores",
        choices=[
            "Consultar",
            "Cadastrar",
            "Editar",
            "Apagar",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar":
            consultar_cores()
        elif opcao_escolhida == "Cadastrar":
            cadastrar_cor()
        elif opcao_escolhida == "Editar":
            editar_cor()
        elif opcao_escolhida == "Apagar":
            apagar_cor()

def consultar_cores():
    listaCores = get_all_colors()
    if len(listaCores) == 0:
        print("Nenhuma cor cadastrada!")
        return
    
    table = Table(title="Lista de Cores")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Cor", justify="center", style="magenta")

    for cor in listaCores:
        table.add_row(str(cor.id), cor.nome)

    console = Console()
    console.print(table)

def cadastrar_cor():
    nome = questionary.text("Informe o nome da cor: ").ask()
    insert_color(nome)

def editar_cor():
    listaCores = get_all_colors()

    if len(listaCores) == 0:
        print("Nenhuma cor cadastrada!")
        return

    opcoes_para_escolher = []
    for cor in listaCores:
        opcao = questionary.Choice(title=cor.nome, value=cor.id)
        opcoes_para_escolher.append(opcao)
    
    id_cor_escolhida = questionary.select(
        "Escolha a cor que deseja editar?",
        choices=opcoes_para_escolher
    ).ask()

    novo_nome = questionary.text("Informe o novo nome da cor: ").ask()
    update_color(id_cor_escolhida, novo_nome)
     
def apagar_cor():
    listaCores = get_all_colors()

    if len(listaCores) == 0:
        print("Nenhuma cor cadastrada!")
        return

    opcoes_para_escolher = []
    for cor in listaCores:
        opcao = questionary.Choice(title=cor.nome, value=cor.id)
        opcoes_para_escolher.append(opcao)
    
    id_cor_escolhida = questionary.select(
        "Escolha qual COR deseja excluir: ",
        choices=opcoes_para_escolher
    ).ask()

    delete_color(id_cor_escolhida)