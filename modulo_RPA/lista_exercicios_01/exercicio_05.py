# Crie um conversor entre Celsius e Fahrenheit. 
# - Implemente funções para converter de Celsius para Fahrenheit e vice-versa. 
# - Use as fórmulas: C = (F - 32) * 5/9 e F = (C * 9/5) + 32. 
# - Permita que o usuário escolha a direção da conversão.

import pyautogui

resposta = pyautogui.confirm(
    'Deseja calcular: \n\n1.Celsius para Fahrenheit \n2. Fahrenheit para Celcius', 
    buttons=['1', '2'])

while True:
    try:
        valor = pyautogui.prompt(f'Digite a temperatura em {'Celcius' if resposta == '1' else 'Fahrenheit'}:')
        valor = valor.replace(',','.')
        valor = float(valor)
        break
    except Exception as error:
        pyautogui.alert('Valor para temperatura informado é incorreto. Tentar novamente')

if resposta == '1':
    pyautogui.alert(f'O valor {valor}°C em Fahrenheit é {(9/5)*valor + 32}°F')
else:
    pyautogui.alert(f'O valor {valor}°F em Celcius é {(valor-32)*(5/9)}°C')