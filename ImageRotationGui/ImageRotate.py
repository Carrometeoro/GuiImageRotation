from PIL import Image
from PIL import ImageTk
import os
import  copy

def rotate(im):
    width, height = im.size

    pixels = list(im.getdata())
    longitud =len(pixels)
    pixelrotado = pixels.copy()

    k=0
    for p in range(longitud):
        kp = height*(width-k-1)+(1+height*width)*int(k/width)
        pixelrotado[kp] = pixels[k]
        k = k + 1
    # print(pixelrotado)
    # print(longitud)

    sizer = height, width
    im2 = Image.new(im.mode, sizer)
    im2.putdata(pixelrotado)
    # print(im2.mode)
    return im2


def readImage(path):
    im = Image.open(path)
    im2 = im.resize((300, 300), Image.ANTIALIAS)
    return im2

def imToPhoto(image):
    photo = ImageTk.PhotoImage(image)
    return photo

def rotatehorario(im):
    width, height = im.size

    pixels = list(im.getdata())
    longitud =len(pixels)
    pixelrotado = pixels.copy()

    k=0
    for p in range(longitud):
        kp = height-1-(int(k/width))+height*(k-width*(int(k/width)))
        pixelrotado[kp] = pixels[k]
        k = k + 1
    # print(pixelrotado)
    # print(longitud)

    sizer = height, width
    im2 = Image.new(im.mode, sizer)
    im2.putdata(pixelrotado)
    # print(im2.mode)
    return im2