from typing import List
import questionary
import os
from rich.console import Console
from rich.table import Table

from database import conectar
from modelos import Marca


def limpar_tela():
    os.system("cls")


def menu_marcas():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Marcas",
        choices=[
            "Consultar marcas",
            "Cadastrar marca",
            "Editar marca",
            "Apagar marca",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar marcas":
            consultar_marcas()
        elif opcao_escolhida == "Cadastrar marca":
            inserir_marca()
        elif opcao_escolhida == "Editar marca":
            atualizar_marca()
        elif opcao_escolhida == "Apagar marca":
            apagar_marca()


def inserir_marca(): # create
    nome = questionary.text("Informe o nome da marca: ").ask()
    cnpj = questionary.text("Informe o CNPJ: ").ask()

    conexao = conectar()
    print("Conectado com sucesso")

    cursor = conexao.cursor()
    cursor.execute("use dev_motors")
    cursor.execute(f"INSERT INTO marcas (nome, cnpj) VALUES ('{nome}', '{cnpj}');")
    conexao.commit() # Efetuar a transação
    conexao.close() # Fechar a conexão com o banco de dados
    print("Marca cadastrada com sucesso")

def obter_todas_marcas() -> List[Marca]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cnpj FROM marcas")
    registros = cursor.fetchall()

    listaMarcas: List[Marca] = []
    for registro in registros:
        id, nome, cnpj = registro
        veiculo = Marca(id,nome,cnpj)
        listaMarcas.append(veiculo)

    conexao.close()
    return listaMarcas


def consultar_marcas(): # read
    registros = obter_todas_marcas()

    table = Table(title="Consulta de Marcas")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", justify="center", style="magenta")
    table.add_column("CNPJ", justify="center", style="green")

    for registro in registros:
        table.add_row(str(registro.id), registro.nome, registro.cnpj)

    console = Console()
    console.print(table)


def atualizar_marca(): # update
    marcas = obter_todas_marcas()

    opcoes = []
    for marca in marcas:
        opcao = questionary.Choice(title=marca.nome, value=marca.id)
        opcoes.append(opcao)

    nome_marca = questionary.select(
        "Escolha a marca a atualizar",
        choices=opcoes,
    ).ask()
    novo_nome = questionary.text("Insira o novo nome da Marca: ").ask()

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f'UPDATE marcas SET nome = "{novo_nome}" WHERE id={nome_marca}')
    conexao.commit()
    conexao.close()


# https://dontpad.com/franciscosensaulas/python
def apagar_marca(): # delete
    # Consultar todas as marcas
    marcas = obter_todas_marcas()

    # Criar um vetor com as marcas para o usuário poder escolher a marca que deseja apagar
    opcoes = []
    for marca in marcas:
        opcoes.append(marca.nome)

    # perguntando para o usuário qual marca ele deseja apagar
    marca_apagar = questionary.select(
        "Escolha a marca para apagar",
        choices=opcoes,
    ).ask()
    # Abrir a conexão
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f'DELETE FROM marcas WHERE nome = "{marca_apagar}"')
    conexao.commit() # Efetuar a transação
    conexao.close() # Fechar a conexão com o banco de dados


if __name__ == "__main__":
    menu_marcas()
