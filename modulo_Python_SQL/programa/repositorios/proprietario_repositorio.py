from typing import List
from database import conectar
from entidades import Proprietario

def get_all_owners() -> List[Proprietario]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM proprietarios;")
    registros = cursor.fetchall()

    listaProprietarios: List[Proprietario] = []
    for proprietario in registros:
        id, nome, cpf_cnpj, data, email, telefone, estado, cidade, bairro, logradouro, cep, numero, complemento = proprietario
        novoProprietario = Proprietario(id, nome, cpf_cnpj, data, email, telefone, estado, cidade, bairro, logradouro, cep, numero,complemento)
        listaProprietarios.append(novoProprietario)

    conexao.close()
    return listaProprietarios

def insert_owner(nome, cpf_cnpj, data_nascimento, email, celular, estado, cidade, bairro, logradouro, cep, numero, complemento):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO proprietarios (nome, cpf_cnpj, data_nascimento, email, celular, estado, cidade, bairro, logradouro, cep, numero, complemento) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (nome, cpf_cnpj, data_nascimento, email, celular, estado, cidade, bairro, logradouro, cep, numero, complemento))
    conexao.commit() 
    conexao.close()

def update_owner(id:int, campo_alterado: str, novo_dado: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE proprietarios SET {campo_alterado} = %s WHERE id = %s;", (novo_dado, id))
    conexao.commit()
    conexao.close()

def delete_owner(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM proprietarios WHERE id = %s', (id,))
    conexao.commit() 
    conexao.close() 

if __name__ == "__main__":
    get_all_owners()