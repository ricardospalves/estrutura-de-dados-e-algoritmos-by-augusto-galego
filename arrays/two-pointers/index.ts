const reverseWords = (value: string) => {
  let reversedString = "";
  let lowPointer = 0;
  let hightPointer = 0;

  while (hightPointer < value.length) {
    if (value[hightPointer] !== " ") {
      hightPointer += 1;
    } else {
      reversedString += [...value.slice(lowPointer, hightPointer + 1)]
        .reverse()
        .join("");

      hightPointer += 1;
      lowPointer = hightPointer;
    }
  }

  reversedString += " ";
  reversedString += [...value.slice(lowPointer, hightPointer + 2)]
    .reverse()
    .join("");

  return reversedString.slice(1);
};

const VALUE = `Let's take LeetCode contest`;
const REVERSED_STRING_REFERENCE = `s'teL ekat edoCteeL tsetnoc`;

console.log(reverseWords(VALUE));
console.log(reverseWords(VALUE) === REVERSED_STRING_REFERENCE);
