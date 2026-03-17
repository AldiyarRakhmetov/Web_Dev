def xor(a: bool, b: bool):
    if (a and not b) or (b and not a):
        return True
    else:
        return False
    
arr = [int(x) for x in input().split(" ")]
print(xor(arr[0], arr[1]))