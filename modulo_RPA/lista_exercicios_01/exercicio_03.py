# Organizador de Arquivos por Extensão 
# Escreva um programa que organize arquivos em um diretório por suas extensões. 
# - Use os.listdir() para listar arquivos no diretório. 
# - Extraia a extensão de cada arquivo com split(). 
# - Crie pastas para cada extensão com os.makedirs(). 
# - Mova os arquivos para as pastas correspondentes usando shutil.move(). 

import os
import shutil

arquivos = os.listdir()
tipos_arquivos = []

# pasta_origem = os.getcwd()
# arquivo_origem = os.path.join(pasta_origem, 'teste.txt')
# pasta_destino = os.path.join(pasta_origem, 'lista_exercicios_01')
# shutil.move(arquivo_origem, pasta_destino)

for arquivo in arquivos:
    try:
        nome_formato = arquivo.split('.')
        if nome_formato[1] in tipos_arquivos:
            pasta_origem = os.getcwd()
            arquivo_origem = os.path.join(pasta_origem, arquivo)
            pasta_destino = os.path.join(pasta_origem, nome_formato[1] , arquivo)
            shutil.move(arquivo_origem, pasta_destino)
        else:
            tipos_arquivos.append(nome_formato[1])
            os.makedirs(nome_formato[1])
            pasta_origem = os.getcwd()
            arquivo_origem = os.path.join(pasta_origem, arquivo)
            pasta_destino = os.path.join(pasta_origem, nome_formato[1] , arquivo)
            shutil.move(arquivo_origem, pasta_destino)
    except Exception as error:
        print(f'Arquivo {arquivo} sem formato.')