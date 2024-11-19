import pyautogui
import webbrowser
import time

def login_automatico(usuario: str, senha: str):
    webbrowser.open('login-html.html')
    time.sleep(3)
    # busca o campo LOGIN e clica sobre ele
    campo_login = pyautogui.locateOnScreen('campo_login.png', confidence=0.8)
    if campo_login:
        pyautogui.click(campo_login)
        pyautogui.typewrite(usuario)
    else:
        print('Campo login não encontrado!')
        return
    pyautogui.press('tab')
    pyautogui.write(senha)
    # busca o campo ENTRAR e clica sobre ele
    campo_entrar = pyautogui.locateOnScreen('campo_entrar.png', confidence=0.8)
    if campo_entrar:
        pyautogui.click(campo_entrar)
    else:
        print('Campo entrar não encontrado!')
        return


if __name__ == "__main__":
    login_automatico('wolneihd@hotmail.com', '123456')