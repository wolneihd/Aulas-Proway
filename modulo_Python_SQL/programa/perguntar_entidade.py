from entidades import Marca
from marcas import obter_todas_marcas
import questionary

def escolher_marca() -> Marca:
    marcas = obter_todas_marcas()

    if len(marcas) == 0:
        print("Nenhuma marca cadastrada!")
        return

    opcoes_para_escolher = []
    for marca in marcas:
        opcao = questionary.Choice(title=marca.nome, value=marca.id)
        opcoes_para_escolher.append(opcao)
    
    id_marca_escolhida = questionary.select(
        "Escolha a marca que deseja editar",
        choices=opcoes_para_escolher
    ).ask()