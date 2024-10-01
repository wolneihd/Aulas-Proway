import questionary
from repositorios.marca_repositorio import obter_todas_marcas
from repositorios.modelo_repositorio import cadastrar, obter_todos_modelos
import os
from rich.console import Console
from rich.table import Table

def limpar_tela():
    os.system("cls")

def menu_modelos():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Modelos",
        choices=[
            "Consultar",
            "Cadastrar",
            "Editar",
            "Apagar",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar":
            consultar_modelos()
        elif opcao_escolhida == "Cadastrar":
            inserir_modelo()
        elif opcao_escolhida == "Editar":
            pass
        elif opcao_escolhida == "Apagar":
            pass

def inserir_modelo():
    marcas = obter_todas_marcas()

    if len(marcas) == 0:
        print("Nenhuma marca cadastrada!")
        return

    opcoes_para_escolher = []
    for marca in marcas:
        opcao = questionary.Choice(title=marca.nome, value=marca.id)
        opcoes_para_escolher.append(opcao)
    
    id_marca_escolhida = questionary.select(
        "Escolha a marca que deseja editar",
        choices=opcoes_para_escolher
    ).ask()

    nome = questionary.text("Informe o nome do modelo: ").ask()
    cadastrar(id_marca_escolhida, nome)

    print("Marca cadastrada com sucesso")

def consultar_modelos():
    registros = obter_todos_modelos()
    if len(registros) == 0:
        print("Nenhuma marca cadastrada!")
        return
    
    table = Table(title="Consulta de Marcas")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Marca", justify="center", style="magenta")
    table.add_column("Modelo", justify="center", style="green")

    for registro in registros:
        table.add_row(str(registro.id), registro.marca, registro.nome)

    console = Console()
    console.print(table)