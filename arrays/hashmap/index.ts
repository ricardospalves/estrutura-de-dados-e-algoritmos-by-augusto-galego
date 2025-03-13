/**
 * Encontra o índice do primeiro caractere único em uma string.
 *
 * Um caractere é considerado único se ele aparece apenas uma vez na string.
 * Se não houver caracteres únicos, a função retorna -1.
 *
 * @param input - A string de entrada na qual o primeiro caractere único será buscado.
 * @returns O índice do primeiro caractere único ou -1 se não houver caracteres únicos.
 */
export const firstUniqueChar = (input: string): number => {
  // Converte a string de entrada em um array de caracteres
  const inputAsArray = [...input];

  // Objeto para armazenar a contagem de caracteres e seus índices
  const charCount: Record<
    string,
    {
      count: number;
      index: number;
    }
  > = {};

  // Itera sobre o array de caracteres para contar as ocorrências
  for (const index in inputAsArray) {
    const currentChar = inputAsArray[index];

    // Se o caractere ainda não foi encontrado, inicializa sua contagem
    if (!(currentChar in charCount)) {
      charCount[currentChar] = {
        count: 1,
        index: Number(index),
      };
      continue;
    }

    // Incrementa a contagem do caractere
    charCount[currentChar].count += 1;
  }

  // Converte o objeto de contagem em uma lista de entradas
  const charCountAsEntries = Object.entries(charCount);

  // Procura o primeiro caractere único
  for (const [char, value] of charCountAsEntries) {
    if (value.count === 1) {
      return value.index; // Retorna o índice do primeiro caractere único
    }
  }

  // Retorna -1 se não houver caracteres únicos
  return -1;
};

// Exemplo de uso da função
const TEST_CASE = {
  INPUT: "leetcode", // String de entrada para teste
  EXPECTED_VALUE: 0, // Comprimento máximo esperado
} as const;

console.log(firstUniqueChar(TEST_CASE.INPUT));
console.log(firstUniqueChar(TEST_CASE.INPUT) === TEST_CASE.EXPECTED_VALUE);
