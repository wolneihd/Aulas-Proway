from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Motorola g55
# Configurações para o Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")  

driver = webdriver.Chrome(service=Service("./chromedriver.exe")  , options=chrome_options)

load_dotenv()
AMAZON = os.getenv('AMAZON')
MOTOROLA = os.getenv('MOTOROLA')

# Abre o site desejado
driver.get(AMAZON)

# Mantém o navegador aberto por 10 segundos
driver.implicitly_wait(5)

try:
    valor_amazon = driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/div/div/div/span[1]/span[2]/span[2]')
    valor_amazon = valor_amazon.text
    valor_amazon = str(valor_amazon)
    valor_amazon = valor_amazon.replace('.','')
    valor_amazon = int(valor_amazon)
    print(valor_amazon, type(valor_amazon))
except Exception as error:
    print('erro: ', error)

# soup = BeautifulSoup(html_completo, features='html.parser')
# table = soup.find("table")
# print(table)

# print('... gerar o CSV ...')
# try:
#     with open('feriados.csv', mode='w', encoding="utf-8") as arquivo:
#         arquivo.write(f'data,nome,observacao\n')
#         for linha in table.find_all('tr')[1:]:
#             cols = linha.find_all('td')
#             data = str(cols[0].text)
#             nome = str(cols[1].text)
#             observacao = str(cols[2].text)
#             arquivo.write(f'{data.replace(' de ','/').replace('º','')},{nome},{observacao.replace(',','-')}')       
# except Exception as error:
#     print('Erro ao gerar CSV: ', error)

# # Fecha o navegador
# print('... finalizado ...')
# driver.quit()
