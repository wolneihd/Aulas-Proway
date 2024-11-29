from PIL import Image, ImageFilter

# carrega imagem
img = Image.open('new_york.jpg')

# imagem redimensionada
img_resized = img.resize((200,200))
img_resized.save('imagem_200x200.jpg')

# borrar fundo
img_blur = img.filter(ImageFilter.BLUR)
img_blur.save('imagem_desfocada.jpg')
img_blur = img_blur.show()

# converter para PNG
img.convert('RGB').save('image_convertida.png','PNG')