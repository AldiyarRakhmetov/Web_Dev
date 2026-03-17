a = int(input())
arr = [int(x) for x in input().split(" ")]
flag = True

for i in range(1, a):
    if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0) or (arr[i] == arr[i - 1] == 0):
        print("YES")
        flag = False
        break
if flag:
    print("NO")