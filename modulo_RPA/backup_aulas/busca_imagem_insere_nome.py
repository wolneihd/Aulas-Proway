import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def baixar_imagem(url_api):
    """
    Faz uma requisição à API e retorna a imagem baixada.
    """
    try:
        response = requests.get(url_api)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return Image.open(BytesIO(response.content))
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

def adicionar_texto_centralizado(imagem, texto, tamanho_fonte=50):
    """
    Adiciona texto centralizado em uma imagem com bordas para legibilidade.
    """
    draw = ImageDraw.Draw(imagem)
    
    try:
        # Definir a fonte
        fonte = ImageFont.truetype("arial.ttf", tamanho_fonte)
    except IOError:
        print("Fonte Arial não encontrada. Usando fonte padrão.")
        fonte = ImageFont.load_default()

    # Medir o tamanho do texto
    bbox = draw.textbbox((0, 0), texto, font=fonte)  # Obtém as bordas do texto
    largura_texto = bbox[2] - bbox[0]  # largura = x2 - x0
    altura_texto = bbox[3] - bbox[1]  # altura = y2 - y0

    # Tamanho da imagem
    largura_imagem, altura_imagem = imagem.size

    # Calcular a posição central
    x_central = (largura_imagem - largura_texto) / 2
    y_central = (altura_imagem - altura_texto) / 2

    # Adicionar borda ao texto para maior contraste
    for deslocamento in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
        draw.text((x_central + deslocamento[0], y_central + deslocamento[1]), texto, font=fonte, fill="black")

    # Adicionar texto principal (branco)
    draw.text((x_central, y_central), texto, font=fonte, fill="white")

    return imagem

def salvar_imagem(imagem, caminho_saida):
    """
    Salva a imagem editada em um arquivo.
    """
    try:
        imagem.save(caminho_saida)
        print(f"Imagem salva como {caminho_saida}")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")

def busca_nome_aleatorio():
    data = requests.get("https://randomuser.me/api/")
    data = data.json()
    nome = data['results'][0]['name']['first']
    return nome

def main():
    """
    Fluxo principal do programa: baixa a imagem, edita e salva.
    """
    # Configurações
    url_api = "https://cataas.com/cat"  # URL da API
    texto_para_adicionar = busca_nome_aleatorio()
    nome_arquivo_saida = "imagem_com_texto_centralizado.jpg"

    # Baixar a imagem
    imagem = baixar_imagem(url_api)
    if imagem is None:
        return

    # Adicionar texto centralizado
    imagem_editada = adicionar_texto_centralizado(imagem, texto_para_adicionar, tamanho_fonte=30)

    # Salvar a imagem editada
    salvar_imagem(imagem_editada, nome_arquivo_saida)
    Image.open(nome_arquivo_saida).show()
    

# Executar o programa
if __name__ == "__main__":
    main()
    