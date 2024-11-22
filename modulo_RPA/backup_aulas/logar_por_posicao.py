import pyautogui
import webbrowser
import time

def login_automatico(usuario: str, senha: str):
    webbrowser.open('login-html.html')
    time.sleep(3)
    pyautogui.click(724, 333)
    pyautogui.write(usuario)
    pyautogui.press('tab')
    pyautogui.write(senha)
    pyautogui.press('enter')

if __name__ == "__main__":
    login_automatico('wolneihd@hotmail.com', '123456')