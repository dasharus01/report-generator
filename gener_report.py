from docxtpl import DocxTemplate
def generator(name, group, teacher, rank, degree, position, subject, typework, namework, year):
    doc = DocxTemplate("template.docx")
    context = { 'name' : name,
                'group' : group,
                'teacher' : teacher,
                'rank' : rank, 'degree' : degree, 'position' : position,
                'subject' : subject,
                'typework' : typework,
                'namework' : namework, 
                'year' : year}
    doc.render(context)
    doc.save("report.docx")

# основная программа
# ввод данных о студенте
print("Введите фамилию и инициалы студента: ")
name = input()
# фамилия должна быть с большой буквы и инициалы тоже
# так же эта функция оставляет в верхнем регисторе только первые буквы слов
name = name.title()
print("Введите номер группы студента: ")
group = input()
# ввод данных о преподавателе
print("Введите фамилию и инициалы преподавателя: ")
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
    if degree != "нет" and position == "старший преподаватель":
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
# перевод всей строки в верхней регистор
subject = subject.upper()
print("Введите тип работы: ")
typework = input()
# перевод всей строки в верхней регистор
typework = typework.upper()
print("Введите название работы: ")
namework = input()
# перевод всей строки в верхней регистор
namework = namework.upper()
print("Введите год выполнения работы: ")
year = input()
#вызов заполнения
generator(name, group, teacher, rank, degree, position, subject, typework, namework, year)


























