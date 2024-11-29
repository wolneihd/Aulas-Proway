from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

url_imagem = 'https://cataas.com/cat'
url_nome = 'https://randomuser.me/api/'

data_atual = datetime.now()

# GET
response_imagem = requests.get(url_imagem)
response_nome = requests.get(url_nome)

# Transforma a imagem Rash em variável
imagem = Image.open(BytesIO(response_imagem.content))

data = response_nome.json()
nome = f'{data['results'][0]['name']['first']} - {data_atual}'

# Adicionar texto
draw = ImageDraw.Draw(imagem)
fonte = ImageFont.load_default(50)
draw.text((100, 100), nome, fill="black", font=fonte)

imagem.save('gato.jpg')


