from typing import List

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"{self.nome} tem {self.idade} anos!")

    def validar_idade(self):
        if self.idade >= 18:
            print(f"{self.nome} é maior de idade!")
        else:
            print(f"{self.nome} é menor de idade!")

listaUsuarios: List[Pessoa] = []
while True:
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")
    novaPessoa = Pessoa(nome, int(idade))
    listaUsuarios.append(novaPessoa)
    resposta = input("Deseja continuar? [s]im - [n]ão: ")
    if resposta.lower() == 'n':
        break

for pessoa in listaUsuarios:
    pessoa.mostrar_dados()
    pessoa.validar_idade()