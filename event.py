import copy 
from tkinter import filedialog
import tkinter as tk
from pdf_gen import get_pdf_from_json
from utils import pillow_to_tk_image, load_json, save_json, inject_image_to_json, inject_text_to_json
from utils import remove_elem_from_json

json_dict = {'image': [], 'text': []}

#! update
ret_location = [0, 0]
ret_width    = 0
ret_height   = 0
ret_flag     = False 

ret_color    = [0,0,0]
ret_text     = ''
ret_font     = ['Helvetica', 10]


def generate_event(image_size):
    global json_dict

    dst_path = filedialog.asksaveasfilename(defaultextension=".pdf")
    if dst_path:
        get_pdf_from_json(json_dict, image_size, dst_path=dst_path)
    
    # TODO : use toplevel to inform result 


def load_event(root, label, image_size):
    root.file = filedialog.askopenfile(initialdir='path', title='select file', filetypes=(('json files', '*.json'), ('all files', '*.*')))

    global json_dict
    json_dict = copy.deepcopy(load_json(root.file.name))
    image = get_pdf_from_json(json_dict, image_size)
    imgtk = pillow_to_tk_image(image)

    label.config(image=imgtk)
    label.image = imgtk

def start_event(root, label, image_size):
    global json_dict
    image = get_pdf_from_json(json_dict, image_size)
    imgtk = pillow_to_tk_image(image)
    label.config(image=imgtk)
    label.image = imgtk


def close_event(root):
    root.quit()
    root.destroy()

def apply_image(label, json_dict, image_size, loc, width, height, file_name):
    temp_json_dict = json_dict.copy()    
    temp_json_dict = inject_image_to_json(temp_json_dict, file_name, loc, width, height)
    update_main_lable(label, temp_json_dict, image_size)

def apply_text(label, json_dict, image_size, loc, text, font, color):
    json_dict = inject_text_to_json(json_dict, text, loc, font, color)
    update_main_lable(label, json_dict, image_size)

def reset_global_params():
    global ret_location
    global ret_width
    global ret_height
    global ret_flag
    global ret_color
    global ret_text
    global ret_font

    ret_location = [0, 0]
    ret_width    = 0
    ret_height   = 0
    ret_flag     = False 

    ret_color    = [0,0,0]
    ret_text     = ''
    ret_font     = ['Helvetica', 10]

