class Solution:
  def climbStairs(self, n: int) -> int:
    array_length = (n + 1)
    dynamic_programming = [0] * array_length

    dynamic_programming[0] = 1
    dynamic_programming[1] = 1

    for i in range(2, array_length):
      dynamic_programming[i] = dynamic_programming[i - 1] + dynamic_programming[i - 2]

    return dynamic_programming[n]