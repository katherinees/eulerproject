# Problem 6
# find the difference between the square of the sum and the sum of the squares of the first 100 natural numbers

import math

squareofsum = (101*50)**2

sumofsquares = 0

for x in range(1, 101):
  sumofsquares = sumofsquares + x**2
  
solution = squareofsum - sumofsquares

print(solution)
