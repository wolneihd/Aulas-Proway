# Gerador de Lista de Compras 
# Crie um script que gere uma lista de compras aleatória e a salve em um arquivo 
# CSV. 
# - Defina uma lista de itens possíveis. 
# - Use random.sample() para selecionar itens aleatoriamente. 
# - Utilize o módulo csv para escrever a lista em um arquivo CSV. 
# - Implemente funções separadas para gerar a lista e salvar o arquivo.

import random

compras_cozinha = [
    "Panela de pressao",
    "Jogo de talheres",
    "Conjunto de pratos",
    "Liquidificador",
    "Batedeira",
    "Faqueiro",
    "Tabua de corte",
    "Espremedor de frutas",
    "Conjunto de panelas",
    "Cafeteira"
]

def gerar_lista_sem_repetidos() -> list:
    objetos_selecionados = [] 
    contador = 1
    while contador<=5:
        index = random.randint(0,9)
        if compras_cozinha[index] in objetos_selecionados:
            pass
        else:
            objetos_selecionados.append(compras_cozinha[index])
            contador+=1
    return objetos_selecionados

def gerar_arquivo_csv(objetos:list):
    with open('lista_compra.csv', mode='w') as arquivo:
        for objeto in objetos:
            arquivo.write(f'{objeto}\n')

if __name__ == "__main__":
    cinco_objetos = gerar_lista_sem_repetidos()
    gerar_arquivo_csv(cinco_objetos)