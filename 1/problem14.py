'''
Problem 14: find number which starts longest Collatz
sequence less than 1000000.
Method: mostly brute force, avoiding rechecking numbers
Answer: 837799.
'''
i = 1
collatz = {}
while i < 1000001:
    start = i
    count = 1
    while start != 1:
        if str(start) in collatz:
            collatz[str(i)] = count + collatz[str(start)]
        if start % 2 == 0:
            start = start/2
        else:
            start = 3*start + 1
        count = count + 1
    collatz[str(i)] = count
    i = i + 1

print(max(collatz, key=collatz.get))
