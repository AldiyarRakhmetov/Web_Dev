def sleep_in(weekday, vacation):
  return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile


def sum_double(a, b):
  if a == b:
    return 4 * a
  else:
    return a + b
  

def diff21(n):
  n -= 21
  if n < 0:
    return abs(n)
  else:
    return n*2


def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False
  

def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False


def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  else:
    return False


def pos_neg(a, b, negative):
  if not negative:
    return a * b < 0
  else:
    return a < 0 and b < 0


def not_string(str):
  if str[0:3] == "not":
    return str
  return "not " + str


def missing_char(str, n):
  return str[0:n] + str[n+1:]


def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1] + str[1:-1] + str[0]


def front3(str):
  if len(str) < 3:
    return str * 3
  return str[0:3] * 3