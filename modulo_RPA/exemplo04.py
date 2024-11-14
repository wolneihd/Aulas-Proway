import pyautogui
import os

def criar_arquivo_notepad_e_inserir_texto():
    try:
        os.makedirs("Textos", exist_ok=True)

        # Define o nome do arquivo e o caminho na pasta raiz
        caminho_arquivo = "Textos/notepad_exemplo04.txt"

        # Texto que será inserido no arquivo
        texto = pyautogui.prompt('Digite o que desejar')

        # Usa o open() para criar o arquivo e escrever o texto
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)

        pyautogui.alert(f"Arquivo '{caminho_arquivo}' criado e texto inserido com sucesso!")
    except Exception as e:
        print(e)

# Chama a função para criar o arquivo e inserir o texto
if __name__ == "__main__":
    criar_arquivo_notepad_e_inserir_texto()