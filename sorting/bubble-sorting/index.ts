export const bubbleSorting = (list: Array<number>) => {
  const length = list.length;
  const listWithoutLast = list.slice(0, -1);

  for (const _ in list) {
    let isSorted = true;

    console.log(list);

    for (const [index] of listWithoutLast.entries()) {
      if (list[index] > list[Number(index) + 1]) {
        const current = list[index];
        const next = list[index + 1];

        isSorted = false;

        list[index] = next;
        list[index + 1] = current;
      }
    }

    if (isSorted) {
      return;
    }
  }
};

console.log(bubbleSorting([1, 2, 5, 3, 4]));
