import pyautogui

# Calcule os juros usando a fórmula: Juros = Principal * Taxa * Tempo.

principal = pyautogui.prompt('Digite o valor principal: ')
taxa = pyautogui.prompt('Digite a taxa de juros: ')
tempo = pyautogui.prompt('Digite a quantidade de meses: ')

try:
    principal = float(principal)
    taxa = float(taxa) / 100
    tempo = int(tempo) 
    juros = principal * tempo * taxa
    montante = juros + principal
    pyautogui.alert(f'O total será de: R$ {montante:.2f}')
except Exception as error:
    print("Eror a calcular o valor.")


