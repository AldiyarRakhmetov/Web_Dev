def swap_case(s):
    out = ''
    for c in s:
        if c.islower():
            out += c.upper()
        if c.isupper():
            out += c.lower()
    return out

print(swap_case(input()))