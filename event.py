import tkinter as tk
from tkinter import filedialog
from PIL import Image
from utils import pillow_to_tk_image

def start_event(root,label,json_dict, image_size):
    #TODO: implement

    img = Image.new(mode = 'RGB', size = image_size)
    imgtk = pillow_to_tk_image(img)

    label.config(image=imgtk)
    label.image = imgtk

def load_event(root, label, json_dict, image_size):
    root.file = filedialog.askopenfile(
        initialdir = 'path',
        title = '사용자 정의 json 파일을 선택해라',
        filetypes = (('json files', '*.json'),('all files', '*.*'))
    #TODO :make json files
    )
    json_dict['image'] = True
    print(json_dict)
    print(root.file.name)

def save_event(root, label, json_dict, image_size):
    import json
    with open('test.json','w') as f:
        json.dump(json_dict, f, indent = '\t')
    popup_window = tk.Toplevel()
    popup_window.title('saved')
    popup_window.geometry('200x200')

