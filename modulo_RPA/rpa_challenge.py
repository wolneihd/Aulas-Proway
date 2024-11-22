import pyautogui
import webbrowser
import time
import pandas
import json

def contador_tempo(segundos: int):
    for i in range(1, segundos+1):
        time.sleep(1)
        print(f'Tempo de espera para abrir e carregar a pagina: {segundos} | contador: {i}')

# abrindo a página
print('Abrindo página RPA CHALLENGE')
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

def buscar_campo(nome_campo:str, informacao_campo:str, just_click:bool):
    try:
        time.sleep(1)
        campo = f'{nome_campo}.png'
        buscar_campo = pyautogui.locateOnScreen(campo, confidence=0.8)

        if buscar_campo and just_click == False:
            pyautogui.click(buscar_campo)
            pyautogui.typewrite(informacao_campo)            
        elif buscar_campo and just_click == True:
            pyautogui.click(buscar_campo)
        else:
            print(f'Campo {nome_campo} não localizado | informação não adicionada: {informacao_campo}')
            return
    except Exception as error:
        print(f"Erro ao inserir dados {nome_campo} | informação não adicionada: {informacao_campo}")
        print('Erro: ', error)

def preencher_formulario(usuario: Usuario):  
 
    print(f'Preenchendo os campos do(a) usuário(a): {usuario.first_name}')

    buscar_campo('address', usuario.address, False)
    buscar_campo('email', usuario.email, False)
    buscar_campo('first_name', usuario.first_name, False)
    buscar_campo('last_name', usuario.last_name, False)
    buscar_campo('role', usuario.role, False)
    buscar_campo('phone', str(usuario.phone), False)
    buscar_campo('company', usuario.company, False)
    buscar_campo('submit', None, True)

if __name__ == "__main__":
    # START o jogo
    buscar_campo('start', None, True)

    # iniciar preencher os dados
    lista_usuarios = dados_usuario()
    for usuario in lista_usuarios:
        user = Usuario(
            usuario['First Name'], 
            usuario['Last Name'], 
            usuario['Address'], 
            usuario['Email'], 
            usuario['Company Name'], 
            usuario['Phone Number'], 
            usuario['Role in Company'])
        preencher_formulario(user)

    print('Preenchimento finalizado!')
    