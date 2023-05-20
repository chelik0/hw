a = [5, 3, 2, 4]
five = a.count(5)
four = a.count(4)
three = a.count(3)
two = a.count(2)
one = a.count(1)
zero = a.count(0)

print(a)
print(f"""
5: {five}
4: {four}
3: {three}
2: {two}
1: {one}
0: {zero}
""")
print(((five+four+three)/len(a))*100)
