import random
import pyautogui

numero = random.choice(range(1,11))
print(numero)

while True:    
    try: 
        resposta = pyautogui.prompt('Digite um número: ')

        if resposta == None:
            pyautogui.alert('Você saiu.')
            break

        if numero == int(resposta):
            pyautogui.alert('Parabéns! Você acertou!')
            break  
        
    except:
        print('Valor informado não permitido. Deve ser de 1 até 10.')

