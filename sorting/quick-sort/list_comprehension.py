def quicksort_with_list_comprehension(array):
  if len(array) <= 1:
    return array
  else:
    pivot = array[0]
    less_than_pivot = [x for x in array[1:] if x <= pivot]
    greater_than_pivot = [x for x in array[1:] if x > pivot]

    return quicksort_with_list_comprehension(less_than_pivot) + [pivot] + quicksort_with_list_comprehension(greater_than_pivot)

array = [0, 3, 6, 7, 8, 4, 2, 1, 5]

array = quicksort_with_list_comprehension(array, 0, len(array) - 1)

print(array)