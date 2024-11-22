import pyautogui
import webbrowser
import time
import pandas
import json

def contador_tempo(segundos: int):
    for i in range(1, segundos+1):
        time.sleep(1)
        print(f'Tempo de espera: {segundos} | contador: {i}')

# abrindo a página
print('Abrindo página RPA CHALLENGE:')
webbrowser.open('https://rpachallenge.com/')
contador_tempo(8)

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
    lista_usuarios = json.loads(dados_json)
    return lista_usuarios    

def preencher_formulario(usuario: Usuario):  

    confidence = 0.8    
    print(f'Iniciando a preeencher os campos do usuário {usuario.first_name} ... ')

    try:
        time.sleep(1)
        campo_address = pyautogui.locateOnScreen('address.png', confidence=confidence)
        if campo_address:
            pyautogui.click(campo_address)
            pyautogui.typewrite(usuario.address)
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados campo_address - ", error)

    try:
        time.sleep(1)
        email = pyautogui.locateOnScreen('email.png', confidence=confidence)
        if email:
            pyautogui.click(email)
            pyautogui.typewrite(usuario.email)
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados email - ", error)

    try:
        time.sleep(1)
        first_name = pyautogui.locateOnScreen('first_name.png', confidence=confidence)
        if first_name:
            pyautogui.click(first_name)
            pyautogui.typewrite(usuario.first_name)
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados first_name - ", error)

    try:
        time.sleep(1)
        last_name = pyautogui.locateOnScreen('last_name.png', confidence=confidence)
        if last_name:
            pyautogui.click(last_name)
            pyautogui.typewrite(usuario.last_name)
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados last_name - ", error)

    try:
        time.sleep(1)
        role = pyautogui.locateOnScreen('role.png', confidence=confidence)
        if role:
            pyautogui.click(role)
            pyautogui.typewrite(usuario.role)
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados role - ", error)

    try:
        time.sleep(1)
        phone = pyautogui.locateOnScreen('phone.png', confidence=confidence)
        if phone:
            pyautogui.click(phone)
            pyautogui.typewrite(str(usuario.phone))
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados phone - ", error)

    try:
        time.sleep(1)
        company = pyautogui.locateOnScreen('company.png', confidence=confidence)
        if company:
            pyautogui.click(company)
            pyautogui.typewrite(usuario.company)
        else:
            print('Campo login não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao inserir dados company - ", error)

    # envia dados
    try:
        time.sleep(1)
        submit = pyautogui.locateOnScreen('submit.png', confidence=confidence)
        if company:
            pyautogui.click(submit)
        else:
            print('Campo SUBMIT não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao ENVIAR dados", error)

def start_game():
    try:
        start = pyautogui.locateOnScreen('start.png', confidence=0.8)
        if start:
            pyautogui.click(start)
            print('clicado START')
        else:
            print('Campo START não encontrado!')
            return
    except Exception as error:
        print(f"Erro ao START", error)

if __name__ == "__main__":
    # START o jogo
    start_game()

    # iniciar preencher os dados
    lista_usuarios = dados_usuario()
    for usuario in lista_usuarios:
        user = Usuario(usuario['First Name'], usuario['Last Name'], usuario['Address'], usuario['Email'], usuario['Company Name'], usuario['Phone Number'], usuario['Role in Company'])
        preencher_formulario(user)
    