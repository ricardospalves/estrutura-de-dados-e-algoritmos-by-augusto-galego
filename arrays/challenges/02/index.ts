const twoSum = (nums: number[], target: number): [number, number] => {
  const hashmap: Record<string, number> = {};

  for (const index in nums) {
    if (nums[index] in hashmap) {
      return [hashmap[nums[index]], Number(index)];
    }

    const hashmapKey = `${target - nums[index]}`;
    hashmap[hashmapKey] = Number(index);
  }
};
