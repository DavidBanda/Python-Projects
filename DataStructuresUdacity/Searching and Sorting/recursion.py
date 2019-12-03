"""
def getFib(position):

  if position == 0:
      return 0

  if position == 1:
      return 1

  first = 0
  second = 1
  next = first + second

  for i in range(2, position):

      first = second
      second = next
      next = first + second

  return next
    """
