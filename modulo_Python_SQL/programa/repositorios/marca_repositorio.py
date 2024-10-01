from typing import List
from entidades import Marca
from database import conectar

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

def cadastrar(nome:str, cnpj:str):
    conexao = conectar()

    cursor = conexao.cursor()
    cursor.execute("use dev_motors")

    cursor.execute("INSERT INTO marcas (nome, cnpj) VALUES (%s, %s);", nome, cnpj)
    conexao.commit() 
    conexao.close()

def atualizar(id:int, nome_editado:str, cnpj_editado:str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE marcas SET nome = %s, cnpj = %s WHERE id = %s", (nome_editado, cnpj_editado, id))
    conexao.commit()
    conexao.close()

def apagar(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM marcas WHERE id = %s', (id,))
    conexao.commit() 
    conexao.close() 