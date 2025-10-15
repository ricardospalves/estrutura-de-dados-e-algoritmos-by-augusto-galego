def numberOfSteps(number: int) -> int:
  steps = 0

  while(number > 0):
    if number & 1:
      number -= 1
    else:
      number >>= 1
    steps += 1
  
  return steps
