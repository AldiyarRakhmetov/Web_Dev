def string_times(str, n):
  return str * n


def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[:3] * n


def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result


def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result


def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count


def array_count9(nums):
  return nums.count(9)


def array_front9(nums):
  for i in range(min(4, len(nums))):
    if nums[i] == 9:
      return True
    
  return False


def array123(nums):
  return 1 in nums and 2 in nums and 3 in nums


def string_match(a, b):
  count = 0
  
  for i in range(min(len(a), len(b)) - 1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
      
  return count