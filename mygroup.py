groupmates = [
    {
        "name": "Диана",
        "surname": "Крюкова",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 2, 2]
    },
    {
        "name": "Мария",
        "surname": "Шубина",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 2, 3]
    },
    {
        "name": "Павел",
        "surname": "Никитин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Ярослав",
        "surname": "Семенов",
        "exams": ["Русский язык", "АиГ", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Василий",
        "surname": "Карзанов",
        "exams": ["Иностранный язык", "ВМ", "КТП"],
        "marks": [4, 5, 4]
    }
]

srball = float(input())
groupmates = filter(lambda x: sum(x["marks"]) / len(x["marks"]) > srball, groupmates)

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(60), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(60), str(student["marks"]).ljust(20))
print_students(groupmates)


