from typing import List

reset = "\033[0m"
vermelho = "\033[31m"
verde = "\033[32m"

class Aluno:
    def __init__(self, id:int, nome:str, nota1:float, nota2:float, nota3:float):
        self.id = id
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def mediaAluno(self):
        return (self.nota1 + self.nota2 + self.nota3)/3
    
    def validarNota(self):
        media = self.mediaAluno()
        if (media >= 7):
            print(f"{verde}{self.nome} está aprovado{reset}")
        else:
            print(f"{vermelho}{self.nome} está reprovado{reset}")

listaAlunos: List[Aluno] = []
for aluno in range(0,3):
    id = input("Digite o id do aluno: ")
    nome = input("Digite o nome do aluno: ")
    nota1 = input("Digite nota 01: ")
    nota2 = input("Digite nota 02: ")
    nota3 = input("Digite nota 03: ")
    novoAluno = Aluno(int(id), nome, float(nota1), float(nota2), float(nota3))
    listaAlunos.append(novoAluno)

for aluno in listaAlunos:
    print(f"média: {aluno.mediaAluno():.2f}")
    aluno.validarNota()

