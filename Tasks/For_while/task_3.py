while True:
    k = str(input())
    for i in range(len(k)):
        if k[i] in ['=','?','*','^','$','№','@','_']:
            print(k[i])