def firstUniqueChar(s: str) -> int:
  char_counter = {}

  for index, char in enumerate(s):
    if not char_counter.get(char):
      char_counter[char] = [index, 1]
      continue

    char_counter[char][1] += 1
  
  for char, value in char_counter.items():
    if value[1] == 1:
      return value[0]
  
  return -1

TEST_CASE = {
  'INPUT': 'leetcode',
  'EXPECTED_VALUE': 0,
}

print(firstUniqueChar(TEST_CASE.get('INPUT')))
print(firstUniqueChar(TEST_CASE.get('INPUT')) == TEST_CASE.get('EXPECTED_VALUE'))