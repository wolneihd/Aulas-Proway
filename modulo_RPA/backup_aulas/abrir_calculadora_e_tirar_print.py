from pywinauto.application import Application
from pywinauto import Desktop
from PIL import ImageGrab
import time

def abrir_calculadora_e_tirar_print():
    app = Application().start('calc.exe')
    time.sleep(1)
    calc = Desktop(backend="uia").Calculator
    calc.wait('visible',timeout=10)
    rect = calc.rectangle()
    screenshot = ImageGrab.grab(bbox=(rect.left, rect.top, rect.right, rect.bottom))
    screenshot.save("imagem.png")

if __name__ == "__main__":
    abrir_calculadora_e_tirar_print()