while True:
    summ = int(input("summ: "))
    if summ == 0:
        break
    summ = summ - summ/100*20
    print(summ)