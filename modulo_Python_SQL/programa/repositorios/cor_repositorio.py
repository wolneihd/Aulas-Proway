from typing import List
from entidades import Cor
from database import conectar

def get_all_colors() -> List[Cor]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM cores;")
    registros = cursor.fetchall()

    listaCores: List[Cor] = []
    for cor in registros:
        id, nome = cor
        veiculo = Cor(id, nome)
        listaCores.append(veiculo)

    conexao.close()
    return listaCores

def insert_color(nome:str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO cores (nome) VALUE (%s);", (nome,))
    conexao.commit() 
    conexao.close()

def update_color(id:int, novo_nome_cor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE cores SET nome = %s WHERE id = %s", (novo_nome_cor, id))
    conexao.commit()
    conexao.close()

def delete_color(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM cores WHERE id = %s', (id,))
    conexao.commit() 
    conexao.close() 