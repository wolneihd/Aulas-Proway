from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

# Configurações para o Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")  

driver = webdriver.Chrome(service=Service("./chromedriver.exe")  , options=chrome_options)

# Abre o site desejado
url = 'https://rpachallenge.com/'
driver.get(url)

# Mantém o navegador aberto por 10 segundos
driver.implicitly_wait(10)
html_completo = driver.page_source

soup = BeautifulSoup(html_completo, features='html.parser')
all_inputs = soup.find_all("input")

for input in all_inputs:
    if 'labelFirstName' in str(input):
        print(input)

# first_name = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[5]/rpa1-field/div/input")
# first_name.send_keys('wolnei')

# campo_login = driver.find_element(By.ID, "usuario")
# campo_senha = driver.find_element(By.ID, "senha")
# botao_login = driver.find_element(By.XPATH, "/html/body/div/form/button")

# time.sleep(2)
# campo_login.send_keys('ALUNOS')
# campo_senha.send_keys('SUPERDEV')

# time.sleep(2)
# botao_login.click()

# Fecha o navegador
time.sleep(2)
driver.quit()
