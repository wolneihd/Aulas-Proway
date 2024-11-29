import os
import random

def funcao01():
    # lista arquivos numa pasta:
    arquivos = os.listdir()
    for arquivo in arquivos:
        print(arquivo)

def funcao02():
    # criar pasta 
    nova_pasta = 'projetos'
    os.makedirs(nova_pasta, exist_ok=True)

def funcao03():
    # gera .txt com um titulo com numero aleatório de 1 a 99.
    nome = f'arquivo_{random.randint(1,99)}.txt'
    caminho_arquivo = os.path.join('projetos', nome)
    with open(caminho_arquivo, 'w') as f:
        f.write('oi') 

if __name__ == "__main__":
    funcao02()
    for i in range(5):
        funcao03()