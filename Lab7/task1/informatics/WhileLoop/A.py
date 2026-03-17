import math as m

a = int(input())
i = 1

while i <= a:
    if m.isqrt(i)**2 == i:
        print(i)
    i += 1