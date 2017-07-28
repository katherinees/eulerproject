# Problem 2
# sum of even Fibonacci numbers less than four million

x = 1
y = 2
z = 0
sum = 0

while (x <= 4000000):
  if (x % 2 == 0):
    sum = sum + x
  z = x
  x = y
  y = z + y

print(sum)
