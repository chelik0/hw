int1 = int(input("1: "))
int2 = int(input("2: "))
int3 = int(input("3: "))
summ = int1 + int2 + int3

if int1 < int2 and int2 < int3:
    print("Акция! ", summ/2)
elif int1 > int2 and int2 > int3:
    print("Акция! ", summ/3)
else:
    print("К оплате:", summ)

