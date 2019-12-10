'''

Problem 16: find sum of digits of 2^1000

Method: Brute force.

Answer: 1366.

'''

x = str(2**1000)
y = 0
for d in x:
  y += int(d)

print(y)
