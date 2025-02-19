from typing import List

def binary_search(list: List[int], target: int, low_pointer: int, high_pointer: int) -> int:
  while high_pointer > low_pointer:
    middle_pointer = int((high_pointer + low_pointer) / 2)

    if list[middle_pointer] < target:
      low_pointer = middle_pointer + 1
      continue

    if list[middle_pointer] > target:
      high_pointer = middle_pointer
      continue

    return middle_pointer

  return -1

def exponential_search(list: List[int], target: int) -> int:
  if(list[0] == target):
    return target
  
  list_length = len(list)
  right_pointer = 1

  while (right_pointer < list_length) and (list[right_pointer] < target):
    right_pointer *= 2

    if list[right_pointer] == target:
      return right_pointer
  
  return binary_search(list=list, target=target, low_pointer=(right_pointer // 2), high_pointer=min(right_pointer, list_length - 1))

LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
TARGET = 32

print(f"Element found at index {exponential_search(LIST, TARGET)}")