from typing import List


def missing_number(nums: List[int]) -> int:
  x = 0

  for number in nums:
     x ^= number
  
  for index in range(len(nums) + 1):
     x ^= index

  return x

print(missing_number([3,0,1]))