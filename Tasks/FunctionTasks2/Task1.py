"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""

def main(num1=None, num2=None, num3=None):
    if num1 is not None:
        print(num1)
    if num2 is not None:
        print(num2)
    if num3 is not None:
        print(num3)


par1 = input("Параметр 1: ")
par2 = input("Параметр 2: ")
par3 = input("Параметр 3: ")

main(num1=par1, num2=par2, num3=par3)
