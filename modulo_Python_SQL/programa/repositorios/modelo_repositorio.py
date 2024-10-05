from typing import List
from database import conectar
from entidades import Modelo, Marca


def cadastrar(id_marca: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO modelos (id_marca, nome) VALUES (%s,%s)",(id_marca,nome))
    conexao.commit()
    conexao.close()


def atualizar_modelo(id: int, id_marca: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE modelos SET id_marca = %s, nome = %s WHERE id = %s", (id_marca, nome, id))
    conexao.commit()
    conexao.close()


def obter_todos_modelos() -> List[Modelo]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT 
        modelos.id,
        modelos.nome,
        modelos.id_marca,
        marcas.id,
        marcas.nome,
        marcas.cnpj
        FROM modelos
        INNER JOIN marcas ON marcas.id = modelos.id_marca;
    """)
    registros = cursor.fetchall()
    conexao.close()

    listaModelos: List[Modelo] = []
    for registro in registros:
        id, nome_modelo, id_marca, marcas_id, nome_marca, cnpj = registro
        veiculo = Modelo(id, Marca(id_marca, nome_marca, cnpj),nome_modelo)
        listaModelos.append(veiculo)
    return listaModelos


def delete_modelo(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM modelos WHERE id = %s', (id,))
    conexao.commit() 
    conexao.close() 
