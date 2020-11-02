# Author : Samuel Lamb
# Date last worked on : 11/1/2020
# Purpose : Reference example of recursion using a factorial function
# Further use of recursion can be seen in the Quicksort.py file

def factorial(x):
  if x == 1:
    return 1
  else:
    return (x * factorial(x-1))

x = 5
print(factorial(x))