import pyautogui

frase = pyautogui.prompt('Digite a frase a ser verificada:')
frase = frase.lower().replace('é','e').replace('ã','a')

array = frase.split(' ')
localizado = False

for palavra in array:
    for palavra_invertida in array:
        inverter = ''
        for letra in palavra_invertida[::-1]:
            inverter += letra        
        if inverter in palavra and len(palavra_invertida) > 2:
            print(inverter, palavra, inverter in palavra and len(palavra_invertida) > 2)
            pyautogui.alert(f'{palavra} tem internamenta invertida a palavra {palavra_invertida} - É um Palindromo')
            localizado = True

if localizado == False:
    pyautogui.alert(f'A frase "{frase}" não possui Palindromo')
