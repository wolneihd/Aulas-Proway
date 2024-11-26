import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import time

class OrganizadorPorDataHandler(FileSystemEventHandler):
    def __init__(self, pasta_monitorada):
        self.pasta_monitorada = pasta_monitorada

    def on_created(self, event):
        if not event.is_directory:
            self.organizar_arquivo(event.src_path)

    # def organizar_arquivo(self, caminho_arquivo):
    #     # Obter o nome do arquivo e sua data de modificação
    #     arquivos = os.listdir(caminho_arquivo)
    #     for arquivo in arquivos:
    #         caminho_arquivo = os.path.join('entrada', arquivo)
    #         data_arquivo = self.obter_data_modificacao(caminho_arquivo)

    #         # Criar a pasta de destino com base na data
    #         pasta_data = os.path.join('entrada', data_arquivo)
    #         os.makedirs(pasta_data, exist_ok=True)
    #         print(f'{arquivo} - {data_arquivo}')
        
    #         # Mover o arquivo para a pasta de destino
    #         dest_path = os.path.join(data_arquivo, arquivo)
    #         source_path = os.path.join('entrada')
    #         shutil.move(source_path, dest_path)

    def organizar_arquivo(self, caminho_arquivo):
        # Obter o nome do arquivo e sua data de modificação
        try:
            data_arquivo = self.obter_data_modificacao(caminho_arquivo)

            # Criar a pasta de destino com base na data
            pasta_data = os.path.join(self.pasta_monitorada, data_arquivo)
            os.makedirs(pasta_data, exist_ok=True)

            # Nome do arquivo
            nome_arquivo = os.path.basename(caminho_arquivo)

            # Caminho de destino
            dest_path = os.path.join(pasta_data, nome_arquivo)

            # Mover o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, dest_path)
            print(f"Arquivo '{nome_arquivo}' movido para a pasta '{pasta_data}'.")
        except Exception as e:
            print(f"Erro ao organizar o arquivo '{caminho_arquivo}': {e}")


    def obter_data_modificacao(self, caminho_arquivo):
        timestamp = os.path.getmtime(caminho_arquivo)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def organizar_arquivos_existentes(pasta):
    print("Organizando arquivos existentes...")
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            try:
                handler = OrganizadorPorDataHandler(pasta)
                handler.organizar_arquivo(caminho_arquivo)
            except Exception as e:
                print(f"Erro ao organizar o arquivo '{arquivo}': {e}")
    print("Organização inicial concluída.")

def monitorar_pasta():
    pasta_monitorada = "entrada"
    os.makedirs(pasta_monitorada, exist_ok=True)
    
    # Organizar arquivos existentes antes de iniciar o monitoramento
    organizar_arquivos_existentes(pasta_monitorada)
    
    # Configurar e iniciar o monitoramento
    handler = OrganizadorPorDataHandler(pasta_monitorada)
    handler.organizar_arquivo(pasta_monitorada)
    observer = Observer()
    observer.schedule(handler, path=pasta_monitorada, recursive=False)
    observer.start()
    
    try:
        print(f"Monitorando a pasta '{pasta_monitorada}'... Pressione Ctrl+C para encerrar.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitoramento encerrado.")
    observer.join()

if __name__ == "__main__":
    monitorar_pasta()