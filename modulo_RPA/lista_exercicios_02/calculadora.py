import pyautogui

numero01 = pyautogui.prompt('Digite o número 01:')
numero02 = pyautogui.prompt('Digite o número 02:')
operacao = pyautogui.confirm('Escolha a operação', buttons=["+", "-", "*", "/"])

try:
    if operacao == '+':
        pyautogui.alert(f'{int(numero01)} + {int(numero02)} = {int(numero01) + int(numero02)}')
    elif operacao == '-':
        pyautogui.alert(f'{int(numero01)} - {int(numero02)} = {int(numero01) - int(numero02)}')
    elif operacao == '*':
        pyautogui.alert(f'{int(numero01)} * {int(numero02)} = {int(numero01) * int(numero02)}')
    elif operacao == '/':
        pyautogui.alert(f'{int(numero01)} / {int(numero02)} = {int(numero01) / int(numero02)}')
except Exception as error:
    pyautogui.alert(f'Erro ao fazer a operação')