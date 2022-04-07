from pdf2image import convert_from_path
from fpdf import FPDF
import shutil
import cv2
import os

def cam_scanner_filter(filer_location):
    image1 = cv2.imread(filer_location)
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 10)
    cv2.imwrite(filer_location, thresh1)
    # thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 15)
    # cv2.imwrite(filer_location, thresh2)


def pdf_to_img(input_pdf):
    dir="Images"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    if input_pdf.split(".")[1] == 'pdf':
        print("start")
        pages = convert_from_path(input_pdf,poppler_path='C:\\poppler-0.68.0_x86\\poppler-0.68.0\\bin',fmt='jpeg') #Replace poppler-bin Location 
        count = 0
        for page in pages:
            count +=1
            page.save(f'{dir}\\file-{count}.jpg', 'JPEG')
            cam_scanner_filter(f'{dir}\\file-{count}.jpg')

def img_to_pdf():
    dir="Output"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    pdf = FPDF()
    imagelist=os.listdir('Images')
    for image in imagelist:
        pdf.add_page()
        pdf.image(f'Images//{image}',0,0,210)
    pdf.output("Output//Output.pdf", "F")


input_pdf = input("INPUT PDF: ")
pdf_to_img(input_pdf)
img_to_pdf()