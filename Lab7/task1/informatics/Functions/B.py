def power(a: float, b: int):
    return a ** b

arr = [int(x) for x in input().split(" ")]
print(power(arr[0], arr[1]))