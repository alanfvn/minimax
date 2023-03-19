GAME_BOARD = [
    # 0: 0|1|2
    # 1: 0|1|2
    # 2: 0|1|2
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


AGENT, PLAYER = 'X', 'O'

def spot_available(x,y):
    return GAME_BOARD[x][y] is None

def attempt_human_move(number):
    moves = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
    }
    x,y = moves[number]
    good_move = spot_available(x,y)

    if good_move:
        GAME_BOARD[x][y] = PLAYER
    else:
        raise Exception('Invalid player move')

def get_board_draw():
    separator = '---------------'
    draw = f'\n{separator}\n'

    for row in GAME_BOARD:
        for cell in row:
            symbol = ' ' if cell is None else cell
            draw += f'| {symbol} |'
        draw += f'\n{separator}\n'
    return draw


def check_tie(board):
    for row in board:
        if None in row:
            return False
    return True

def find_winner(board):
    # TODO: refactor this
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

    # last check for ties 
    is_tie = check_tie(board)
    return 'tie' if is_tie else None
