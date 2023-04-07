import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdf2image import convert_from_bytes, convert_from_path
from PIL import Image

#POPPLER_PATH = 'C:\\Users\\username\\Downloads\\poppler-23.01.0\\Library\\bin'
POPPLER_PATH = None 

class PDFGenerator:
    def __init__(self, json_dict):
        self.json_dict = json_dict

    def __call__(self, pdf_path=None):
        if pdf_path is None:
            pdf_path = 'tmp.pdf'

        pdf = canvas.Canvas(pdf_path, pagesize=A4) 

        # put images
        if 'image' in self.json_dict:
            for elem in self.json_dict['image']:
                # get size
                if 'width' in elem and 'height' in elem:
                    width = elem['width']
                    height = elem['height']
                
                location = elem['loc']
                file_path = os.path.join('resource', elem['name'])
                pdf.drawImage(file_path, *location, width=width, height=height)

        # put texts 
        if 'text' in self.json_dict:
            for elem in self.json_dict['text']:
                if 'color' in elem:
                    color = elem['color']
                else:
                    color = (0,0,0) # black 
                
                if 'font' in elem:
                    font = elem['font']
                
                location = elem['loc']
                text = elem['text']
                
                pdf.setFont(*font)
                pdf.setFillColorRGB(*color)
                pdf.drawString(*location, text)

        pdf.showPage()
        pdf.save()

        pdf_as_image = self.convert_to_image(pdf, POPPLER_PATH)
        return pdf_as_image

    def convert_to_image(self, pdf, poppler_path):
        try:
            if poppler_path is None:
                image = convert_from_bytes(pdf.getpdfdata())[0]
            else:
                image = convert_from_bytes(pdf.getpdfdata(), poppler_path=poppler_path)[0]
        except Exception:
            print('Please install poppler first: conda install -c conda-forge poppler')
            exit()
        return image 

def get_pdf_from_json(json_dict, image_size, dst_path=None):
    pdf = PDFGenerator(json_dict)
    img = pdf(dst_path) # pdf.__call__(dst_path)
        
    img = img.resize(image_size)
    return img  