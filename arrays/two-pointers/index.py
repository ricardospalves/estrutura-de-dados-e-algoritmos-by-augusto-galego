# Função para rever as palavras dentro de uma string.
def reverseWords(value):
  reversedString = ''

  # Ponteiros
  leftPointer = 0
  rightPointer = 0

  # Loop para iterar por cada letra na string.
  while rightPointer < len(value):
    # Verifica se a letra atual é um espaço vazio. Se não for um espaço vazio,
    # significa que o ponteiro ainda não chegou no final da palavra.
    if value[rightPointer] != ' ':
      rightPointer += 1
    
    # Se cair no else, significa que o rightPointer encontrou a palavra,
    # portanto, está pronto para inverter a palavra.
    else:
      # Incrementa na reversedString a palavra encontrada, porem, de trás para
      # frente. 
      reversedString += value[leftPointer:rightPointer + 1][::-1]

      # Move o rightPointer para a próxima palavra.
      rightPointer += 1

      # Move o leftPointer para a mesma posição do rightPointer.
      leftPointer = rightPointer

  reversedString += ' '

  # Concatena a última palavra (invertida), pois o while será interrompido
  # quando o rightPointer estiver na penúltima letra, portando, a última palavra
  # não terá sido concatenada e nem invertida.
  reversedString += value[leftPointer:rightPointer + 2][::-1]

  return reversedString[1:]

# String que será invertida.
VALUE = "Let's take LeetCode contest"

# String invertida para referência.
REVERSED_STRING_REFERENCE = "s'teL ekat edoCteeL tsetnoc"

print(reverseWords(VALUE))
print(reverseWords(VALUE) == REVERSED_STRING_REFERENCE)