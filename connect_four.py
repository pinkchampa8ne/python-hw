ROW_COUNT = 6
COLUMN_COUNT = 7

def align_all_columns(board=None, aligned_board=None):
    if board == None:
        board = []
        for col in range(COLUMN_COUNT):
            board.append([] * ROW_COUNT)
    if aligned_board == None:
        aligned_board = []
        for col in range(COLUMN_COUNT):
            aligned_board.append([] * ROW_COUNT)
    for n in range(len(board)):
        empty_column = [" "] * ROW_COUNT
        new_column = empty_column + board[n]
        aligned_board[n] = new_column[-6:]
    draw_grid(aligned_board)
    game_over(aligned_board)
    if game_over(aligned_board) == True:
        return True

def draw_grid(aligned_board=None):
    if aligned_board == None:
        aligned_board = []
        for col in range(COLUMN_COUNT):
            aligned_board.append([] * ROW_COUNT)
    all_rows = [[], [], [], [], [], []]
    for index in range(len(aligned_board)):
        for element in range(len(all_rows)):
            all_rows[element].append(aligned_board[index][element])
    for element in range(len(all_rows)):
        print()
        print("|", sep="", end="")
        for col in range(COLUMN_COUNT):
            print(all_rows[element][col], "|", sep="", end="")
    print("\n", "-" * 15, sep="")
    for col in range(COLUMN_COUNT):
        print(" ", col, sep="", end="")
    print()

def game_over(aligned_board=None):
    if aligned_board == None:
        aligned_board = []
        for col in range(COLUMN_COUNT):
            aligned_board.append([] * ROW_COUNT)
    winX = ["X", "X", "X", "X"]
    winO = ["O", "O", "O", "O"]
    all_rows = [[], [], [], [], [], []]
    for index in range(len(aligned_board)):
        for value in range(len(aligned_board[index])):  # tests vertical
            col_test = aligned_board[index][value : value + 4]
            if col_test == winX or col_test == winO:
                return True
        for element in range(len(all_rows)):
            all_rows[element].append(aligned_board[index][element])
            for value in range(len(all_rows[element])):  # tests horizontal
                row_test = all_rows[element][value : value + 4]
                if row_test == winX or row_test == winO:
                    return True
    diag_up_row = [[], [], [], []]
    for index in range(4):  # tests diagonals going down & right by row ("up" in row & col #)
        y = index
        for subindex in range(ROW_COUNT):
            diag_up_row[index].append(aligned_board[y][subindex])
            y = y + 1
            if y > ROW_COUNT:
                break
        for value in range(len(diag_up_row[index])):
            diag1_test = diag_up_row[index][value : value + 4]
            if diag1_test == winX or diag1_test == winO:
                return True
    diag_down_row = [[], [], [], []]
    for index in range(4):  # tests diagonals going down & left by row ("down" in col #, up in row #)
        y = index + 3
        for subindex in range(ROW_COUNT):
            diag_down_row[index].append(aligned_board[y][subindex])
            y = y - 1
            if y < 0:
                break
        for value in range(len(diag_down_row[index])):
            diag2_test = diag_down_row[index][value : value + 4]
            if diag2_test == winX or diag2_test == winO:
                return True
    diag_up_col = [[], []]
    for index in range(2):  # tests diagonals going down & right in 2nd & 3rd rows of first column
        y = 0
        for subindex in range(1, ROW_COUNT - 1):
            diag_up_col[index].append(aligned_board[y][subindex + index])
            y = y + 1
            if subindex + index > ROW_COUNT - 1:
                break
        for value in range(len(diag_up_col[index])):
            diag3_test = diag_up_col[index][value : value + 4]
            if diag3_test == winX or diag3_test == winO:
                return True
    diag_down_col = [[], []]
    for index in range(2):  # tests diagonals going down & left in 2nd & 3rd rows of last column
        y = 6
        for subindex in range(1, ROW_COUNT - 1):
            diag_down_col[index].append(aligned_board[y][subindex + index])
            y = y - 1
            if subindex + index > ROW_COUNT - 1:
                break
        for value in range(len(diag_down_col[index])):
            diag4_test = diag_down_col[index][value : value + 4]
            if diag4_test == winX or diag4_test == winO:
                return True

def play_turn(board=None, is_x_turn=True, turn=0):
    if board == None:
        board = []
        for col in range(COLUMN_COUNT):
            board.append([] * ROW_COUNT)
    if is_x_turn == True:
        var = "X"
        is_x_turn = False
    else:
        var = "O"
        is_x_turn = True
    move = input("Where would you like to move?")
    for col in range(7):
        if move == str(col):
            if len(board[col]) == ROW_COUNT:
                raise ValueError("This column is full.")
            else:
                board[col] = [var] + board[col]
    if move not in ("0", "1", "2", "3", "4", "5", "6"):
        raise ValueError("That is not one of the possible choices.")
    if align_all_columns(board) == True:
        print("Connect Four!", var, "wins!")
    elif turn == 41:
        print("Tie! No one wins.")
    else:
        turn = turn + 1
        play_turn(board, is_x_turn, turn)

align_all_columns()
play_turn()
