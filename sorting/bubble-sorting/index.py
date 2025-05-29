def bubble_sorting(list):
  size = len(list)

  for _ in list:
    is_sorted = True

    print(list)

    for i in range(size - 1):
      if list[i] > list[i + 1]:
        is_sorted = False

        list[i + 1], list[i] = list[i], list[i + 1]

    if is_sorted:
      return

bubble_sorting([1, 2, 5, 3, 4])