def count_evens(nums):
  out = 0
  for num in nums:
    if num % 2 == 0:
      out += 1
    
  return out


def big_diff(nums):
  min_val = float("inf")
  max_val = float("-inf")
  
  for num in nums:
    if num > max_val:
      max_val = num
    if num < min_val:
      min_val = num
    
  return abs(max_val - min_val)


def centered_average(nums):
  min_val = float("inf")
  max_val = float("-inf")
  
  for num in nums:
    if num > max_val:
      max_val = num
    if num < min_val:
      min_val = num
    
  nums.remove(max_val)
  nums.remove(min_val)
  return sum(nums) / len(nums)


def sum13(nums):
  sum = 0
  flag = False
  
  for i in range(len(nums)):
    if nums[i] == 13:
      flag = True
    elif flag:
      flag = False
    else:
      sum += nums[i]
  
  return sum


def sum67(nums):
  sum = 0
  flag = False
  
  for num in nums:
    if num == 6:
      flag = True
    if not flag:
      sum += num
    if num == 7:
      flag = False
  
  return sum


def has22(nums):
  flag = False
  for num in nums:
    if flag and num == 2:
      return True
    if num == 2:
      flag = True
    else:
      flag = False
      
  return False