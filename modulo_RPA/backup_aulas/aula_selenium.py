from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurações para o Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")  

driver = webdriver.Chrome(service=Service("./chromedriver.exe")  , options=chrome_options)

# Abre o site desejado
url = "https://www.folha.uol.com.br/"
driver.get(url)

# Mantém o navegador aberto por 10 segundos
driver.implicitly_wait(10)

elemento = driver.find_element(By.CLASS_NAME, "c-main-headline__title")
print(elemento.text)

is_nome_lula = 'lula' in elemento.text.lower()
print('Nome LULA encontrado na página' if is_nome_lula else 'Nome Lula não encontrado')

# Fecha o navegador
driver.quit()
