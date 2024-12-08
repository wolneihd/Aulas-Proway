import pyautogui

texto = pyautogui.prompt('Digite o texto desejado:')

vogais = 0
consoantes = 0

for letra in texto:
    if letra in ['a','e','i','o','u']:
        vogais += 1
    elif letra in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        consoantes += 1

pyautogui.alert(f'o texto: {texto}\n\nVogais: {vogais}\nConsoantes: {consoantes}')