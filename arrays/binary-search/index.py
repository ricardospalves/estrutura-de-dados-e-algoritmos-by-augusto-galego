def binarySearch(list, target):
  """
  Implementação do algoritmo Binary Search.

  Args:
    list (List[int]): lista ordenada que será usado na busca.
    target (int): número que deve ser encontrado no array.

  Returns:
    int: número ncontrado.
  """

  # Ponteiro que, inicialmente, fica no começo da lista.
  lowPointer = 0

  # Ponteiro que, inicialmente, fica no fim da lista.
  highPointer = len(list)

  # Número de passos que o algoritmo levou para encontrar o resultado.
  steps = 0

  # Loop para iterar sobre a lista através dos ponteiros. Enquanto o highPointer
  # for maior que o lowPointer, significa que o resultado ainda não foi
  # encontrado. Se o ponteiro highPointer for igual ou menor que o lowerPointer,
  # então o loop é interrompido.
  while highPointer > lowPointer:
    steps += 1

    # Ponteiro que sempre inicia na metade da lista.
    middle = int((highPointer + lowPointer) / 2)

    # Se o elemento da metade da lista for menor que o número a ser encontrado,
    # então o lowerPointer é movido para depois da metade da lista.
    if list[middle] < target:
      lowPointer = middle + 1
      continue

    # Se o elemento da metade da lista for maior que o número a ser encontrado,
    # então o highPointer é movido a metade da lista.
    if list[middle] > target:
      highPointer = middle
      continue

    print("steps", steps)

    # Retorna o resultado encontrado.
    return list[middle]
  
  # Se retornar -1, significa que o target não foi encontrado.
  return -1

binarySearch([1, 2, 3, 4, 5], 3)
binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 3)