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
    # поднимаем регистор
    d['organisation']['department'] = d['organisation']['department'].upper()
    d['report']['task_type'] = d['report']['task_type'].upper()
    d['report']['task_name'] = d['report']['task_name'].upper()
    d['report']['subject_name'] = d['report']['subject_name'].upper()
    #преобразуем имя студента
    if d['student'].get('patronymic', ""):
        names = d['student']['surname'] + " " + d['student']['name'][0] + "." + d['student']['patronymic'][0] + "."
    else:
        names = d['student']['surname'] + " " + d['student']['name'][0] + "."
    # преобразуем имя преподавателя
    if d['teacher'].get('patronymic', ""):
        teachern = d['teacher']['surname'] + " " + d['teacher']['name'][0] + "." + d['teacher']['patronymic'][0] + "."
    else:
        teachern = d['teacher']['surname'] + " " + d['teacher']['name'][0] + "."
    # наличие студ.билета
    studbilet = ""
    identity_card = ""
    if d['student'].get('identity_card', ""):
        studbilet = "Студенческий билет №"
        identity_card = d['student']['identity_card']
    # наличие факультета
    faculty = ""
    if d['organisation'].get('faculty', ""):
        faculty = d['organisation']['faculty'].upper()
    # заполнение атоматической части
    if d['report']['task_type'].find("КОНТРОЛЬНАЯ") != -1:
        type2 = ""
        point = "ОЦЕНКА"
        lecturer = "ПРЕПОДАВАТЕЛЬ"
        how = "по дисциплине"
        
    elif d['report']['task_type'].find("ПРОЕКТУ") != -1:
        type2 = "КУРСОВОЙ ПРОЕКТ"
        point = "ЗАЩИЩЕН С ОЦЕНКОЙ"
        lecturer = "РУКОВОДИТЕЛЬ"
        how = "по дисциплине"
       
    elif d['report']['task_type'].find("КУРСОВОЙ РАБОТЕ ") != -1:
        type2 = "КУРСОВОЙ РАБОТА"
        point = "ЗАЩИЩЕНА С ОЦЕНКОЙ"
        lecturer = "РУКОВОДИТЕЛЬ"
        how = "по дисциплине"
        
    elif d['report']['task_type'].find("ЛАБОР") != -1:
        type2 = "ОТЧЕТ"
        point = "ЗАЩИЩЕН С ОЦЕНКОЙ"
        lecturer = "ПРЕПОДАВАТЕЛЬ"
        how = "по курсу"
        
        
    elif d['report']['task_type'].find("РЕФЕРАТ") != -1:
        type2 = ""
        point = "ОЦЕНКА РЕФЕРАТА"
        lecturer = "РУКОВОДИТЕЛЬ"
        how = "по дисциплине"
    #stri = d["report_structure"][0]
    
    
    # заполнение шаблона
    context = {'founder' : d['organisation']['founder'],
               'name' : d['organisation']['name'],
               'faculty' : faculty,
               'department' : d['organisation']['department'],
               'namestudent' : names,
               'group' : d['student']['group'],
               'ids' : identity_card,
               'studbilet' : studbilet,
               'typework' : d['report']['task_type'],
               'namework' : d['report']['task_name'],
               'subject' : d['report']['subject_name'],
               'status' : d['teacher']['status'],
               'teachername' : teachern,
               'year' : year,
               'type2' : type2, 'point' : point, 'lecturer' : lecturer, 'how' : how
              }
    doc.render(context)
    
    doc.save('report.docx')
def main():
    d = {}
    args = parser.parse_args()
    d["organisation"] = json.loads(args.org)
    d["student"] = json.loads(args.stu)
    d["report"] = json.loads(args.rep)
    d["teacher"] = json.loads(args.tea)
    #d["report_structure"] = json.loads(args.struc)

    #print(d["report_structure"][0])
    pr(d)
if __name__ == "__main__":
    main()