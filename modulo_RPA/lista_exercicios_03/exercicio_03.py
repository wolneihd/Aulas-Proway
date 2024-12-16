import pyautogui
import math

ano = pyautogui.prompt('Digite o ano: ')

romano = ''
try:
    ano = int(ano)
    if ano >= 1000:
        inteiro = math.trunc(ano/1000)
        ano = ano-(inteiro*1000)
        for numero in range(0,inteiro):
            romano += 'M'
    if ano >= 500:
        inteiro = math.trunc(ano/500)
        ano = ano-(inteiro*500)
        for numero in range(0,inteiro):
            romano += 'D'
    if ano >= 100:
        inteiro = math.trunc(ano/100)
        ano = ano-(inteiro*100)
        for numero in range(0,inteiro):
            romano += 'C'
    if ano >= 50:
        inteiro = math.trunc(ano/50)
        ano = ano-(inteiro*50)
        for numero in range(0,inteiro):
            romano += 'C'
    if ano >= 10:
        inteiro = math.trunc(ano/10)
        ano = ano-(inteiro*10)
        for numero in range(0,inteiro):
            romano += 'C'
    if ano >= 5:
        inteiro = math.trunc(ano/5)
        ano = ano-(inteiro*5)
        for numero in range(0,inteiro):
            romano += 'C'
    else:
        for numero in range(0,ano):
            romano += 'I'

except Exception as error:
    pass

pyautogui.alert(f'Conversão para romanos ficou: {romano}')




