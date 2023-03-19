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

    def get_winner(*win_states):
        # We use a set to create a collection
        # of non repeated elements, if the length of the 
        # set equals to 1 that means all values are the same.
        for state in win_states:
            for sub_state in state:
                search = set(sub_state)
                has_none = None in search
                if len(search) == 1 and not has_none:
                    return search.pop()
        return None

    rows = board
    cols = [[row[i] for row in board] for i in range(3)]
    diagonals = [
        # diagonal
        [board[j][j] for j in range(3)], 
        # inverted diagonal 
        [board[j][-j-1] for j in range(3)] 
    ]

    winner = get_winner(rows, cols, diagonals)
    is_tie = check_tie(board)

    return 'tie' if is_tie else winner
