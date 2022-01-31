# import requests
# from bs4 import BeautifulSoup as bs
# import sys

# city = sys.argv[1]


# def get_weather(place):
#     place = place.replace(" ", "-")
#     url = "https://www.weather-forecast.com/locations/" + place + "/forecasts/latest"
#     r = requests.get(url)
#     soup = bs(r.content, "lxml")
#     weather = soup.findAll("span", {"class": "phrase"})[0].text
#     return weather

# print(get_weather(city))
# sys.stdout.flush()


import sys
import PyPDF2, traceback
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import glob
import os
import xlwt
from xlwt import Workbook


sys.stdout.flush()
dir_path = sys.argv[1]
output_dir = f'{dir_path}/graded_sheets'
resource_path = sys.argv[2]
numberfont_path = f'{resource_path}/TrashHand.ttf'
tickfont_path = f'{resource_path}/Dingbats_Normal.ttf'
pdf_files = glob.glob(f'{dir_path}/*.pdf')

wb = Workbook()
marks_sheet = wb.add_sheet('Sheet 1')
start_column = 1
start_row = 4
student_row = start_row
mark_column = start_column


if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for src in pdf_files:
# src = r'./Test.pdf'
    src = src.replace('\\','/')
    print(src)
    input1 = PyPDF2.PdfFileReader(open(src, "rb"))
    
    nPages = input1.getNumPages()

    output_file = PyPDF2.PdfFileWriter()
    
    student_name = src.split('/')[-1]
    student_name = student_name.split('.')[0]
    marks_sheet.write(student_row, 0, student_name)

    mark_column = start_column
    for i in range(nPages) :
        page0 = input1.getPage(i)
        c = canvas.Canvas(f'{resource_path}/marks.pdf')
        for annot in page0['/Annots'] :
            ann = annot.getObject()
            print(ann)
            x = int(ann['/QuadPoints'][2]) 
            y = int((ann['/QuadPoints'][3]+ann['/QuadPoints'][7])/2)
            x_mid = int((ann['/QuadPoints'][2]+ann['/QuadPoints'][0])/2)
            # y_mid = int((ann['/QuadPoints'][1]+ann['/QuadPoints'][7])/2)
            y_mid = int(ann['/QuadPoints'][7])
            # for i in range(0,len(ann['/QuadPoints']),2):
            #     content = f'Coordinate {i}'
            #     x = int(ann['/QuadPoints'][i])
            #     y = int(ann['/QuadPoints'][i+1])
            #     c.drawString(x , y, content)

            content = ann['/Contents']
            # c.drawImage('✓', x_mid, y_mid)
            pdfmetrics.registerFont(TTFont('TrashHand', numberfont_path))
            c.setFont('TrashHand', 80)
            c.setFillColorRGB(255, 0, 0)
            c.drawString(x, y, content)
            pdfmetrics.registerFont(TTFont('Dingbats_Normal', tickfont_path))
            c.setFont('Dingbats_Normal', 150)
            c.setFillColorRGB(255, 0, 0)
            c.drawString(x_mid, y_mid,'w')
            # c.drawImage('tick.png', x_mid, y_mid)

            
            marks_sheet.write(student_row, mark_column, content)
            mark_column+=1

        c.save()
        marks_file = open(f"{resource_path}/marks.pdf", "rb")
        watermark = PyPDF2.PdfFileReader(marks_file)
        page0.mergePage(watermark.getPage(0))
        output_file.addPage(page0)
        output_file.removeLinks()
    
    src_filename = src.split('/')[-1]
    output_filename = f"{output_dir}/{src_filename.split('.')[0]}_graded.pdf"
    
    with open(output_filename, "wb") as outputStream:
        output_file.write(outputStream)

    student_row+=1

wb.save(f'{output_dir}/marks_sheet.xls')
marks_file.close()
# sys.stdout.flush()
# if os.path.exists(f"{resource_path}/marks.pdf"):
#     os.remove(f"{resource_path}/marks.pdf")