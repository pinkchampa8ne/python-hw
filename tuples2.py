# Write your code here :-)
# Write your code here :-)

def t3_board (board = tuple((tuple(('a', 'b', 'c')), tuple(('d', 'e', 'f')), tuple(('g', 'h', 'i'))))):
    print(board[0][0], '|', board[0][1], '|', board[0][2])
    print('- + - + -')
    print(board[1][0], '|', board[1][1], '|', board[1][2])
    print('- + - + -')
    print(board[2][0], '|', board[2][1], '|', board[2][2])

def game_over(board):
    # Here's a shorter way to do the next line: if ('X', 'X', 'X') in board:
    if board[0] == ('X', 'X', 'X') or board[1] == ('X', 'X', 'X') or board[2] == ('X', 'X', 'X'):
        return True
    if board[0] == ('O', 'O', 'O') or board[1] == ('O', 'O', 'O') or board[2] == ('O', 'O', 'O'):
        return True
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return True
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return True
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return True
    else:
        return False

def game(board = tuple((tuple(('a', 'b', 'c')), tuple(('d', 'e', 'f')), tuple(('g', 'h', 'i')))), y = 1, turn = 1):
    if y == 1:
        var = 'X'
        y = y - 1
    else:
        var = 'O'
        y = y + 1
    move = input('Where would you like to move?')
    if move=='a':
        if board[0][0]=='a':
            board = tuple((tuple((var, board[0][1], board[0][2])), board[1], board[2]))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='b':
        if board[0][1]=='b':
            board = tuple((tuple((board[0][0], var, board[0][2])), board[1], board[2]))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='c':
        if board[0][2]=='c':
            board = tuple((tuple((board[0][0], board[0][1], var)), board[1], board[2]))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='d':
        if board[1][0]=='d':
            board = tuple((board[0], tuple((var, board[1][1], board[1][2])), board[2]))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='e':
        if board[1][1]=='e':
            board = tuple((board[0], tuple((board[1][0], var, board[1][2])), board[2]))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='f':
        if board[1][2]=='f':
            board = tuple((board[0], tuple((board[1][0], board[1][1], var)), board[2]))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='g':
        if board[2][0]=='g':
            board = tuple((board[0], board[1], tuple((var, board[2][1], board[2][2]))))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='h':
        if board[2][1]=='h':
            board = tuple((board[0], board[1], tuple((board[2][0], var, board[2][2]))))
        else:
            raise ValueError('That square is taken, please try again.')
    if move=='i':
        if board[2][2]=='i':
            board = tuple((board[0], board[1], tuple((board[2][0], board[2][1], var))))
        else:
            raise ValueError('That square is taken, please try again.')
    t3_board(board)
    if game_over(board) == True:
        print('Tic Tac Toe!', var, 'wins!')
    elif turn == 9:
        print('Tie! No one wins :(')
    else:
        turn = turn + 1
        game(board,y,turn)

t3_board()
game()
