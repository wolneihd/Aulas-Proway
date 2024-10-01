from typing import List

from database import conectar
from entidades import Modelo


def cadastrar(id_marca: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO modelos (id_marca, nome) VALUES (%s,%s)",(id_marca,nome))
    conexao.commit()
    conexao.close()


def atualizar(id: int, nome: str):
    pass


def obter_todos_modelos() -> List[Modelo]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT 
	    modelos.id,
	    marcas.nome,
        modelos.nome
	FROM modelos
    INNER JOIN marcas ON marcas.id = modelos.id_marca;
    """)
    registros = cursor.fetchall()

    listaModelos: List[Modelo] = []
    for registro in registros:
        id, marca, modelo = registro
        veiculo = Modelo(id, marca, modelo)
        listaModelos.append(veiculo)

    conexao.close()
    return listaModelos


def apagar(id: int):
    pass
