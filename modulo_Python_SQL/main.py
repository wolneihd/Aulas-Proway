import mysql.connector;
from dotenv import load_dotenv
import os
import questionary
from rich.console import Console
from rich.table import Table

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acesse as variáveis usando os.environ
db_user = os.getenv('BD_USER')
db_password = os.getenv('BD_PASSWORD')
db_port = os.getenv('BD_PORT')
db_host = os.getenv('BD_HOST')

# configurações do BD como um dicionário
config = {
    'host': db_host,
    'port': db_port,
    'user': db_user,
    'password': db_password,
    'database': 'dev_motors'
}

def inserir_marca():
    conexao = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password
    )
    cursor = conexao.cursor()
    cursor.execute('USE dev_motors')

    nome = questionary.text("Informe a marca: ").ask()
    cnpj = questionary.text("Informe ao CNPJ: ").ask()

    query = f'INSERT INTO marcas (nome, cnpj) VALUE ("{nome}","{cnpj}")'
    cursor.execute(query)
    conexao.commit()
    conexao.close(); print('INSERT com sucesso!')


def consultar_marcas():
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, cnpj FROM marcas')    
    registros = cursor.fetchall()

    # Imprimir os resultados
    table = Table(title="TABELA DE MARCAS")
    table.add_column("id", justify="right", style="cyan", no_wrap=True)
    table.add_column("nome", style="magenta")
    table.add_column("CNPJ", justify="right", style="green")
    for registro in registros:
        id, nome, cnpj = registro; 
        table.add_row(str(id),nome,cnpj)
    console = Console()
    console.print(table)

    cursor.close()
    conexao.close()


def atualizar_marca():
    pass


def apagar_marca():
    pass


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

if __name__ == "__main__":
    menu_marcas()