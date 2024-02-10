#liner_search algo

# def liner_search(list, target):
#   for i in range(0, len(list)):
#     if list[i] == target:
#       return i
#   return None

# def verify(index, target):
#   if index is not None:
#     print("Target found at index: ", index)
#   else:
#     print("" + str(target) + " not found in list")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = liner_search(numbers, 14)
# verify(result, 10)

def liner_search(list, target):
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None

def verify(index, target):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print(" " + str(target) + " not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = liner_search(numbers, 14)
verify(result, 14) 