def double_char(str):
  out = ""
  for c in str:
    out += c + c
    
  return out


def count_hi(str):
  return str.count("hi")


def cat_dog(str):
  return str.count("dog") == str.count("cat")


def count_code(str_val):
    count = 0
    for i in range(len(str_val) - 3):
        if str_val[i] == 'c' and str_val[i+1] == 'o':
            if str_val[i+3] == 'e':
                  count += 1
    return count


def end_other(a, b):
  return b[-len(a):].lower() == a.lower() or a[-len(b):].lower() == b.lower()


def xyz_there(str):
  return str.count("xyz") > str.count(".xyz")