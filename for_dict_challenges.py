from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
dict_name = {}
for i in students:
    name = i['first_name']
    if name in dict_name:
        dict_name[name] += 1
    else:
        dict_name[name] = 1
for name in dict_name:
    print(f'{name}: {dict_name[name]}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
most_common_student = Counter(student['first_name']
        for student in students).most_common(1)
print(f'Самое частое имя среди учеников: {most_common_student[0][0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
names = dict()

for students in school_students:
    for student in students:
        if student['first_name'] not in names.keys():
            names[student['first_name']] = 1
        else:
            names[student['first_name']] += 1
        max_count = max(names.values())
    for name, count in names.items():
        if count == max_count:
            print(f'Само частое имя в классе {school_students.index(students)+1}: {name}')
    names.clear()
print()


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    girls_count = 0
    boys_count = 0
    for students in school_class['students']:
        for name in students.values():
            if is_male[name]:
                boys_count += 1
            else:
                girls_count += 1
    print(f"Класс {school_class['class']}: девочки {girls_count}, мальчики {boys_count}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
girls = 0
boys = 0
class_school = ''
result_boys = {}
result_girls = {}
for i in school:
    for j in i['students']:
        class_school = i['class']
        if j['first_name'] in is_male:
            if is_male[j['first_name']] == True:
                boys += 1
            else:
                girls += 1
    result_boys[class_school]= boys
    result_girls[class_school] = girls
    for q in result_boys:
        pass
    for w in result_girls:
        pass
    if result_girls[w] > result_boys[q]:
        print(f"Больше всего девочек в классе {w}")
    else:
        print(f"Больше всего мальчиков  в классе {q}")
    girls = 0
    boys = 0
    
