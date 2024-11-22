from pynput import mouse  # pip install pynput
import os

def on_click(x, y, button, pressed):
    # Verifica se o botão foi pressionado para registrar as coordenadas
    if not pressed and button == mouse.Button.left:
        print(x, y)
        
        # Cria o arquivo caso ele não exista
        if not os.path.exists("coordenadas.txt"):
            with open("coordenadas.txt", "w"): pass  # Cria o arquivo sem adicionar conteúdo

        # Abre o arquivo e adiciona as coordenadas capturadas
        with open("coordenadas.txt", "a") as file:
            file.write(f"{x}, {y}\n")
    
    # Verifica se o botão direito foi pressionado para parar a execução
    elif not pressed and button == mouse.Button.right:
        print("-" * 20)  # Exibe uma sequência de traços ao finalizar
        return False  # Para o listener e encerra o programa

# Exibe a mensagem inicial
print("Iniciando os cliques...")

# Inicia o listener para capturar cliques do mouse
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
