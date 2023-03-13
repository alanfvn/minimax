BOARD = [
    # 0: 0|1|2
    # 1: 0|1|2
    # 2: 0|1|2
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

AGENT, PLAYER = 'X', 'O'

def get_board():
    board = '\n'
    for i in range(3):
        for j in range(3):
            char = BOARD[i][j] if BOARD[i][j] is not None else ' '
            board +=  f'|{char}|' if j == 1 else char
        if i < 2: 
            board += '\n-+-+-\n'
    return board


def find_winner():
    def get_winner(arr):
        # we use a set because it doesn't allow duplicates,
        # so if theres only one element it means someone has won the game.
        search = set(arr)
        if len(search) == 1:
            return search.pop()
        return None

    # check rows
    for i in range(3):
        srch = get_winner(BOARD[i])
        if srch is not None:
            return srch

    # check cols
    for i in range(3):
        # get the columns of the array.
        column = [col[i] for col in BOARD]
        srch = get_winner(column)
        if srch is not None:
            return srch

    # check diagonals
    diag = [BOARD[j][j] for j in range(3)]
    inverted_diag = [BOARD[j][-j-1] for j in range(3)]
    srch0 = get_winner(diag)
    srch1 = get_winner(inverted_diag)

    if srch0 is not None:
        return srch0

    if srch1 is not None:
        return srch1

    # last check for draw
    all_pos = sum(BOARD, [])
    is_draw = not (None in all_pos)

    return 'draw' if is_draw else None


find_winner()
print(get_board())
