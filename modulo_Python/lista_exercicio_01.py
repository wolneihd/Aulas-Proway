# Vide PDF na pasta do projeto: Lista 01 Leia.pdf 

def exercicio_01(numero):
    try:
        print(f'O número dado é {numero}, seu antecessor é {numero-1} e o sucessor é {numero+1}.')
    except Exception as error:
        print('Houve erro ao reproduzir a função.')
        print(error)


def exercicio_02(litros, quantidade_anos, valor_por_litro):
    try:
        print(f'Quantidade de litros: {litros:.2f} {"litro" if litros == 1 else "litros"}')
        print(f'Quantidade de anos: {quantidade_anos} {"ano" if quantidade_anos == 1 else "anos"}')
        print(f'Valor por litro: R$ {valor_por_litro:.2f}')  
        print(f'Quantidade de litros consumidos: {litros * quantidade_anos} litro(s)')
        print(f'Valor total a ser pago: R$ {(litros * quantidade_anos) * valor_por_litro:.2f}')
    except Exception as error:
        print('Houve erro ao reproduzir a função.')
        print(error)


def exercicio_03(numero_1, numero_2):
    try:
        print(f'A soma de {numero_1} com {numero_2} é igual a {numero_1 + numero_2}')
        print(f'A subtração de {numero_1} com {numero_2} é igual a {numero_1 - numero_2}')
        print(f'A multiplicação de {numero_1} com {numero_2} é igual a {numero_1 * numero_2}')
        print(f'A divisão de {numero_1} com {numero_2} é igual a: {'Não é possível dividir por zero' if numero_2 == 0 else (numero_1/numero_2)}')
    except Exception as error:
        print('Houve erro ao reproduzir a função.')
        print(error)

def exercicio_04(numero):
    try:
        if numero.isnumeric():
            numero = int(numero)
            for index in range(1,11):
                print(f'{numero} x {index} = {numero * index}')
        else:
            print(f'O dado informado {numero} é inválido!')
    except Exception as error:
        print('Houve erro ao reproduzir a função.')
        print(error)


# Exericio 05
class Carro:
    def __init__(self, nome, valor, valor_parcela, qtd_parcelas):
        self.nome = nome
        self.valor = valor
        self.valor_parcela = valor_parcela
        self.qtd_parcelas = qtd_parcelas
    
    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Valor Parcela: R$ {self.valor_parcela:.2f}")
        print(f"Quantidade de parcelas: {self.qtd_parcelas}")
        print(f"Valor financiamento: R$ {self.qtd_parcelas * self.valor_parcela:.2f}")
        print(f"Diferença entre o valor total do financiamento e valor do carro: R$ {(self.qtd_parcelas * self.valor_parcela) - self.valor:.2f}")

def exericio_06(array_notas):
    soma = 0
    try: 
        for nota in array_notas:
            soma += nota
        media = soma/(len(array_notas))
        print(f'A média do aluno é: {media:.2}')
    except Exception as error:
        print('Houve erro ao reproduzir a função.')
        print(error)       
        

def exercicio_07():
    print(f'     *')
    print(f'    ***')
    print(f'   *****')
    print(f'  *******')
    print(f' *********')
    print(f'***********')


# Exericio 08:
class Despesas:
    def __init__(self, conta_luz, conta_agua, internet, valor_vivo, valor_oi, iptu, ipva, seguro_carro):
        self.conta_luz = conta_luz
        self.conta_agua = conta_agua
        self.internet = internet
        self.valor_vivo = valor_vivo
        self.valor_oi = valor_oi
        self.iptu = iptu
        self.ipva = ipva
        self.seguro_carro = seguro_carro

    def mostrar_despesas(self):
        print(f'Contas de telefone: R$ {self.valor_oi:.2f}, R$ {self.valor_vivo:.2f}')
        print(f'Impostos: R$ {self.iptu:.2f}, R$ {self.ipva:.2f}')
        print(f'Demais contas: R$ {self.conta_luz:.2f}, R$ {self.conta_agua:.2f}, R$ {self.internet:.2f}, R$ {self.seguro_carro:.2f}')
        print(f'Todas as despesas: R$ {self.conta_luz + self.conta_agua + self.internet + self.valor_oi + self.valor_vivo + self.seguro_carro + self.iptu + self.ipva:.2f}')

import copy
def exericio_09():
    # antes
    valor_01 = int(input('Digitei o número 01: '))
    valor_02 = int(input('Digitei o número 02: '))
    print(f'Valor 01 = {valor_01}')
    print(f'Valor 02 = {valor_02}')

    # depois
    array_copy = [copy.deepcopy(valor_01),copy.deepcopy(valor_02)]
    valor_01 = array_copy[1]
    valor_02 = array_copy[0]
    print(f'Valor 01 = {valor_01}')
    print(f'Valor 02 = {valor_02}')

def exercicio_10(ano_nascimento):
    print(f'Sua idade é {2024 - ano_nascimento}')

from datetime import datetime
def exercicio_11(dia,mes,ano):
    # Obter a data e hora atuais
    ano_atual = datetime.now().year


    # Exibir as informações
    print(f'Anos: {ano_atual - ano} anos')
    print(f'meses: {(12 - mes) + ((ano_atual - 1 - ano - 1 )*12) + mes} meses')
    print(f'dias: {((12 - mes) + ((ano_atual - 1 - ano - 1 )*12) + mes)*30} dias')
    print(f'dias: {(((12 - mes) + ((ano_atual - 1 - ano - 1 )*12) + mes)*30)*24} horas')


# Chamando as funções:

# exercicio_01(10)
# exercicio_02(250,2,1.75)
# exercicio_03(10,5)
# exercicio_04('11')]
# carro_01 = Carro('Fiat Palio', 10000, 1000, 12)
# carro_01.exibir_info()
# exericio_06([5.1,3,7,8])
# exercicio_07()
# pessoa_01 = Despesas(100,50,15,250,45,25,18,1250)
# pessoa_01.mostrar_despesas()
# exericio_09()
# exercicio_10(1991)
# exercicio_11(4,8,1991)