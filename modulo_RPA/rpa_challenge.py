import pyautogui
import webbrowser
import time
import pandas
import json
import random

class Usuario:
    def __init__(self, first_name, last_name, address, email, company, phone, role):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.company = company
        self.phone = phone
        self.role = role

def dados_usuario():
    dados = pandas.read_excel('challenge.xlsx')
    dados_json = dados.to_json(orient='records')
    dados_lista = json.loads(dados_json)
    aleatorio = random.randint(0, 9)

    first_name = dados_lista[aleatorio]['First Name']
    address = dados_lista[aleatorio]['Address']
    email = dados_lista[aleatorio]['Email']
    company = dados_lista[aleatorio]['Company Name']
    role = dados_lista[aleatorio]['Role in Company']
    last_name = dados_lista[aleatorio]['Last Name']
    phone = dados_lista[aleatorio]['Phone Number']    

    usuario = Usuario(first_name, last_name, address, email, company, phone, role)
    return usuario    

def preencher_formulario(usuario: Usuario):
    webbrowser.open('https://rpachallenge.com/')

    try:
        time.sleep(3)
        campo_address = pyautogui.locateOnScreen('address.png', confidence=0.8)
        if campo_address:
            pyautogui.click(campo_address)
            pyautogui.typewrite(usuario.address)
        else:
            print('Campo login não encontrado!')
            return

        time.sleep(1)
        email = pyautogui.locateOnScreen('email.png', confidence=0.8)
        if email:
            pyautogui.click(email)
            pyautogui.typewrite(usuario.email)
        else:
            print('Campo login não encontrado!')
            return

        time.sleep(1)
        first_name = pyautogui.locateOnScreen('first_name.png', confidence=0.8)
        if first_name:
            pyautogui.click(first_name)
            pyautogui.typewrite(usuario.first_name)
        else:
            print('Campo login não encontrado!')
            return

        time.sleep(1)
        last_name = pyautogui.locateOnScreen('last_name.png', confidence=0.8)
        if last_name:
            pyautogui.click(last_name)
            pyautogui.typewrite(usuario.last_name)
        else:
            print('Campo login não encontrado!')
            return

        time.sleep(1)
        role = pyautogui.locateOnScreen('role.png', confidence=0.8)
        if role:
            pyautogui.click(role)
            pyautogui.typewrite(usuario.role)
        else:
            print('Campo login não encontrado!')
            return

        time.sleep(1)
        phone = pyautogui.locateOnScreen('phone.png', confidence=0.8)
        if phone:
            pyautogui.click(phone)
            pyautogui.typewrite(str(usuario.phone))
        else:
            print('Campo login não encontrado!')
            return

        time.sleep(1)
        company = pyautogui.locateOnScreen('company.png', confidence=0.9)
        if company:
            pyautogui.click(company)
            pyautogui.typewrite(usuario.company)
        else:
            print('Campo login não encontrado!')
            return

        pyautogui.alert("Dados inseridos no campos com sucesso!")

    except Exception as error:
        pyautogui.alert(f"Erro ao inserir dados")
        print(error)

if __name__ == "__main__":
    usuario = dados_usuario()
    preencher_formulario(usuario)