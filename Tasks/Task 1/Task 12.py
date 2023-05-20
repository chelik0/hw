s = float(input())
h = float(input())
rashod = int(input())
V = int(input())
zapac = int(input())

ds = round(s*h,2)
kol_lit = (ds/rashod)+(((ds/rashod)/100)*zapac)
bank = int((kol_lit/V)+1)

print(ds,
      round(kol_lit,2),
      bank,
      round((bank*V)-kol_lit, 2)
      )