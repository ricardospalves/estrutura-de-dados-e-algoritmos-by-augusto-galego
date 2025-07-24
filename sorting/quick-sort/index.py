def quicksort(array, left, right):
  if left < right:
    print(array[left:right+1])

    pi = partition(array, left, right)

    quicksort(array, left, pi - 1)
    quicksort(array, pi + 1, right)
  
  return array

def partition(array, left, right):
  sub = array[left:right]

  pivot = array[right]

  i = left - 1

  for j in range(left, right):
    if array[j] <= pivot:
      i += 1

      array[i], array[j] = array[j], array[i]

  array[i + 1], array[right] = array[right], array[i + 1]

  return i + 1

array = [0, 3, 6, 7, 8, 4, 2, 1, 5]

print(quicksort(array, 0, len(array) - 1))