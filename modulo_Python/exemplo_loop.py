def exemplo_while01():
    indice = 0
    while indice <= 10:
        print(indice)
        indice+=1
    while indice>0:
        print(indice)
        indice-=1


def exemplo_while02():
    indice = 0
    while indice < 3:
        nome = input('Digite o nome: ').strip()
        sobrenome = input('Digite o sobrenome: ').strip()
        if sobrenome.lower() == "souza":
            print(f'Sobrenome é {sobrenome}')
        nome_completo = f'{nome} {sobrenome}'
        print(f'Nome completo: {nome_completo}')
        indice+=1


def exemplo_while_descobrir_media(quantidade_notas):
    lista_notas = []
    soma = 0
    while True:
        try:
            nota = int(input('Digite a nota: '))
            lista_notas.append(nota)
            if len(lista_notas) == quantidade_notas:
                for numero in lista_notas:
                    soma += numero          
                return soma/quantidade_notas
        except:
            return 'erro'
    

def exemplo_maior_valor(quantidade_notas):
    valor = int(input('Digite o valor: '))
    maior_valor = valor
    lista_valores = [maior_valor]
    while True:
        try:
            valor = int(input('Digite o valor: '))
            lista_valores.append(valor)
            if valor > maior_valor:
                maior_valor = valor
            if len(lista_valores) == quantidade_notas:
                return f'O maior valor informado é {maior_valor}'
        except:
            return 'erro'
        

def exemplo_menor_valor(quantidade_valores):
    valor = int(input('Digite o valor: '))
    menor_valor = valor
    lista_valores = [valor]
    while True:
        try:
            valor = int(input('Digite o valor: '))
            lista_valores.append(valor)
            if valor < menor_valor:
                menor_valor = valor
            if len(lista_valores) == quantidade_valores:
                return f'O menor valor informado é {menor_valor}'
        except:
            return 'erro'
        

def exemplo_condicao_usuario():
    lista_produtos = []
    while True:
        nome_produto = input("Digite o nome do produto: ")
        if nome_produto.lower() == 'sair':
            print(lista_produtos)
            return 'Usuário saiu!'
        lista_produtos.append(nome_produto)

# chamando as funções:

# exemplo_while01()
# exemplo_while02()
# resultado = exemplo_while_descobrir_media(5)
# resultado = exemplo_maior_valor(5)
# resultado = exemplo_menor_valor(5)
resultado = exemplo_condicao_usuario()
print(resultado)