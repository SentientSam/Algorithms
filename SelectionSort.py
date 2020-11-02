# Author : Samuel Lamb
# Date last worked on : 11/1/2020
# Purpose : Reference example of selection sort


# import time
# start_time = time.time()
def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range (1,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr
array = [5,3,6,2,10]
print(selectionSort(array))
# print("--- %s seconds ---" % (time.time() - start_time))