import pyautogui
import time
import os

def gerar_imagem_calculadora():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write("Calculadora")
    pyautogui.press("enter")
    time.sleep(2)

    os.makedirs("Imagens", exist_ok=True)
    screenshot = pyautogui.screenshot()
    screenshot.save('Imagens/imagem_calculadora.png')
    pyautogui.hotkey("alt","f4")

    pyautogui.alert('Print gerado com sucesso!')

# Chama a função para criar o arquivo e inserir o texto
if __name__ == "__main__":
    gerar_imagem_calculadora()