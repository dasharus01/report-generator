from docxtpl import DocxTemplate
# для года
import datetime

def generator(name, group, teacher, rank, degree, position, subject, typework, namework, year, department, founder, uni, type2, point, lecturer,how):
    doc = DocxTemplate("template.docx")
    context = { 'name' : name,
                'group' : group,
                'teacher' : teacher,
                'rank' : rank, 'degree' : degree, 'position' : position,
                'subject' : subject,
                'typework' : typework,
                'namework' : namework, 
                'year' : year,
                'department' : department,
                'founder' : founder,
                'uni' : uni, 
                'type2' : type2, 'point' : point, 'lecturer' : lecturer, 'how' : how}
    doc.render(context)
    doc.save("report.docx")
    
# функция для проверки строки на число
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
# функция на проверку пустоты
def not_empty(str):
        if str == "":
            return False
        else:
            return True
        
# основная программа
# год текущий
now = datetime.datetime.now()
year = now.year 
# ввод данных о студенте
print("Введите фамилию и инициалы студента: ")
name = input()
# проверка на пустоту
while(not_empty(name) != True):
    print("Введите фамилию и инициалы студента. Данное поле не может быть пустым! ")
    name = input()
# фамилия должна быть с большой буквы и инициалы тоже
# так же эта функция оставляет в верхнем регисторе только первые буквы слов
name = name.title()
print("Введите номер группы студента: ")
group = input()
# проверка на пустоту
while(not_empty(group) != True):
    print("Введите номер группы студента. Данное поле не может быть пустым! ")
    group = input()
# ввод данных о преподавателе
print("Введите фамилию и инициалы преподавателя: ")
teacher = input()
# проверка на пустоту
while(not_empty(teacher) != True):
    print("Введите фамилию и инициалы преподавателя. Данное поле не может быть пустым! ")
    teacher = input()
# имя должно быть с большой буквы и инициалы тоже
teacher = teacher.title()
print("Введите звание преподавателя. Если его нет, введите слово нет: ")
rank = input()
rank = rank.lower()
print("Введите уч.степень преподавателя. Если её нет, введите слово нет: ")
degree = input()
degree = degree.lower()
# проверка на наличие нужной должности
# старший преподаватель не может иметь ученую степень
# флаг для выхода из цикла
a = 0;
while a == 0:
    print("Введите должность преподавателя. Если её нет, введите слово нет:")
    position = input()
    position = position.lower()
    if (degree != "нет" or degree == "") and position == "старший преподаватель":
        print("Ошибка! Старший преподаватель не может иметь степень!")
    else:
        a = 1;
# проверка на все регалии. Стирание слов нет
# звание
if rank == "нет":
    rank = ""
else: 
    rank = rank.capitalize()
# степень
if degree == "нет":
    degree = ""
elif degree != "нет" and rank == "": 
    degree =  degree.capitalize()
else: 
    degree = "," + degree
# должность   
if position == "нет":
    position = ""
elif position != "нет" and degree == "": 
    position =  position.capitalize()
else: 
    position = "," + position
# ввод данных о предмете
print("Введите название дисциплины: ")
subject = input()
# проверка на пустоту
while(not_empty(subject) != True):
    print("Введите название дисциплины. Данное поле не может быть пустым! ")
    subject = input()
# перевод всей строки в верхней регистор
subject = subject.upper()

print("Введите тип работы: ")
typework = input()
# проверка на пустоту
while(not_empty(typework) != True):
    print("Введите тип работы. Данное поле не может быть пустым! ")
    typework = input()
# перевод всей строки в верхней регистор
typework = typework.upper()

print("Введите название работы: ")
namework = input()
# проверка на пустоту
while(not_empty(namework) != True):
    print("Введите название работы. Данное поле не может быть пустым! ")
    namework = input()
# перевод всей строки в верхней регистор
namework = namework.upper()

# заполнение заголовка
# ввод кафедры
print("Введите номер или название кафедры: ")
department = input()
# проверка на пустоту
while(not_empty(department) != True):
    print("Введите год выполнения работы. Данное поле не может быть пустым! ")
    department = input()
if is_number(department) == True: 
    department = "№" + department
else:
    department = department.upper()
# заполнение данных о ВУЗе
print("Приналичии введите учередителя ВУЗа. Если такого не имеется, пропустите данное заполнение")
founder = input()
founder = founder.upper()

# заполнение названия ВУЗа
# рассматриваем только ГУАП
if not_empty(founder) == True:
    print("Введите название ВУЗа")
    uni = input()
    # проверка на пустоту
    while(not_empty(uni) != True):
        print("Введите название ВУЗа. Данное поле не может быть пустым! ")
        uni = input()
else:
    uni = "ГУАП"
if typework.find("КОНТРОЛЬНАЯ") != -1:
    type2 = ""
    point = "ОЦЕНКА"
    lecturer = "ПРЕПОДАВАТЕЛЬ"
    how = "по дисциплине"
if typework.find("ПРОЕКТУ") != -1:
    type2 = "КУРСОВОЙ ПРОЕКТ"
    point = "ЗАЩИЩЕН С ОЦЕНКОЙ"
    lecturer = "РУКОВОДИТЕЛЬ"
    how = "по дисциплине"
if typework.find("КУРСОВОЙ РАБОТЕ ") != -1:
    type2 = "КУРСОВОЙ РАБОТА"
    point = "ЗАЩИЩЕНА С ОЦЕНКОЙ"
    lecturer = "РУКОВОДИТЕЛЬ"
    how = "по дисциплине"
   
if typework.find("ЛАБОР") != -1:
    type2 = "ОТЧЕТ"
    point = "ЗАЩИЩЕН С ОЦЕНКОЙ"
    lecturer = "ПРЕПОДАВАТЕЛЬ"
    how = "по курсу"
    
if typework.find("РЕФЕРАТ") != -1:
    type2 = ""
    point = "ОЦЕНКА РЕФЕРАТА"
    lecturer = "РУКОВОДИТЕЛЬ"
    how = "по дисциплине"

#вызов заполнения
generator(name, group, teacher, rank, degree, position, subject, typework, namework, year, department, founder, uni, type2, point, lecturer, how)


























