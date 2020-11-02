# Author : Samuel Lamb
# Date last worked on : 11/1/2020
# Purpose : Reference example of recursion using a factorial function


def factorial(x):
  if x == 1:
    return 1
  else:
    return (x * factorial(x-1))

x = 5
print(factorial(x))