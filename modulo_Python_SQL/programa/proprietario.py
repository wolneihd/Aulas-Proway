from typing import List
import questionary
import os
from rich.console import Console
from rich.table import Table
from repositorios.proprietario_repositorio import get_all_owners, update_owner, insert_owner, delete_owner


def limpar_tela():
    os.system("cls")


def menu_proprietarios():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Proprietarios",
        choices=[
            "Consultar",
            "Cadastrar",
            "Editar",
            "Apagar",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar":
            consultar_proprietarios()
        elif opcao_escolhida == "Cadastrar":
            inserir_proprietario()
        elif opcao_escolhida == "Editar":
            atualizar_proprietario()
        elif opcao_escolhida == "Apagar":
            excluir_proprietario()

def consultar_proprietarios():
    listaProprietarios = get_all_owners()

    if len(listaProprietarios) == 0:
        print("Nenhum proprietário na planilha!")
        return
    
    table = Table(title="Consulta de proprietarios")

    table.add_column("id", justify="center", style="cyan", no_wrap=True)
    table.add_column("nome", justify="center", style="magenta")
    table.add_column("cpf_cnpj", justify="center", style="green")
    table.add_column("data", justify="center", style="green")
    table.add_column("email", justify="center", style="green")
    table.add_column("telefone", justify="center", style="green")
    table.add_column("estado", justify="center", style="green")
    table.add_column("cidade", justify="center", style="green")
    table.add_column("logradouro", justify="center", style="green")
    table.add_column("cep", justify="center", style="green")
    table.add_column("numero", justify="center", style="green")
    table.add_column("complemento", justify="center", style="green")

    for registro in listaProprietarios:
        table.add_row(str(registro.id), registro.nome, registro.cpf_cnpj, str(registro.data_nascimento),
                      registro.email, registro.celular, registro.estado,registro.cidade, registro.logradouro,
                      registro.cep, registro.numero, registro.complemento)

    console = Console()
    console.print(table)


def atualizar_proprietario(): # update
    listaProprietarios = get_all_owners()

    if len(listaProprietarios) == 0:
        print("Nenhuma marca cadastrada!")
        return

    opcoes_para_escolher = []
    for proprietario in listaProprietarios:
        opcao = questionary.Choice(title=proprietario.nome, value=proprietario.id)
        opcoes_para_escolher.append(opcao)
    
    id_proprietario = questionary.select(
        "Escolha o que deseja alterar",
        choices=opcoes_para_escolher
    ).ask()

    opcoes = ["nome", "cpf_cnpj","data_nascimento", "email", "celular","estado","cidade","bairro","logradouro","cep","numero","complemento"]
    campo_alterado = questionary.select(
        "Escolha o que deseja alterar",
        choices=opcoes
    ).ask()

    novo_dado = questionary.text("Informe o novo dado: ").ask()

    update_owner(id_proprietario, campo_alterado, novo_dado)


def inserir_proprietario():
    nome = questionary.text("Informe o novo nome: ").ask()
    cpf_cnpj = questionary.text("Informe o novo cpf_cnpj: ").ask()
    data_nascimento = questionary.text("Informe o novo data_nascimento: ").ask()
    email = questionary.text("Informe o novo email: ").ask()
    celular = questionary.text("Informe o novo celular: ").ask()
    estado = questionary.text("Informe o novo estado: ").ask()
    cidade = questionary.text("Informe o novo cidade: ").ask()
    bairro = questionary.text("Informe o novo bairro: ").ask()
    logradouro = questionary.text("Informe o novo logradouro: ").ask()
    cep = questionary.text("Informe o novo cep: ").ask()
    numero = questionary.text("Informe o novo numero: ").ask()
    complemento = questionary.text("Informe o novo complemento: ").ask()

    insert_owner(nome, cpf_cnpj, data_nascimento, email, celular, estado, cidade, bairro, logradouro, cep, numero, complemento)

def excluir_proprietario():
    listaProprietarios = get_all_owners()

    if len(listaProprietarios) == 0:
        print("Nenhuma proprietário cadastrado!")
        return

    opcoes_para_escolher = []
    for proprietario in listaProprietarios:
        opcao = questionary.Choice(title=proprietario.nome, value=proprietario.id)
        opcoes_para_escolher.append(opcao)
    
    id_proprietario = questionary.select(
        "Escolha o que deseja excluir",
        choices=opcoes_para_escolher
    ).ask()

    delete_owner(id_proprietario)