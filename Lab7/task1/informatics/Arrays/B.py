a = int(input())
arr = input().split(" ")

for i in range(a):
    if int(arr[i]) % 2 == 0:
        print(arr[i], end=" ")