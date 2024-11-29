import os
import random
import time
from datetime import datetime

def criar_arquivos_aleatorios(numero_arquivos, pasta_saida, tamanho_min, tamanho_max, data_modificacao):
    # Criar a pasta de saída se não existir
    os.makedirs(pasta_saida, exist_ok=True)

    # Converter a data de modificação para timestamp
    timestamp = time.mktime(data_modificacao.timetuple())

    for i in range(numero_arquivos):
        # Gerar nome de arquivo aleatório
        nome_arquivo = f"arquivo_{i+1}_{random.randint(1000, 9999)}.txt"
        caminho_arquivo = os.path.join(pasta_saida, nome_arquivo)

        # Gerar conteúdo aleatório
        tamanho = random.randint(tamanho_min, tamanho_max)
        conteudo = os.urandom(tamanho)

        # Escrever o arquivo
        with open(caminho_arquivo, 'wb') as f:
            f.write(conteudo)

        # Alterar a data de modificação do arquivo
        os.utime(caminho_arquivo, (timestamp, timestamp))

    print(f"{numero_arquivos} arquivos criados em '{pasta_saida}' com data de modificação {data_modificacao}")

# Configurações
numero_arquivos = 5
pasta_saida = 'entrada'
tamanho_min = 1024  # 1 KB
tamanho_max = 1048576  # 1 MB
data_modificacao = datetime(2024, 11, 10, 17, 0)  # Ano, mês, dia, hora, minuto

# Executar a função
criar_arquivos_aleatorios(numero_arquivos, pasta_saida, tamanho_min, tamanho_max, data_modificacao)