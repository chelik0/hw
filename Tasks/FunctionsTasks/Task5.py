"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""

def prise():
    if summ > 80:
        return "Наградить дипломом"
    elif summ < 50:
        return "Выдать грамоту об участии"
    else:
        return "Наградить дипломом"


name_student = input("При желдании остановить работу программы введите 'стоп'")

while name_student == "стоп":
    name_student = input("Введите ваше имя: ")
    print("Далее введите число выших баллов по предметам:")

    ball1 = int
    