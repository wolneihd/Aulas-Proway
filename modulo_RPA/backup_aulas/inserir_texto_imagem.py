from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Função para editar a imagem
def editar_imagem(caminho_imagem, texto, novo_tamanho, filtro):
    # Abrir a imagem
    img = Image.open(caminho_imagem)

    # Redimensionar
    img = img.resize(novo_tamanho)

    # Aplicar filtro
    if filtro == "blur":
        img = img.filter(ImageFilter.BLUR)
    elif filtro == "contour":
        img = img.filter(ImageFilter.CONTOUR)
    elif filtro == "sharpen":
        img = img.filter(ImageFilter.SHARPEN)

    # Adicionar texto
    draw = ImageDraw.Draw(img)
    fonte = ImageFont.load_default(50)
    draw.text((100, 100), texto, fill="black", font=fonte)

    # Salvar a imagem
    img.save("imagem_editada.jpg")
    print("Imagem editada salva como 'imagem_editada.jpg'")

# MAIN
# Exemplo de uso
editar_imagem("new_york.jpg", "Ola, Mundo!", (800, 600), "sharpen")