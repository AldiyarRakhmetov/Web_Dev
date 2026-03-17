def min(a: int, b: int, c: int, d: int):
    arr = [a, b, c, d]
    min_val = float('inf')

    for i in arr:
        if i < min_val:
            min_val = i

    return min_val

arr = [int(x) for x in input().split(" ")]
print(min(arr[0], arr[1], arr[2], arr[3]))