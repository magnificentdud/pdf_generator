import json
from PIL import Image, ImageTk

def load_main_image():
    image = Image.open('img/main_image.jpg')
    return image

def pillow_to_tk_image(pillow_image):
    imgtk = ImageTk.PhotoImage(image=pillow_image)
    return imgtk