def adjust_text(root, json_dict, image_size):
    global ret_location
    global ret_flag
    global ret_color
    global ret_text
    global ret_font

    popup_window = tk.Toplevel(root)
    popup_window.title("Adding Text")
    popup_window.geometry("200x440")

    # label(width)
    label_text = tk.Label(popup_window, text='Text({})'.format(ret_text))
    # label(color-red/green/blue)
    label_cr = tk.Label(popup_window, text='Red({})'.format(ret_color[0]))
    label_cg = tk.Label(popup_window, text='Green({})'.format(ret_color[1]))
    label_cb = tk.Label(popup_window, text='Blue({})'.format(ret_color[2]))
    # font(style, size) TODO: replace to menu??
    label_style = tk.Label(popup_window, text='Font-Style({})'.format(ret_font[0]))
    label_size  = tk.Label(popup_window, text='Font-Size({})'.format(ret_font[1]))

    # location (x,y)
    label_x = tk.Label(popup_window, text='Location x({})'.format(ret_location[0]))
    label_y = tk.Label(popup_window, text='Location y({})'.format(ret_location[1]))

    def _popup_entry_event_text(user_input): # text entry
        global ret_text
        label_text.config(text='Text({})'.format(entry_text.get()))
        ret_text = entry_text.get()
                
    def _popup_entry_event_cr(user_input): # entry red
        global ret_color
        label_cr.config(text='Red({})'.format(entry_cr.get()))
        ret_color[0] = entry_cr.get()

    def _popup_entry_event_cg(user_input): # entry green
        global ret_color
        label_cg.config(text='Green({})'.format(entry_cg.get()))
        ret_color[1] = entry_cg.get()

    def _popup_entry_event_cb(user_input): # entry blue
        global ret_color
        label_cb.config(text='Blue({})'.format(entry_cb.get()))
        ret_color[2] = entry_cb.get()
        
    def _popup_entry_event_style(user_input): # entry font style
        global ret_font
        label_style.config(text='Font-Style({})'.format(entry_style.get()))
        ret_font[0] = entry_style.get()

    def _popup_entry_event_size(user_input): # entry font size
        global ret_font
        label_size.config(text='Font-Size({})'.format(entry_size.get()))
        ret_font[1] = entry_size.get()

    def _popup_entry_event_y(user_input): # entry event 
        global ret_location
        label_y.config(text='Location y({})'.format(entry_y.get()))
        ret_location[1] = entry_y.get()
    def _popup_entry_event_x(user_input): # entry event 
        global ret_location
        label_x.config(text='Location x({})'.format(entry_x.get()))
        ret_location[1] = entry_x.get()
        

    def _popup_button_event_apply(): # button event 
        global ret_flag
        popup_window.quit()
        popup_window.destroy()
        ret_flag = False 

    def _popup_button_event_finish(): # button event 
        global ret_flag
        popup_window.quit()
        popup_window.destroy()
        ret_flag = True

    entry_text = tk.Entry(popup_window) # entry (width)
    entry_cr = tk.Entry(popup_window) # entry (height)
    entry_cg = tk.Entry(popup_window) # entry (height)
    entry_cb = tk.Entry(popup_window) # entry (height)
    entry_x = tk.Entry(popup_window) # entry (x)
    entry_y = tk.Entry(popup_window) # entry (y)
    entry_style = tk.Entry(popup_window) # 
    entry_size = tk.Entry(popup_window) # 

    entry_text.bind('<Return>', _popup_entry_event_text)
    entry_cr.bind('<Return>', _popup_entry_event_cr)
    entry_cg.bind('<Return>', _popup_entry_event_cg)
    entry_cb.bind('<Return>', _popup_entry_event_cb)

    entry_x.bind('<Return>', _popup_entry_event_x)
    entry_y.bind('<Return>', _popup_entry_event_y)

    entry_style.bind('<Return>', _popup_entry_event_style)
    entry_size.bind('<Return>', _popup_entry_event_size)

    # button 
    button_apply  = tk.Button(popup_window, text='Apply', command=_popup_button_event_apply)
    button_finish = tk.Button(popup_window, text='Finish', command=_popup_button_event_finish)

    label_text.pack(); entry_text.pack()
    label_cr.pack(); entry_cr.pack()
    label_cg.pack(); entry_cg.pack()
    label_cb.pack(); entry_cb.pack()

    label_x.pack(); entry_x.pack()
    label_y.pack(); entry_y.pack()

    label_style.pack(); entry_style.pack()
    label_size.pack(); entry_size.pack()

    button_apply.pack(side='left', expand=True, fill='both') 
    button_finish.pack(side='left', expand=True, fill='both') 
    
    popup_window.mainloop()
    return ret_location, ret_text, ret_font, ret_color, ret_flag


def adjust_image(root, label, json_dict, image_size, file_name):
    global ret_location
    global ret_width
    global ret_height

    popup_window = tk.Toplevel(root)
    popup_window.title("Adding Image")
    popup_window.geometry("200x240")

    # label(width)
    label_w = tk.Label(popup_window, text='Width({})'.format(ret_width))
    # label(height)
    label_h = tk.Label(popup_window, text='Height({})'.format(ret_height))
    # location (x,y)
    label_x = tk.Label(popup_window, text='Location x({})'.format(ret_location[0]))
    label_y = tk.Label(popup_window, text='Location y({})'.format(ret_location[1]))

    def _popup_entry_event_w(user_input): # entry event 
        global ret_location
        global ret_width
        global ret_height
        label_w.config(text='Width({})'.format(entry_w.get()))
        ret_width = entry_w.get()
        #apply_image(label, json_dict, image_size, ret_location, ret_width, ret_height, file_name)
        
    def _popup_entry_event_h(user_input): # entry event 
        global ret_location, ret_width, ret_height
        label_h.config(text='Height({})'.format(entry_h.get()))
        ret_height = entry_w.get()
        #apply_image(label, json_dict, image_size, ret_location, ret_width, ret_height, file_name)

    def _popup_entry_event_x(user_input): # entry event 
        global ret_location, ret_width, ret_height
        label_x.config(text='Location x({})'.format(entry_x.get()))
        ret_location[0] = entry_x.get()
        #apply_image(label, json_dict, image_size, ret_location, ret_width, ret_height, file_name)

    def _popup_entry_event_y(user_input): # entry event 
        global ret_location, ret_width, ret_height
        label_y.config(text='Location y({})'.format(entry_y.get()))
        ret_location[1] = entry_y.get()
        #apply_image(label, json_dict, image_size, ret_location, ret_width, ret_height, file_name)

    def _popup_button_event_apply(): # button event 
        global ret_location, ret_width, ret_height, ret_flag
        popup_window.quit()
        popup_window.destroy()
        ret_flag = False 

    def _popup_button_event_finish(): # button event 
        global ret_location, ret_width, ret_height, ret_flag
        popup_window.quit()
        popup_window.destroy()
        ret_flag = True
        
    entry_w = tk.Entry(popup_window) # entry (width)
    entry_h = tk.Entry(popup_window) # entry (height)
    entry_x = tk.Entry(popup_window) # entry (x)
    entry_y = tk.Entry(popup_window) # entry (y)
    entry_w.bind('<Return>', _popup_entry_event_w)
    entry_h.bind('<Return>', _popup_entry_event_h)
    entry_x.bind('<Return>', _popup_entry_event_x)
    entry_y.bind('<Return>', _popup_entry_event_y)
    # button 
    button_apply  = tk.Button(popup_window, text='Apply', command=_popup_button_event_apply)
    button_finish = tk.Button(popup_window, text='Finish', command=_popup_button_event_finish)

    label_w.pack(); entry_w.pack()
    label_h.pack(); entry_h.pack()
    label_x.pack(); entry_x.pack()
    label_y.pack(); entry_y.pack()
    button_apply.pack(side='left', expand=True, fill='both') 
    button_finish.pack(side='left', expand=True, fill='both') 
    
    popup_window.mainloop()
    
    return ret_location, ret_width, ret_height, ret_flag

