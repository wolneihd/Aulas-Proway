from typing import List
from database import conectar
from entidades import Modelo, Marca, Versao

def obter_todas_versoes() -> List[Versao]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(""" SELECT * FROM versoes;""")
    registros = cursor.fetchall()
    conexao.close()
    listaModelos: List[Modelo] = []
    for registro in registros:
        id, nome_modelo, id_marca, marcas_id, nome_marca, cnpj = registro
        veiculo = Modelo(id, Marca(id_marca, nome_marca, cnpj),nome_modelo)
        listaModelos.append(veiculo)
    return listaModelos

def cadastrar_versao(id_modelo: int, nome: int, motor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO versoes (id_modelo, nome, motor) VALUES (%s, %s, %s)", (id_modelo, nome, motor))
    conexao.commit()
    conexao.close()