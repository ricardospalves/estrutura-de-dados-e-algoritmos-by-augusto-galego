/**
 * Constante que define o limite máximo de repetições de caracteres permitidas.
 * Neste caso, um caractere pode aparecer no máximo 2 vezes.
 */
const MAXIMUM_CHARACTER_REPEAT_LIMIT = 2;

/**
 * Função que calcula o comprimento máximo de uma substring que contém
 * caracteres repetidos até um limite definido.
 *
 * @param value - A string de entrada na qual a substring será analisada.
 * @returns O comprimento máximo da substring que atende à condição de repetição.
 *
 * A função utiliza a técnica de "sliding window" (janela deslizante) para
 * percorrer a string. Ela mantém dois ponteiros (`lowPointer` e `highPointer`)
 * que delimitam a janela atual da substring. Um contador é usado para rastrear
 * a frequência de cada caractere na janela.
 *
 * O algoritmo funciona da seguinte forma:
 * 1. Inicializa os ponteiros e um objeto contador para rastrear a frequência
 *    dos caracteres.
 * 2. Expande a janela movendo o `highPointer` para a direita e atualizando
 *    o contador.
 * 3. Se a frequência de um caractere exceder o limite máximo permitido,
 *    move o `lowPointer` para a direita até que a condição seja satisfeita.
 * 4. Atualiza o comprimento máximo da substring sempre que uma nova janela
 *    válida é encontrada.
 * 5. Retorna o comprimento máximo encontrado.
 */
const maximumLengthSubstring = (value: string): number => {
  let lowPointer = 0; // Ponteiro inferior da janela
  let highPointer = 0; // Ponteiro superior da janela
  let maximum = 1; // Comprimento máximo da substring
  const counter = {
    [value[0]]: 1, // Contador inicial para o primeiro caractere
  };

  // Loop enquanto o ponteiro superior não ultrapassar o comprimento da string
  while (highPointer < value.length - 1) {
    highPointer += 1; // Expande a janela

    // Atualiza o contador para o caractere atual
    if (counter[value[highPointer]]) {
      counter[value[highPointer]] += 1;
    } else {
      counter[value[highPointer]] = 1;
    }

    // Ajusta o ponteiro inferior se a condição de repetição for violada
    while (counter[value[highPointer]] === MAXIMUM_CHARACTER_REPEAT_LIMIT + 1) {
      counter[value[lowPointer]] -= 1; // Reduz a contagem do caractere no ponteiro inferior
      lowPointer += 1; // Move o ponteiro inferior para a direita
    }

    // Atualiza o comprimento máximo da substring
    maximum = Math.max(maximum, highPointer - lowPointer + 1);
  }

  return maximum; // Retorna o comprimento máximo encontrado
};

// Exemplo de uso da função
const TEST_CASE = {
  INPUT: "bcbbbcba", // String de entrada para teste
  EXPECTED_LENGTH: 4, // Comprimento máximo esperado
} as const;

// Testes da função
console.log(maximumLengthSubstring(TEST_CASE.INPUT)); // Saída: 4
console.log(
  maximumLengthSubstring(TEST_CASE.INPUT) === TEST_CASE.EXPECTED_LENGTH
); // Saída: true
