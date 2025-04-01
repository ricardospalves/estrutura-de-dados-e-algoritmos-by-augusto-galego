export const containsNearbyDuplicate = (nums: number[], k: number): boolean => {
  const window = new Set();
  let leftPointer = 0;

  for (const index in nums) {
    if (Math.abs(Number(index) - leftPointer) > k) {
      window.delete(nums[leftPointer]);

      leftPointer += 1;
    }

    if (window.has(nums[index])) {
      return true;
    }

    window.add(nums[index]);
  }

  return false;
};

const TEST_CASE = [
  {
    NUMS: [1, 2, 3, 1],
    K: 3,
    EXPECTED_RESULT: true,
  },
  {
    NUMS: [1, 0, 1, 1],
    K: 1,
    EXPECTED_RESULT: true,
  },
  {
    NUMS: [1, 2, 3, 1, 2, 3],
    K: 2,
    EXPECTED_RESULT: false,
  },
];

const CHOSEN = TEST_CASE[0];
const RESULT = containsNearbyDuplicate(CHOSEN.NUMS, CHOSEN.K);

console.log(RESULT);

// if (RESULT) {
//   console.log("✅ Success");
// } else {
//   throw Error(`Expected ${CHOSEN.EXPECTED_RESULT}, but received ${RESULT}`);
// }
