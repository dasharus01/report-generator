from docxtpl import DocxTemplate
# для года
import datetime
# для получения данных из консоли
import sys

from docx import Document
from docx.shared import Inches
import argparse
import json
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--org', help="Info about organisation")
parser.add_argument('-s', '--stu', help="Info about student")
parser.add_argument('-r', '--rep' , help = "Info about report")
parser.add_argument('-t', '--tea' , help = "Info about teacher")
#parser.add_argument('--struc' , help = "Info about paragraph")
# год текущий
now = datetime.datetime.now()
year = now.year 
def pr (d):
    doc = DocxTemplate('template.docx')
    #преобразуем имя студента
    if d['student'].get('patronymic', ""):
        names = d['student']['surname'] + " " + d['student']['name'][0] + "." + d['student']['patronymic'][0] + "."
    else:
        names = d['student']['surname'] + " " + d['student']['name'][0] + "."
    if d['teacher']['patronymic'] != "":
        teachern = d['teacher']['surname'] + " " + d['teacher']['name'][0] + "." + d['teacher']['patronymic'][0] + "."
    else:
        teachern = d['teacher']['surname'] + " " + d['teacher']['name'][0] + "."
    studbilet = ""
    if d['student']['identity_card'] != "":
        studbilet = "Студенческий билет №"
    context = {'founder' : d['organisation']['founder'],
               'name' : d['organisation']['name'],
               'faculty' : d['organisation']['faculty'],
               'department' : d['organisation']['department'],
               'namestudent' : names,
               'group' : d['student']['group'],
               'ids' : d['student']['identity_card'],
               'studbilet' : studbilet,
               'typework' : d['report']['task_type'],
               'namework' : d['report']['task_name'],
               'subject' : d['report']['subject_name'],
               'status' : d['teacher']['status'],
               'teachername' : teachern,
               'year' : year
              }
    doc.render(context)
    doc.save('report.docx')

d = {}
args = parser.parse_args()
d["organisation"] = json.loads(args.org)
d["student"] = json.loads(args.stu)
d["report"] = json.loads(args.rep)
d["teacher"] = json.loads(args.tea)
#d["report_structure"] = json.loads(args.struc)

#print(len(d["report_structure"]))
pr(d)