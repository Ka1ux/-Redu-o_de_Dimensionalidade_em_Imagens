from PIL import Image

def img_to_gray(path_img):
    imagem = Image.open(path_img)
    imagem_cinza = imagem.convert("L")  # Converter para escala de cinza
    imagem_cinza.save("imagem_cinza.jpg")
    return imagem_cinza

def img_to_dark(path_img_gray):
    imagem = Image.open(path_img_gray)
    limiar = 128  # Ajuste o valor conforme necessário
    imagem_escura = imagem.point(lambda x: 255 if x > limiar else 0, '1')
    imagem_escura.save("imagem_escura.jpg")
    return imagem_escura

# Colocar caminho da imagem original
imagem_cinza = img_to_gray("imagem.png")

# Colocar o caminho da imagem cinza criada no passo anterior
imagem_escura = img_to_dark("imagem_cinza.jpg")
