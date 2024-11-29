from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from contador import contador_segundos

# Motorola g55
# Configurações para o Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")  

driver = webdriver.Chrome(service=Service("./chromedriver.exe")  , options=chrome_options)

load_dotenv()
AMAZON = os.getenv('AMAZON')
MERCADO_LIVRE = os.getenv('MERCADO_LIVRE')

# Abre o site desejado
driver.get(AMAZON)

# Mantém o navegador aberto por 10 segundos
contador_segundos(segundos=10)

try:
    valor_amazon = driver.find_element(By.CLASS_NAME, 'a-price-whole')
    
    valor_amazon = valor_amazon.text
    valor_amazon = str(valor_amazon)
    valor_amazon = valor_amazon.replace('.','')
    valor_amazon = int(valor_amazon)
    print(valor_amazon)

    nome_modelo_amazon = driver.find_element(By.ID, 'productTitle')
    nome_modelo_amazon = str(nome_modelo_amazon.text)
    print(nome_modelo_amazon)

except Exception as error:
    print('erro: ', error)

# Abre o site desejado
print('... ABRINDO MERCADO_LIVRE ...')
driver.get(MERCADO_LIVRE)

# Mantém o navegador aberto por 10 segundos
contador_segundos(segundos=10)

try:
    valor_ML = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]')
    
    valor_ML = valor_ML.text
    valor_ML = str(valor_ML)
    valor_ML = valor_ML.replace('.','')
    valor_ML = int(valor_ML)

    print('MERCADO LIVRE: ', valor_ML)

    nome_modelo_ML = driver.find_element(By.CLASS_NAME, 'ui-pdp-title')
    nome_modelo_ML = str(nome_modelo_ML.text)
    print(nome_modelo_ML)

except Exception as error:
    print('erro: ', error)

with open('motorola_g54.csv', mode='w', encoding="utf-8") as arquivo:
    arquivo.write(f'nome do modelo,valor\n')
    arquivo.write(f'{nome_modelo_amazon},{valor_amazon}\n')
    arquivo.write(f'{nome_modelo_ML},{valor_ML}\n')