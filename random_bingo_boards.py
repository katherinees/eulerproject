# If I have a 4x4 bingo board, and mark 9 spaces, what are the changes of getting 0, 1, 2, or 3 bingos?
# AKA, Katherine got nerdsniped (again)
# If you don't have a python IDE, you can run it online here: https://repl.it/languages/python3
# Output should be:
# 11440 valid boards w 9 spaces marked, and of these:
# 4752 boards with 0 bingos
# 5480 boards with 1 bingo
# 1184 boards with 2 bingos
# 24 boards with 3 bingos

def is_valid_board(b):
    # checks if it's a valid board, with 9 pieces
    x = list(b)
    pieces = 0
    for i in range(len(x)):  
        x[i]= int(x[i])
        pieces += x[i]
    
    if pieces == 9:
        valid = 'Y' 
    elif len(b) == 17:
        valid = 'N'
    else: 
        valid = 'N'
    return valid

def calc_next_board(b):
    #creates the next board by converting to binary and adding 1
    next_board = int(b, 2) + 1
    next_board = bin(next_board)[2:]
    next_board = next_board.rjust(16, '0')
    return next_board

def count_bingos(b):
    # counts the number of bingos on the board
    count = 0
    b = list(b)
    if b[0] == '1' and b[1] == '1' and b[2] == '1' and b[3] == '1':
        count += 1
    if b[4] == '1' and b[5] == '1' and b[6] == '1' and b[7] == '1':
        count += 1
    if b[8] == '1' and b[9] == '1' and b[10] == '1' and b[11] == '1':
        count += 1
    if b[12] == '1' and b[13] == '1' and b[14] == '1' and b[15] == '1':
        count += 1
    if b[0] == '1' and b[4] == '1' and b[8] == '1' and b[12] == '1':
        count += 1
    if b[1] == '1' and b[5] == '1' and b[9] == '1' and b[13] == '1':
        count += 1
    if b[2] == '1' and b[6] == '1' and b[10] == '1' and b[14] == '1':
        count += 1
    if b[3] == '1' and b[7] == '1' and b[11] == '1' and b[15] == '1':
        count += 1
    if b[0] == '1' and b[5] == '1' and b[10] == '1' and b[15] == '1':
        count += 1
    if b[3] == '1' and b[6] == '1' and b[9] == '1' and b[12] == '1':
        count += 1
    return count

potential_board = '0000000111111111'
valid_board_count = 0
bingos0 = 0
bingos1 = 0
bingos2 = 0
bingos3 = 0

while potential_board != '10000000000000000':
    if is_valid_board(potential_board) == 'Y':
        valid_board_count += 1
        bc = count_bingos(potential_board)
        if bc == 0:
            bingos0 += 1
        if bc == 1:
            bingos1 += 1
        if bc == 2:
            bingos2 += 1
        if bc == 3:
            bingos3 += 1

    potential_board = calc_next_board(potential_board)

print('valid board count is ', valid_board_count)
print('boards with 0 bingos: ', bingos0)
print('boards with 1 bingos: ', bingos1)
print('boards with 2 bingos: ', bingos2)
print('boards with 3 bingos: ', bingos3)
