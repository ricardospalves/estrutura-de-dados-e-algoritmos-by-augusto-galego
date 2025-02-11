MAX_CHAR_REPEAT_LIMIT = 2

def maximumLengthSubstring(string: str) -> int:
  lowPointer = 0
  highPointer = 0

  # Tamanho máximo da substring inicializado em 1, pois esse sempre será o valor
  # mínimo retornado, uma vez que sempre haverá pelo menos uma string.
  maximum = 1

  # O counter representa a quantidade de strings que está atualmente dentro da
  # janela (os elementos entre o lowerPointer e o highPointer).
  counter = {}

  # Inicia o contador com o primeiro item da string.
  counter[string[0]] = 1

  while highPointer < (len(string) - 1):
    # Inicia expandido a janela (ao aumentar o ponteiro mais à direita), pois o
    # primeiro item da string já foi adicionado no contador.
    highPointer += 1

    # Verifica se o item atual já está no contador, se estiver, aumenta o seu
    # valor no contador, caso contrário, adiciona o novo item no contador.
    if counter.get(string[highPointer]):
      counter[string[highPointer]] += 1
    else:
      counter[string[highPointer]] = 1
    
    # Loop para contrair a janela caso o número de itens iguais ultrapasse o
    # limite máximo.
    while counter[string[highPointer]] == (MAX_CHAR_REPEAT_LIMIT + 1):
      # Remove o item do contador
      counter[string[lowPointer]] -= 1

      # Contrai a janela
      lowPointer += 1
    
    # Pega a largura da maior substring encontrada
    maximum = max(
      maximum,
      # O "+1" serve para lidar com casos onde, o lowPointer está na posição 0
      # (zero) e o highPointer está na posição 1 (um), por exemplo, portanto,
      # existem 2 itens dentro da janela, porém a subtração de 0 - 1 é 1, e a
      # soma de + 1 resolve o problema. 
      (highPointer - lowPointer + 1)
    )
  
  return maximum

print(maximumLengthSubstring('bcbbbcba'))