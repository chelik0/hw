t_f = False

a = [1,2,3,4,5] # Верно

b = [1,2,4,5] # Верно

c = [1,3,2,4,5] # Верно

d =[1] # Верно

for i in a:
    if len(a) != 1:
        if i == a[i-1]:
            t_f = True
        else:
            t_f = False
            break
    else:
        t_f = False
        break

if t_f:
    print("Да")
else:
    print("Нет")


