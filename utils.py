import json 
from PIL import Image, ImageTk

def load_json(src_path):
    with open(src_path, 'r') as f:
        data = json.load(f)
    return data

def save_json(json_dict, dst_path):
    with open(dst_path, 'w') as f:
        json.dump(json_dict, f, indent='\t')

def remove_elem_from_json(json_dict, target_elem):
    target_elem = str(target_elem)
    for k in json_dict:
        for elem in json_dict[k]:
            if k == 'image':
                if elem['name'] == target_elem:
                    json_dict[k].remove(elem)
                    return json_dict
            elif k == 'text':
                if elem['text'] == target_elem:
                    json_dict[k].remove(elem)
                    return json_dict

    raise ValueError('Error occurd in utils.py: remove_elem_from_json')

def inject_text_to_json(json_dict, text, location, font, color):
    if not 'text' in json_dict:
        json_dict['text'] = []

    json_dict['text'].append({
        'text': text,
        'color': list(map(int, color)),
        'font': (font[0], int(font[1])),
        'loc': list(map(int, location)),
    })
    return json_dict     

def inject_image_to_json(json_dict, file_name, location, width, height):
    if not 'image' in json_dict:
        json_dict['image'] = []

    json_dict['image'].append({
        'name': file_name,
        'loc': list(map(int, location)),
        'width': int(width), 
        'height': int(height), 
    })
    return json_dict     

def pillow_to_tk_image(pillow_image):
    imgtk = ImageTk.PhotoImage(image=pillow_image)
    return imgtk

def load_main_image():
    image = Image.open('img/main_image.png')
    return image

if __name__ == '__main__':
    JSON_PATH = 'user_layout.json'
    '''
    data = load_json(JSON_PATH)
    for k1 in data:
        for elem in data[k1]:
            print(elem)
    '''
    data = {
        'image': [
            {
                'name': 'gold.png', 
                'loc': (100,100), # (x,y)
                'width': 100,
                'height': 100
            },
            {
                'name': 'logo.jpg', 
                'loc': (100,500), # (x,y)
                'width': 150,
                'height': 150
            },
        ],
        'text': [
            {
                'text': 'Certificate of Outstanding Achivement',
                'color': (0,0,0),
                'font': ('Helvetica', 15),                
                'loc': (100,50), # (x,y)
            },
            {
                'text': 'The Society for in vitro biology',
                'color': (255,0,0),
                'font': ('Helvetica', 20),
                'loc': (50,400), # (x,y)
            }   
        ]
    }

    save_json(data, JSON_PATH)