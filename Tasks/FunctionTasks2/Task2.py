"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""

def S():
    S = int(input ("Расстояние в км: "))
    
    summ = 4 + (S/1000*140) * 0.25
    print (summ)

print(S())
