import os
import subprocess

# Caminho para o diretório do repositório
caminho_pasta = 'C:/Users/alzir/OneDrive/Área de Trabalho/Super DEV/Aulas-Proway/'

# Caminho para o arquivo de log
caminho_log = 'C:/Users/alzir/OneDrive/Área de Trabalho/Super DEV/log_auto_commit/historico.txt'

# Certifique-se de que o diretório para o log existe
log_dir = os.path.dirname(caminho_log)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Função para executar um comando Git e capturar a saída
def run_git_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar o comando {' '.join(command)}: {e}"

# Mudar para o diretório do repositório
os.chdir(caminho_pasta)

# Capturar o status do repositório
status_output = run_git_command(['git', 'status'])

# Adicionar arquivos ao commit
add_output = run_git_command(['git', 'add', '.'])

# Comitar mudanças com uma mensagem
commit_message = 'Atualização automática de commit'
commit_output = run_git_command(['git', 'commit', '-m', commit_message])

# Fazer push das mudanças para o repositório remoto
push_output = run_git_command(['git', 'push'])

# Atualizar o log com o status, o commit e o push
with open(caminho_log, 'w') as f:
    f.write("Status do Git:\n")
    f.write(status_output + "\n")
    f.write("Adicionado:\n")
    f.write(add_output + "\n")
    f.write("Commit:\n")
    f.write(commit_output + "\n")
    f.write("Push:\n")
    f.write(push_output + "\n")

print("O status do Git, commit e push foram salvos com sucesso em:", caminho_log)
