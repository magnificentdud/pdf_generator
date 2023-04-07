import tkinter as tk
from PIL import Image 

from event import *
from utils import *

def main():
    window = tk.Tk() 
    monitor_width  = window.winfo_screenwidth()
    monitor_height = window.winfo_screenheight()
        
    # window size 
    window_height = monitor_height-100
    window_width  = int(window_height*0.7) 
    # image(logo) size 
    image_height = window_height - 100
    image_width  = window_width
    image_size   = (image_width, image_height) 

    # geometry 
    window.geometry('{}x{}+0+0'.format(window_width, window_height))
    # title
    window.title('PDF Gen.') 
    window.resizable(True, True)

    # main image load 
    main_image = load_main_image()
    main_image = main_image.resize(image_size)
    main_tk_image = pillow_to_tk_image(main_image) # convert 

    # label 
    label = tk.Label(window, image=main_tk_image)
    label.pack() 
    
    # button frame 
    button_frame = tk.Frame(window)
    button_frame.pack(side='bottom', fill='both', expand=True)
    
    # 1. Start button 
    start_button = tk.Button(
        button_frame, text='Start', overrelief='solid',
        width=3, command= lambda: start_event(window, label, image_size)
    )
    start_button.pack(side='left', expand=True, fill='x')

    
    # 2. Load button
    load_button = tk.Button(
        button_frame, text='Load Json', overrelief='solid',
        width=3, command= lambda: load_event(window, label, image_size)
    )
    load_button.pack(side='left', expand=True, fill='x')
    
    # 3. Save button
    save_button = tk.Button(
        button_frame, text='Save Json', overrelief='solid',
        width=3, command= lambda: save_event(window)
    )
    save_button.pack(side='left', expand=True, fill='x')

    # 4. Add Image button 
    add_image_button = tk.Button(
        button_frame, text='Add Image', overrelief='solid',
        width=3, command= lambda: add_image_event(window, label, image_size)
    )
    add_image_button.pack(side='left', expand=True, fill='x')

    # 5. Add Text button 
    add_text_button = tk.Button(
        button_frame, text='Add Text', overrelief='solid',
        width=3, command= lambda: add_text_event(window, label, image_size)
    )
    add_text_button.pack(side='left', expand=True, fill='x')

    # 6. Remove button 
    remove_button = tk.Button(
        button_frame, text='Remove Item', overrelief='solid',
        width=3, command= lambda: remove_event(window, label, image_size)
    )
    remove_button.pack(side='left', expand=True, fill='x')

    # 7. PDF Generation button 
    pdf_gen_button = tk.Button(
        button_frame, text='PDF Gen.', overrelief='solid',
        width=3, command= lambda: generate_event(image_size)
    )
    pdf_gen_button.pack(side='left', expand=True, fill='x')

    # 8. Exit button 
    exit_button = tk.Button(
        button_frame, text='Finish', overrelief='solid',
        width=3, command= lambda: close_event(window)
    )
    exit_button.pack(side='left', expand=True, fill='x')
    

    window.mainloop()


if __name__ == '__main__':
    main() 