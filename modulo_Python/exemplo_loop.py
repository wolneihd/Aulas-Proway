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

# chamando as funções:
# exemplo_while01()
exemplo_while02()