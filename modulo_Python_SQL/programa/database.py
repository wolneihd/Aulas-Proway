import mysql.connector;
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acesse as variáveis usando os.environ
db_user = os.getenv('BD_USER')
db_password = os.getenv('BD_PASSWORD')
db_port = os.getenv('BD_PORT')
db_host = os.getenv('BD_HOST')
db_database = os.getenv('BD_DATABASE')

# configurações do BD como um dicionário
config = {
    'host': db_host,
    'port': db_port,
    'user': db_user,
    'password': db_password,
    'database': db_database
}

def conectar():
    conexao = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database
    )
    return conexao