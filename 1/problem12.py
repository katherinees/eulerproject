'''
Problem 12: Find first triangle number with over 500 divisors.
Method: first number with over 500 divisors is 14414400 (thanks
https://gist.github.com/dario2994/fb4713f252ca86c1254d). A
triangle number is one in the form n(n+1)/2. First triangle
number greater than 14414400 is 14415765, corresponding to
n = 5369. Start there, brute force.
Answer = 76576500
'''
import math

def gen_primes(n):
# print(gen_primes(11)) = [2, 3, 5, 7, 11]
    x = range(2, n+1)
    for i in x:
        j = i*i
        while j < x[-1]+1:
            if j in x:
                x.remove(j)
            j += i
    return x

def prime_factorize(n, primes):
    exp = []
    # ps = []
    for i in primes:
        e = 0
        while n % i == 0:
            # ps.append(i)
            e += 1
            n = n / i
        if e != 0: exp.append(e)
    # print(ps)
    if n != 1:
        print('need larger prime array or maybe n is prime')
    return(exp)

def count_divisors(n, primes):
    exp = prime_factorize(n, primes)
    count = 1
    for e in exp:
        count = count * (e + 1)
    return count

x = gen_primes(1000)
i = 5369
not_found = True
while not_found == True:
    triangle_num = i * (i+1) / 2
    if count_divisors(triangle_num, x) > 500:
        print(triangle_num)
        not_found = False
    i += 1
# print(prime_factorize(26, x))
print(count_divisors(76576500, x))
