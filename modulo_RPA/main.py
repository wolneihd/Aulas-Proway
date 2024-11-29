from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

# Configurações para o Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")  

driver = webdriver.Chrome(service=Service("./chromedriver.exe")  , options=chrome_options)

# Abre o site desejado
url = "https://pt.wikipedia.org/wiki/Brasil"
driver.get(url)

# Mantém o navegador aberto por 10 segundos
driver.implicitly_wait(10)

elemento = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[113]/table')
html_completo = elemento.get_attribute("outerHTML")

soup = BeautifulSoup(html_completo, features='html.parser')
table = soup.find("table")
print(table)

print('... gerar o CSV ...')
try:
    with open('feriados.csv', mode='w', encoding="utf-8") as arquivo:
        arquivo.write(f'data,nome,observacao\n')
        for linha in table.find_all('tr')[1:]:
            cols = linha.find_all('td')
            data = str(cols[0].text)
            nome = str(cols[1].text)
            observacao = str(cols[2].text)
            arquivo.write(f'{data.replace(' de ','/').replace('º','')},{nome},{observacao.replace(',','-')}')       
except Exception as error:
    print('Erro ao gerar CSV: ', error)

# Fecha o navegador
print('... finalizado ...')
driver.quit()
