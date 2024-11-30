# Calculadora de IMC 
# Desenvolva uma calculadora de Índice de Massa Corporal (IMC). 
# -  Solicite ao usuário seu peso e altura. 
# -  Calcule o IMC usando a fórmula: peso / (altura^2). 
# -  Implemente uma função para classificar o IMC. 
# -  Trate entradas inválidas (como altura zero).

import pyautogui

while True:
    try:
        peso = pyautogui.prompt('Digite seu peso (em kg)')
        peso = peso.replace(',','.')
        peso = float(peso)
        break
    except Exception as error:
        pyautogui.alert('Valor para peso informado incorreto. Tentar novamente')

while True:
    try:
        altura = pyautogui.prompt('Digite sua altura (em metros)')
        altura = altura.replace(',','.')
        altura = float(altura)
        if altura >= 3:
            pyautogui.alert('Valor para altura informado incorreto (maior que 3). Tentar novamente')
        elif altura <= 0:
            pyautogui.alert('Valor para altura informado incorreto (igual ou menor que zero). Tentar novamente')
        else:
            break
    except Exception as error:
        pyautogui.alert('Valor para altura informado incorreto. Tentar novamente')

imc = peso/(altura * altura)

if imc < 18.5:
    pyautogui.alert(f'IMC {imc:.2f} - Abaixo do peso: IMC menor que 18.5')
elif imc >= 18.5 and imc < 25:
    pyautogui.alert(f'IMC {imc:.2f} - Peso normal: IMC entre 18.5 e 24.9') 
elif imc >= 25 and imc < 30:
    pyautogui.alert(f'IMC {imc:.2f} - Sobrepeso: IMC entre 25.0 e 29.9') 
elif imc >= 30 and imc < 35:
    pyautogui.alert(f'IMC {imc:.2f} - Obesidade grau 1: IMC entre 30.0 e 34.9') 
elif imc >= 35 and imc < 40:
    pyautogui.alert(f'IMC {imc:.2f} - Obesidade grau 2: IMC entre 35.0 e 39.9') 
else:
    pyautogui.alert(f'IMC {imc:.2f} - Obesidade grau 3: IMC de 40 ou mais (obesidade mórbida)') 