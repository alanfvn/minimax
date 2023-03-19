AGENT, PLAYER = 'X', 'O'

def get_board(board):
    board_rep = '\n'
    for i in range(3):
        for j in range(3):
            char = board[i][j] if board[i][j] is not None else ' '
            board_rep +=  f'|{char}|' if j == 1 else char
        if i < 2: 
            board_rep += '\n-+-+-\n'
    return board_rep

def check_tie(board):
    for row in board:
        if None in row:
            return False
    return True

def find_winner(board):
    def get_winner(list):
        search = set(list)
        return search.pop() if len(search) == 1 else None

    # check cols
    for i in range(3):
        # get the columns of the array.
        column = [col[i] for col in board]
        srch = get_winner(column)
        if srch is not None:
            return srch

    # check rows
    for i in range(3):
        srch = get_winner(board[i])
        if srch is not None:
            return srch

    # check diagonals
    diag = [board[j][j] for j in range(3)]
    inverted_diag = [board[j][-j-1] for j in range(3)]
    srch0 = get_winner(diag)
    srch1 = get_winner(inverted_diag)

    if srch0 is not None:
        return srch0

    if srch1 is not None:
        return srch1

    # last check for draw
    is_draw = check_tie(board)
    return 'tie' if is_draw else None
