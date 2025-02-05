# Binary Search

O algoritmo **Binary Search** (busca binária) é um método eficiente para buscar
um elemento em uma lista ordenada. Ele funciona dividindo repetidamente a lista
ao meio e descartando a metade que não contém o elemento procurado e esse
processo é repetido até que o elemento alvo seja encontrado.

## Big O Notation

- **Complexidade temporal**: O(log n);
- **Complexidade espacial**: O(1)

## Passos

1. **Pré-condição**: a lista deve estar ordenada;
1. **Inicalização**: são iniciados 2 ponteiros, um no início e outro no final da lista;
1. **Iteração**:

- 1 ponteiro é adicionado na metade da lista: `ponteiroMeio = ((ponteiroInicio + ponteiroFim) / 2)`;
- o elemento do meio é comparado com o elemento alvo:
  - se o elemento do meio for igual ao elemento alvo, o algoritmo é bem-sucedido é o índice é retornado;
  - se o elemento do meio for menor que o alvo, o `ponteiroInicio` é ajustado para `ponteiroMeio + 1`;
  - se o elemento do meio for maior que o alvo, o `ponteiroFim` é ajustado para `ponteiroMeio - 1`;

1. **Repetição**: o processo continua até que o `ponteiroInicio` ultrapasse o `ponteiroFim`, se isso acontecer e o elementp alvo não for encontrado, significa que ele não está na lista.
