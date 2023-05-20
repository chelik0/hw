"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def imt():
    if index < 18.5:
        return "Недостаточный вес"
    elif index >= 18.5 and index < 25:
        return "Вес в норме"
    elif index >= 25:
        return "Избыточный вес"
    else:
        return "Ошибочная команда"


while True:
    height = int(input("Введите ваш рост: "))
    weight = int(input("Введите ваш вес: "))
    index = weight / (height ** 2)

    print(imt())
