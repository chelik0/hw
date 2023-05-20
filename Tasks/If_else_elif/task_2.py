time = float(input())
summ = 1000

while True:
    if time >= 10.00 and time <= 12.00:
        print(summ/2)
    elif time >= 20.00 and time < 22.00:
        print(summ/4)
    else:
        print("Скидки в это время нет, приходите в счастливые часы 😉")
    break