def update_main_lable(label, json_dict, image_size):
    image = get_pdf_from_json(json_dict, image_size)
    imgtk = pillow_to_tk_image(image)
    label.config(image=imgtk)
    label.image = imgtk

def remove_handler(root):
    popup_window = tk.Toplevel(root)
    popup_window.title("Removing elem.")
    popup_window.geometry("200x200")

    listbox = tk.Listbox(popup_window, selectmode='extended')
    listbox.pack()

    num_image_elems = 0
    num_text_elems = 0
    if 'image' in json_dict:
        num_image_elems += len(json_dict['image'])
        for i, elem in enumerate(json_dict['image']):
            listbox.insert(i, elem['name'])

    if 'text' in json_dict:
        for i, elem in enumerate(json_dict['text']):
            listbox.insert(i + num_image_elems, elem['text'])

    def delete():
        global json_dict
        json_dict = remove_elem_from_json(json_dict, listbox.get(tk.ACTIVE))
        listbox.delete(tk.ACTIVE)

    def _popup_button_event_finish(): # button event 
        global ret_flag
        popup_window.quit()
        popup_window.destroy()
        ret_flag = True
    
    
    button_delete  = tk.Button(popup_window, text='Delete', command=delete)
    button_finish = tk.Button(popup_window, text='Finish', command=_popup_button_event_finish)
    button_delete.pack(side='left', expand=True, fill='both') 
    button_finish.pack(side='left', expand=True, fill='both') 

    popup_window.mainloop()
    global ret_flag
    return ret_flag

def remove_event(root, label, image_size):
    global json_dict
    global ret_flag 

    while True:
        exit_flag = remove_handler(root)
        update_main_lable(label, json_dict, image_size)

        if exit_flag:
            reset_global_params() # reset global params 
            break 

def add_text_event(root, label, image_size):
    global json_dict

    while True:
        location, text, font, color, exit_flag = adjust_text(root, json_dict, image_size)
        if not exit_flag: 
            tmp_json_dict = copy.deepcopy(json_dict)
            tmp_json_dict = inject_text_to_json(tmp_json_dict, text, location, font, color)
            apply_text(label, tmp_json_dict, image_size, location, text, font, color)
        else:
            json_dict = inject_text_to_json(json_dict, text, location, font, color)
            update_main_lable(label, json_dict, image_size)
            reset_global_params() # reset global params 
            break


def add_image_event(root, label, image_size):
    global json_dict
    
    root.file = filedialog.askopenfile(
        initialdir='path', title='select file', 
        filetypes=(('image files', '*.jpg'), ('image files', '*.png'), ('all files', '*.*')))

    file_name = root.file.name.split('/')[-1]
    
    if file_name is None:
        return 

    while True:
        location, width, height, exit_flag = adjust_image(root, label, json_dict, image_size, file_name)
        
        if not exit_flag: 
            tmp_json_dict = copy.deepcopy(json_dict)
            tmp_json_dict = inject_image_to_json(tmp_json_dict, file_name, location, width, height)
            
            apply_image(label, tmp_json_dict, image_size, location, width, height, file_name)
        else:
            json_dict = inject_image_to_json(json_dict, file_name, location, width, height)
            update_main_lable(label, json_dict, image_size) 
            reset_global_params() # reset global params 
            break


def save_event(root):
    global json_dict
    dst_path = filedialog.asksaveasfilename(defaultextension=".json")
    
    if dst_path:
        save_json(json_dict, dst_path)
    