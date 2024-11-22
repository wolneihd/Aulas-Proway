def criar_arquivo_notepad_e_inserir_texto():
    # Define o nome do arquivo e o caminho na pasta raiz
    caminho_arquivo = "notepad_teste.txt"
    
    # Texto que será inserido no arquivo
    texto = "Este é um teste de automação com Python - Turma Super DEV - RPA em Python 2024."
    
    # Usa o open() para criar o arquivo e escrever o texto
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    
    print(f"Arquivo '{caminho_arquivo}' criado e texto inserido com sucesso!")

# Chama a função para criar o arquivo e inserir o texto
if __name__ == "__main__":
    criar_arquivo_notepad_e_inserir_texto()