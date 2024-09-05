# Exericio 01

class Usuario():
    def __init__(self, nome, idade, qtd_anos_empresa):
        self.nome = nome
        self.idade = idade
        self.qtd_anos_empresa = qtd_anos_empresa

    def apresentar_bonus(self):
        if self.qtd_anos_empresa >= 15:
            print(f'O {self.nome} com {self.idade} anos tem direito a bônus de R$ 15.000,00')
        elif self.qtd_anos_empresa >= 10:
            print(f'O {self.nome} com {self.idade} anos tem direito a bônus de R$ 8.000,00')
        elif self.qtd_anos_empresa >= 7:
            print(f'O {self.nome} com {self.idade} anos tem direito a bônus de R$ 5.000,00')
        elif self.qtd_anos_empresa >= 3:
            print(f'O {self.nome} com {self.idade} anos tem direito a bônus de R$ 3.000,00')
        else:
            print(f'O {self.nome} com {self.idade} anos tem direito a bônus de R$ 150,00')

# pessoa_01 = Usuario('Wolnei',33,7) 
# pessoa_01.apresentar_bonus()

# Exericio 02
def exercicio_02(tipo, valor):
    if tipo.lower() == 'c':
        print(f'{valor}ºC em Fahrenheit é {(valor * 1.8)+32}ºF')
    else:
        print(f'{valor}ºF em Celcius é {(valor -32 )/1.8}ºC')

# exercicio_02(tipo='f',valor=32)

# Exercicio 03:
import os
def exercicio_03():
    lista_pedido = []
    soma = 0
    cardapio = {
        'cachorro_quente': [100,1.20],
        'bauru': [101,1.3],
        'hamburguer':[103,1.2],
        'pao_com_bolinho': [104,1.3],
        'refrigerante': [105,1]
    }
    for vez in range(0,4):
        os.system('cls')
        for dado in cardapio:
            print(f"Produto: {dado} | código: {cardapio[dado][0]} | valor: {cardapio[dado][1]}")
        pedido = int(input('Digite o código do produto desejado: '))
        lista_pedido.append(pedido)  
    os.system('cls') 
    for codigo in lista_pedido:
        for dado in cardapio:
            if cardapio[dado][0] == codigo:
                soma += cardapio[dado][1]
                print(f'Pedido: {dado}, Valor: {cardapio[dado][1]:.2f}')
    print(f'O Total no final foi de R$ {soma:.2f}')

# exercicio_03()

def exercicio_04(numero):
    if numero <= 100 and numero >= -100:
        print(f'Número {numero} está no intervalo de -100 e 100.')
    else:
        print(f'Número NÃO está no intervalo de -100 e 100!')

# exercicio_04(-100)

def exercicio_05(array_notas):
    soma = 0
    for nota in array_notas:
        soma += nota
    media=soma/len(array_notas)
    if media>=7:
        print(f'Aluno aprovado com média: {media}')
    elif media<7 and media >=5:
        print(f'Aluno em exame com média: {media}')
    else:
        print(f'aluno reprovado com média: {media}')

# exercicio_05([5,5,7,8])

# exercicio_04(-100)

def exercicio_06(array_notas,frequencia):
    soma = 0
    for nota in array_notas:
        soma += nota
    media=soma/len(array_notas)
    if frequencia >= 75:
        if media>=7:
            print(f'Aluno aprovado com média: {media}')
        elif media<7 and media >=5:
            print(f'Aluno em exame com média: {media}')
        else:
            print(f'aluno reprovado com média: {media}')
    else:
        print('Aluno reprovado com frequência inferior a 75%')

exercicio_06([5,5,7,8],frequencia=60)