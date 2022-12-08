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
freq_name = {}
for count in students:
    value = count['first_name']
    freq_name[value] = freq_name.get(value, 0) + 1
for key, val in freq_name.items():
    print(f'{key}: {val}')


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
freq_name = {}
for count in students:
    value = count['first_name']
    freq_name[value] = freq_name.get(value, 0) + 1
max_value = max(freq_name.values())
for key in freq_name:
    if freq_name[key] == max_value:
        print(f'Самое частое имя среди учеников: {key}')


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
counter_class = 0
for count_сlasses in school_students:
    freq_name = {}
    for count_name in count_сlasses:
        value = count_name['first_name']
        freq_name[value] = freq_name.get(value, 0) + 1
    max_value = max(freq_name.values())
    counter_class += 1
    for key in freq_name:
        if freq_name[key] == max_value:
            print(f'Самое частое имя в {counter_class} классе: {key}')


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
for count_сlasses in school:#  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]} перебирает строки
    value_names = count_сlasses['students']
    value_class = count_сlasses['class']
    definition_gende = {}
    gende_woman = 0
    gende_man = 0
    for count_names in value_names:#  [{'first_name': 'Маша'}, {'first_name': 'Оля'}]
        names = count_names['first_name']
        if names in is_male:
            gende = is_male[names]
        definition_gende[names] = definition_gende.get(names, gende)
        if gende is False:
            gende_woman += 1
        else:
            gende_man += 1
    print(f'Класс {value_class}: девочки {gende_woman}, мальчики {gende_man}')


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
for count_сlasses in school:
    value_names = count_сlasses['students']
    value_class = count_сlasses['class']
    definition_gende = {}
    gende_woman = 0
    gende_man = 0
    for count_names in value_names:
        names = count_names['first_name']
        if names in is_male:
            gende = is_male[names]
        definition_gende[names] = definition_gende.get(names, gende)
        if gende is False:
            gende_woman += 1
        else:
            gende_man += 1
    if gende_man > gende_woman:
        print(f'Больше всего мальчиков в классе {value_class}')
    else:
        print(f'Больше всего девочек в классе {value_class}')  
