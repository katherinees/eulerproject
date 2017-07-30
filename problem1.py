import math

# Euler Project Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.

# firstly, observe that the numbers which are multiples of both 3 and 5 are exactly the numbers which are multiples of 15.

# find number of multiples of 3, 5, and 15 strictly less than 1000 by 
numberMultiplesOf3 = math.floor(999/3)
numberMultiplesOf5 = math.floor(999/5)
numberMultiplesOfBoth3and5 = math.floor(999/15)

# next, find the sums of the multiples of 3, 5, and 15.
# observe that the sum of the first n multiples of 3 can be written as
# 3*1 + 3*2 + ... + 3*n = 3(1 + 2 + ... + n)
# but 1 + 2 + ... + n is the nth triangle number
# the nth triangle number is n(n + 1)/2
sumMultiplesOf3 = 3 * numberMultiplesOf3 * (numberMultiplesOf3 + 1) * 0.5;
sumMultiplesOf5 = 5 * numberMultiplesOf5 * (numberMultiplesOf5 + 1) * 0.5;
sumMultiplesOfBoth3and5 = 15 * numberMultiplesOfBoth3and5 * (numberMultiplesOfBoth3and5 + 1) * 0.5;

sumMultiplesOf3or5 = sumMultiplesOf3 + sumMultiplesOf5 - sumMultiplesOfBoth3and5;
# we subtract the sum of multiples of both 3 and 5, because otherwise they'd be counted twice.

print(sumMultiplesOf3or5)
