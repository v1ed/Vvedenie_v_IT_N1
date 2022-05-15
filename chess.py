import numpy as np
from random import randint


def output(mtx):
    print('Итоговая матрица:')
    print('\n+' + ('-' * 7 + '+') * 8)
    for i in mtx:
        print('|', end='\t')
        for j in i:
            if j != 0:
                print(int(j), end='\t|\t')
            else:
                print(' ', end='\t|\t')
        print()
        print('+' + ('-' * 7 + '+') * 8)


shapes_count = 0
size = 8

chess_board = np.zeros((size, size))
rand_x = randint(0, size - 1)
rand_y = randint(0, size - 1)
chess_board[rand_x][rand_y] = 1

chess_board_flipped = np.fliplr(chess_board)

while shapes_count < size - 1:
    s1 = 0
    s2 = 0
    rand_x = randint(0, size - 1)
    rand_y = randint(0, size - 1)

    while chess_board[rand_x][rand_y] == 1:
        rand_x = randint(0, size - 1)
        rand_y = randint(0, size - 1)

    chess_board[rand_x][rand_y] = 1
    chess_board_flipped = np.fliplr(chess_board)

    for i in range(-size + 2, size - 1):
        diag = chess_board.diagonal(i)
        second_diag = chess_board_flipped.diagonal(i)
        s1 = sum(diag)
        s2 = sum(second_diag)
        if s1 > 1 or s2 > 1:
            chess_board[rand_x][rand_y] = 0
            chess_board_flipped = np.fliplr(chess_board)
            break
        chess_board_flipped = np.fliplr(chess_board)
    if s1 <= 1 and s2 <= 1:
        shapes_count += 1

output(chess_board)