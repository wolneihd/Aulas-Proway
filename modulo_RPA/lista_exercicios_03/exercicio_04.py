# Verificador de Números Primos 
# Escreva uma função que verifique se um número é primo. 
# ●  Implemente um algoritmo eficiente que verifique divisibilidade até a raiz 
# quadrada do número. 
# ●  Use um loop for com range() para testar os possíveis divisores. 
# ●  Retorne False imediatamente se encontrar um divisor. 

import pyautogui
import math

num = int(input('Digite um número: '))
is_divisivel = False

for numero in range(2,10):
    if (num % numero) == 0:
        print(f'divisivel por {numero}')
        is_divisivel = True

if is_divisivel:
    print('Este número não é primo!')
else:
    print('Este número é primo!')