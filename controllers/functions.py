from PIL import Image, ImageDraw, ImageTk
from base64 import b64encode, b64decode


def adicionarBordaCircular(imgb64):

    imag = Image.open(ImageTk.BytesIO(b64decode(imgb64)))
    img = imag.resize((300,300))
    mask = Image.new('L', (300,300), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0,0),(300,300)], 150, fill=255)
    img.putalpha(mask)
    return img


def converterImagemParaB64(path_image):
    with open(path_image, 'rb') as image_file:
        return b64encode(image_file.read())