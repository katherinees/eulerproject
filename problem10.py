'''
Problem 10: find sum of primes below 2000000.
Use Sieve of Eratosthenes.
Answer: 142913828922.
'''

def gen_primes(n):
    x = [True]*(n+1)
    x[0] = False
    x[1] = False
    i = 0
    while i < len(x):
        if x[i] == True:
            j = i*i
            while j < len(x):
                x[j] = False
                j = j + i
        i += 1
    return x

primes = gen_primes(2000000)
sum_of_primes = 0
i = 0
while i < len(primes):
    if primes[i] == True:
        sum_of_primes += i
    i += 1

print(sum_of_primes)
