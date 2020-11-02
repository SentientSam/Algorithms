# Author : Samuel Lamb
# Date last worked on : 11/1/2020
# Purpose : Reference example of quick sort
# Quicksort uses recursion, a further example is in Recursion.py


def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
  return quicksort(less) + [pivot] + quicksort(greater)
inputArray = [10, 3, 7, 5, 2]
print(quicksort(inputArray))
