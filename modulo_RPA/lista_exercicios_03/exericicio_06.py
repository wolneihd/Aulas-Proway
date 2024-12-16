# Jogo da Forca Simples 
# Crie uma versão simples do jogo da forca. 
# ●  Defina uma lista de palavras possíveis. 
# ●  Escolha uma palavra aleatoriamente usando random.choice(). 
# ●  Use um conjunto (set) para armazenar as letras corretas adivinhadas. 
# ●  Implemente um loop principal que continue até o jogador ganhar ou 
# perder. 
# ●  Atualize a palavra exibida a cada tentativa, mostrando as letras 
# adivinhadas.

import random

lista = ['colher', 'garfo', 'faca', 'espátula', 'panela', 'tigela', 'batedeira', 'liquidificador', 'ralador', 'escorredor']
escolha = random.choice(lista)

tamanho = len(escolha)
secreto = ['*'] * tamanho
index = 0
print(escolha)

for letra in escolha:
    palavra = ''
    array_acertos = []
    letra = input('Digite a letra: ')
    if letra in escolha:
        for i, letter in enumerate(escolha):
            if letter == letra:
                array_acertos.append(i)
        for idx in array_acertos:
            secreto[idx] = escolha[idx]
        for letra in secreto:
            palavra += letra
        print(palavra)
