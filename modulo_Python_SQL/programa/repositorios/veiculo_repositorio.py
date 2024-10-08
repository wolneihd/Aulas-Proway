from typing import List
from database import conectar
from entidades import Veiculo

def obter_todos_veiculos() -> List[Veiculo]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(""" """)
    registros = cursor.fetchall()
    conexao.close()
    listaModelos: List[Veiculo] = []
    for registro in registros:
        id, nome_modelo, id_marca, marcas_id, nome_marca, cnpj = registro
        listaModelos.append(registro)
    return listaModelos

def cadastrar_veiculo(id_proprietario, id_versao, id_cor, preco_inicial, preco_fipe, km, chassi, placa, renavam, ano_fabricacao, ano_modelo, novo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO veiculos (id_proprietario, id_versao, id_cor, preco_inicial, preco_fipe,km,chassi,placa,renavam,ano_fabricacao,ano_modelo,novo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                   (id_proprietario, id_versao, id_cor, preco_inicial, preco_fipe, km, chassi, placa, renavam, ano_fabricacao, ano_modelo, novo))
    conexao.commit()
    conexao.close()