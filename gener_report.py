from docxtpl import DocxTemplate
# для года
import datetime
# для получения данных из консоли
import sys

from docx import Document
from docx.shared import Inches
def generator1(founder, name, faculty, department):
    doc = DocxTemplate("template.docx")
    context = { 'founder' : founder, 
                'name' : name,
                'faculty' : faculty,
                'department' : department}
    doc.render(context)
    doc.save("report.docx")

    
    
# основная программа
# год текущий
now = datetime.datetime.now()
year = now.year 
# заголовок
# founder = sys.argv[1]
# name = sys.argv[2]
i = 2
j = 0
founder = ""
name = ""
faculty = ""
department = ""
k = len (sys.argv)
if sys.argv[1] == "МИНИСТЕРСТВО": 
    founder  = sys.argv[1]
    
    while sys.argv[i]!= ",":
        founder = founder + " " + sys.argv[i]
        i = i + 1
    i = i + 1
    if  i < k:
        if sys.argv[i] == "федеральное" or sys.argv[i] == "ГУАП":
            while sys.argv[i]!= ",":
                name = name + " " + sys.argv[i]
                i = i + 1
            i = i + 1
    if  i < k:
        if sys.argv[i] == "ИНСТИТУТ":
            while sys.argv[i]!= ",":
                faculty = faculty + " " + sys.argv[i]
                i = i + 1
            i = i + 1
    if  i < k:
        if sys.argv[i] == "КАФЕДРА":
            while sys.argv[i]!= ",":
                department = department + " " + sys.argv[i]
                i = i + 1
            i = i + 1

if sys.argv[1] == "федеральное" or sys.argv[1] == "ГУАП":
    name = sys.argv[1]
    while sys.argv[i]!= ",":
        name = name + " " + sys.argv[i]
        i = i + 1
    i = i + 1
    if  i < k:
        if sys.argv[i] == "ИНСТИТУТ":
            while sys.argv[i]!= ",":
                faculty = faculty + " " + sys.argv[i]
                i = i + 1
            i = i + 1
    if  i < k:
        if sys.argv[i] == "КАФЕДРА":
            while sys.argv[i]!= ",":
                department = department + " " + sys.argv[i]
                i = i + 1
            i = i + 1
if sys.argv[1] == "ИНСТИТУТ":
    faculty = sys.argv[1]
    while sys.argv[i]!= ",":
        faculty = faculty + " " + sys.argv[i]
        i = i + 1
    i = i + 1
    if  i < k:
        if sys.argv[i] == "КАФЕДРА":
            while sys.argv[i]!= ",":
                department = department + " " + sys.argv[i]
                i = i + 1
            i = i + 1  
if sys.argv[1] == "КАФЕДРА":
    department = sys.argv[1]
    while sys.argv[i]!= ",":
        department = department + " " + sys.argv[i]
        i = i + 1
    i = i + 1              
if department == "":
    print("Кафедра обязательна!")
    sys.exit()
if founder == "" and name == "":
    founder = "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ"
    name = "федеральное государственное автономное образовательное учреждение высшего образования «САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ АЭРОКОСМИЧЕСКОГО ПРИБОРОСТРОЕНИЯ»"
generator1(founder, name, faculty, department)



























