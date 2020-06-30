from tkinter import *
from ImageRotationGui import ImageRotate as imr

window = Tk()

window.title("Rotar imagenes")

window.geometry('800x600')

# imagen en PIL
image = imr.readImage("Pruebas.png")


def clicked_izquierdo():
    global image

    imager = imr.rotate(image)

    # image to tk photo
    photo = imr.imToPhoto(imager)
    # create a label
    label = Label(window, image=photo)
    # set the image as img
    label.image = photo
    label.grid(column=394, row=3)

    image = imager


def clicked_derecho():
    global image

    imager = imr.rotatehorario(image)

    # image to tk photo
    photo = imr.imToPhoto(imager)
    # create a label
    label = Label(window, image=photo)
    # set the image as img
    label.image = photo
    label.grid(column=394, row=3)

    image = imager


lbl = Label(window, text="Rotar Imagen", font=("Arial Bold", 20))
lbl.grid(column=394, row=0)

btn = Button(window, text="Rotar imagen derecha", bg="orange", fg="red", command=clicked_derecho)
btn.grid(column=1, row=1)

btn = Button(window, text="Rotar imagen izquierda", bg="orange", fg="red", command=clicked_izquierdo)
btn.grid(column=0, row=1)

# image to tk photo
photo = imr.imToPhoto(image)

label = Label(window, image=photo)
label.grid(column=394, row=3)

window.mainloop()
