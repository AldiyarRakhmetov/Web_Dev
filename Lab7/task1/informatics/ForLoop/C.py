import math as m

a = int(input())
b = int(input())

for i in range(a, b):
    if m.isqrt(i)**2 == i:
        print(i)