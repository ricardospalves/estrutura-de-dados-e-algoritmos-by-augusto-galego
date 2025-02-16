/**
 * Realiza uma busca binária em uma lista ordenada de números.
 *
 * A busca binária é um algoritmo eficiente para encontrar um elemento em uma lista ordenada.
 * Ele divide repetidamente a lista ao meio, comparando o elemento do meio com o alvo.
 * Se o elemento do meio for menor que o alvo, a busca continua na metade superior da lista.
 * Se for maior, a busca continua na metade inferior. O processo se repete até que o alvo
 * seja encontrado ou a lista seja reduzida a zero.
 *
 * @param {number[]} list a lista ordenada de números onde a busca será realizada.
 * @param {number} target o número que está sendo procurado na lista.
 * @returns {number} o índice do elemento encontrado na lista, ou -1 se o elemento não for encontrado.
 */
const binarySearch = (list: number[], target: number) => {
  // Inicializa os ponteiros para o início e o fim da lista
  let lowPointer = 0;
  let highPointer = list.length - 1;

  // Contador de passos para rastrear o número de iterações
  let steps = 0;

  // Enquanto o ponteiro superior for maior ou igual ao ponteiro inferior
  while (highPointer > lowPointer) {
    // Incrementa o contador de passos
    steps += 1;

    // Calcula o índice do meio da lista
    const middlePointer = Math.round((highPointer + lowPointer) / 2);

    // Se o elemento do meio for menor que o alvo, ajusta o ponteiro inferior
    if (list[middlePointer] < target) {
      // Move o ponteiro inferior para a direita
      lowPointer = middlePointer + 1;

      // Continua para a próxima iteração
      continue;
    }

    // Se o elemento do meio for maior que o alvo, ajusta o ponteiro superior
    if (list[middlePointer] > target) {
      // Move o ponteiro superior para a esquerda
      highPointer = middlePointer - 1;

      // Continua para a próxima iteração
      continue;
    }

    // Se o elemento do meio for igual ao alvo, imprime o número de passos e retorna o índice
    console.log("steps:", steps);

    // Retorna o índice do elemento encontrado
    return middlePointer;
  }

  // Se o alvo não for encontrado, imprime uma mensagem e retorna -1
  console.log("target not found");

  // Retorna -1 se o alvo não for encontrado
  return -1;
};

binarySearch(createArrayRange(5), 3);
binarySearch(createArrayRange(10), 3);
binarySearch(createArrayRange(20), 3);

function createArrayRange(n: number): number[] {
  const array = Array(n)
    .fill(0)
    .map((item, index) => index + 1);

  return array;
}
