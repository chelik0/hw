"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""

def sell():
    
    if ball <= 49:
        return "Скидка 10%"
    elif ball > 50 and ball < 100:
        return "Скидка 15%"
    else:
        return "Скидка 20%"

ball = int(input("Количество набранных баллов: "))

print("Выша скидка:", sell())
