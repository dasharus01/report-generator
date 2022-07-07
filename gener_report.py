from docxtpl import DocxTemplate
def generator(name, group, teacher, rank, degree, position):
    doc = DocxTemplate("template.docx")
    context = { 'name' : name,
                'group' : group,
                'teacher' : teacher,
                'rank' : rank, 'degree' : degree, 'position' : position}
    doc.render(context)
    doc.save("report.docx")

# основная программа
# ввод данных о студенте
print("Введите фамилию и инициалы студента: ")
name = input()
print("Введите номер группы студента: ")
group = input()
# ввод данных о преподавателе
print("Введите фамилию и инициалы преподавателя: ")
teacher = input()
print("Введите звание преподавателя. Если его нет, введите слово нет: ")
rank = input()
print("Введите уч.степень преподавателя. Если её нет, введите слово нет: ")
degree = input()
# проверка на наличие нужной должности
# старший преподаватель не может иметь ученую степень
# флаг для выхода из цикла
a = 0;
while a == 0:
    print("Введите должность преподавателя. Если её нет, введите слово нет:")
    position = input()
    if degree != "нет" and position == "старший преподаватель":
        print("Ошибка! Старший преподаватель не может иметь степень!")
    else:
        a = 1;
# проверка на все регалии. Стирание слов нет
# звание
if rank == "нет":
    rank = ""
# степень
if degree == "нет":
    degree = ""
elif degree != "нет" and rank == "": 
    degree =  degree
else: 
    degree = "," + degree
# должность   
if position == "нет":
    position = ""
elif position != "нет" and degree == "": 
    position =  position
else: 
    position = "," + position
#вызов заполнения
generator(name, group, teacher, rank, degree, position)


