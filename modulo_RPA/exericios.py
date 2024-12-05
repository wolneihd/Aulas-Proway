import random
import pyautogui

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

retorno = random.sample(compras_cozinha, k=5)

texto = ''
for index, valor in enumerate(retorno):
    texto += f'{index+1} - {valor}\n'

resposta = pyautogui.alert(texto)

if resposta == 'OK':
    print('Programa finalizado com sucesso!')