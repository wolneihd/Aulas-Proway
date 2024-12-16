import pandas as pd
import pyautogui as pyg

ano = pyg.prompt("Digite o ano a ser verificado: ")

try:
    ano = int(ano)
    data = f"{ano}-01-01"
    print(data)
    idx = pd.date_range(data, freq="YE")    
    print(idx.is_leap_year)
except Exception as error:
    print('Valor incoerente pra verificação.')
