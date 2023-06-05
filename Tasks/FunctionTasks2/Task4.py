"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""

def calculate(*args):
    sum = 0
    count = 0
    for num in args:
        sum += num
        count += 1
    a = sum / count
    above = [num for num in args if num > a]
    return (a, above)

result = calculate(1, 2, 3, 4, 5)
print(result)