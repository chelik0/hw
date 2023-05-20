a = []
while True:
    game = str(input())
    if game == '0':
        break
    else:
        if game not in a:
            a.append(game)
        else:
            print("Игра повторяется")

a.sort()
print(a)