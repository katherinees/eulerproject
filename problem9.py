# Problem 9
# find the product abc such that a + b + c = 1000, a^2 + b^2 = c^2, and a < b < c

# we can equivalently think of this as finding the integral lengths of sides of a 
# scalene right triangle with perimeter of 1000

# then we can use the triangle inequality rules:
# a + b > c, a + c > b, b + c > a

# then since a + b = 1000 - c and a + b > c, it follows that c < 500

# these restrictions reduce number of cases to test by over 90%

for a in range(1,498):
  for b in range (a,499):
    c = 1000-a-b
    if (c < 500) & (b < c) & (a + b > c) & (a + c > b) & (b + c > a): 
      if (a**2 + b**2 == c**2):
        print(a*b*c)
        break
