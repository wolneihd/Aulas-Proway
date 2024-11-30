# tiver que pedir ajuda com o Chatgpt neste caso.
# o open estava dando erro de não encontrar o arquivo.
# segundo ele --> OneDrive: Às vezes, o OneDrive sincroniza ou move os arquivos para um diretório diferente.
# restante do código feito por mim.
import pyautogui

arquivo = open(r'C:\Users\alzir\OneDrive\Área de Trabalho\Super DEV\Aulas-Proway\modulo_RPA\lista_exercicios_01\arquivo.txt', mode='r')

total_palavras = 0
for line in arquivo:
    total_palavras = total_palavras + len(line.split(' '))

pyautogui.alert(f'O total de palavras no arquivo.txt é de {total_palavras} palavras.')