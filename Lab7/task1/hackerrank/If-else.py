n = int(input().strip())

if n % 2 == 1:
    print("Weird")
else:
    if n < 6 or n > 20:
        print("Not weird")
    else:
        print("Weird")