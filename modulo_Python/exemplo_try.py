# Aula 30 de Agosto de 2024
# Professor Francisco Sens

import os

def exemplo_try_catch():
    os.system('cls')
    try:
        numero = int(input('Digite um número: '))
        print('Número: ', numero)
    except Exception as error:
        print('Valor informado não é número nao é inteiro')
        print(error)


def exemplo_try_conversao_float():
    os.system('cls')
    red, reset = '\033[31m', '\033[0m'
    quantidade_horas, valor_hora = None, None
    try:
        while True:
            nome = input('Digite o nome do colaborador: ').strip()
            if nome.isnumeric():
                os.system('cls')
                print(f'{red}Nome inválido. Tentar novamente!{reset}')
            elif len(nome) == 0:
                os.system('cls')
                print(f'{red}Campo nome vazio. Tentar novamente!{reset}')
            else:
                break
        quantidade_horas = int(input('Digite a quantidade de horas: '))
        valor_hora = input('Digite o valor horas: ').replace(',','.')
        valor_hora = float(valor_hora)
        print(f'O colaborador {nome} deve receber R$ {quantidade_horas * valor_hora:.2f}')
    except ValueError as ve:
        if quantidade_horas is None:
            print(f'{red}Quantidade de Horas inválido!{reset}')
        elif not valor_hora.isnumeric():
            print(f'{red}Valor Hora inválido!{reset}')
    except Exception as e:
        print(f'{red}Ocorreu um erro inesperado: {e}{reset}')


exemplo_try_catch()
exemplo_try_conversao_float()