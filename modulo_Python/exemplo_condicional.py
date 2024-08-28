def exemplo_if():
    numero = int(input('Digite um número: '))
    if numero == 10:
        print('Dez', numero)
    elif numero == 11:
        print('Onze', numero)
    else:
        print('Você digitou outro número')

# operador relacional 
def exemplo_if_02(numero):
    if numero > 0:
        print(f'O número {numero} é positivo')
    elif numero ==0:
        print(f'O número {numero} é neutro')
    else:
        print(f'O número {numero} é negativo')


def exemplo_if_03(numero):
    text_format = {
        'negrito': ['\033[1m','\033[0m'],
        'vermelho': ['\033[31m','\033[0m']
    }    
    try:
        print(f'Este número {numero} é {"par" if numero % 2 == 0 else "ímpar"}.')
    except:
        print(f'O valor {text_format['vermelho'][0]}{numero}{text_format['vermelho'][1]} é inválido!')


def exemplo_if_04(quantidade):
    preco_unitario = 1_500.00
    desconto = 0
    try:
        if quantidade > 0:
            if quantidade >= 10 and quantidade <=19:
                desconto = 100
            elif quantidade >=20 and quantidade <=29:
                desconto = 250
            elif quantidade >=30 and quantidade <40:
                desconto = 400
            elif quantidade >=40: 
                desconto = 500
            print(f'Preço unitário: R$ {preco_unitario:.2f}')
            print(f'Desconto: R$ {preco_unitario:.2f}')    
            print(f'Quantidade: {quantidade} {"unidade" if quantidade == 1 else "unidades"}')    
            print(f'Total: R$ {quantidade * (preco_unitario - desconto):.2f}')
        else:
            print(f'Quantidade {quantidade} inválida')
    except:
        print(f'Tipo de dado "quantidade" {quantidade} inválida!')


def exemplo_if_or():
    categoria = input('Digite o nome da categoria: ').strip()
    if categoria == 'rpg' or categoria == 'souls like':
        print('sem vida')
    else:
        print('partiu minecraft')

exemplo_if()
exemplo_if_02(0)
exemplo_if_03('a')
exemplo_if_04('a')
exemplo_if_or()