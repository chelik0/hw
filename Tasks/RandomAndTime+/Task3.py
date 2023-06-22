"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""

from random import randint

first = 0
second = 0

while True:
    if input("Введите имя участника (или off): ") == "off":
        break
    else:
        if randint(1,2) == 1:
            print("Ваш номер: 1")
            first += 1
        else:
            print("Выш номер: 2")
            second += 1
print(f"Участников в первом забеге: {first}, «Участников во втором забеге: {second}")