"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
Решить без применения библиотек
"""

def test(word,num,**znach):
    print(word, num, znach)


test("Colors",2,red="#123123",blue = "#123123145")