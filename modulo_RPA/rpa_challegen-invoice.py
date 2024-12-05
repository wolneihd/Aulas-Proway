from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from contador import contador_segundos
from matplotlib import pyplot as plt
import cv2

# Configurações para o Chrome em modo headless
chrome_options = Options()
# chrome_options.add_argument("--headless") 
# chrome_options.add_argument("--disable-gpu")  

driver = webdriver.Chrome(service=Service("./chromedriver.exe")  , options=chrome_options)

# Abre o site desejado
driver.get('https://rpachallengeocr.azurewebsites.net/invoices/4.jpg')
driver.save_screenshot('invoice_01.png')

image = cv2.imread('path/to/your/image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# https://medium.com/@siromermer/extracting-text-from-images-ocr-using-opencv-pytesseract-aa5e2f7ad513

