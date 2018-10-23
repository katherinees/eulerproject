'''
Problem 13: find first 10 digits of the sum of 50
large numbers
Method: only sum the first 20 digits of each of the
original summands.
Answer: 5537376230
'''

f = open('problem13input.txt')
ans = 0
for line in f:
    ans += int(line.strip()[0:20])
print(ans)
