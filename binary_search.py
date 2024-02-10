def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None


def verify(index, target):
  if target is not None:
    print("Target found at index: ", index)
  else:
    print(" " + str(target) + " not found in list")


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(number, 12)
verify(result, 12)

result = binary_search(number, 6)
verify(result, 6)
