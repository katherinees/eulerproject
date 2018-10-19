'''
Problem 11: find largest product of four adjacent
numbers in a grid (see input file).
Method: Brute force.
Answer: 70600674.
'''

import csv

f = open('problem11input.txt', 'r')
rows = []
for line in f:
    x = line.strip().split(' ')
    y = []
    for k in x:
        y.append(int(k))
    rows.append(y)

best_row = 0
for r in rows:
    i = 0
    while i < len(r)-4:
        poss = r[i]*r[i+1]*r[i+2]*r[i+3]
        if poss > best_row:
            best_row = poss
        i += 1

best_vert = 0
for r in range(len(rows)-3):
    i = 0
    while i < len(rows[0]):
        poss = rows[r][i]*rows[r+1][i]*rows[r+2][i]*rows[r+3][i]
        if poss > best_vert:
            best_vert = poss
        i += 1

best_grave = 0
for r in range(len(rows)-3):
    i = 0
    while i < len(rows[0])-3:
        poss = rows[r][i]*rows[r+1][i+1]*rows[r+2][i+2]*rows[r+3][i+3]
        if poss > best_grave:
            best_grave = poss
        i += 1

best_aigu = 0
for r in range(len(rows)-3):
    i = 0
    while i < len(rows[0])-3:
        poss = rows[r+3][i]*rows[r+2][i+1]*rows[r+1][i+2]*rows[r][i+3]
        if poss > best_aigu:
            best_aigu = poss
        i += 1

print(max(best_row, best_vert, best_grave, best_aigu))
