# Calculadora de Média e Desvio Padrão 
# Desenvolva um programa que calcule a média e o desvio padrão de uma lista de 
# números. 
# ●  Solicite ao usuário uma série de números. 
# ●  Use split() e list comprehension para converter a entrada em uma lista 
# de números. 
# ●  Calcule a média somando todos os números e dividindo pelo total de 
# elementos. 
# ●  Calcule o desvio padrão usando a fórmula matemática apropriada. 
# ●  Use o módulo math para calcular a raiz quadrada.

import pandas as pd
lista_numero = [15,16,17,21,25]

df = pd.Series(lista_numero)
print(df.describe().std())
