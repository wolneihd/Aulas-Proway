import random
import string
import pyautogui

tamanho = pyautogui.prompt('Digite o tamanho da senha desejada: ')

try:
    tamanho = int(tamanho)
    senha = ''
    valores = string.ascii_letters + string.digits + string.punctuation
    for valor in range(0, tamanho):
        senha += random.choice(valores)
    pyautogui.alert(f'A senha de {tamanho} caracteres foi gerada com sucesso: {senha}')
except Exception as e:
    pyautogui.alert('O valor informado não é permitido. Deve ser num numero do tipo inteiro.')
