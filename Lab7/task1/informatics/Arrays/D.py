a = int(input())
arr = [int(x) for x in input().split(" ")]
sum = 0

for i in range(1, a):
    if arr[i] > arr[i - 1]:
        sum += 1

print(sum)