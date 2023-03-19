from game import AGENT, PLAYER, find_winner, get_board
from math import inf

SCORES = {
    AGENT: (1, None),
    PLAYER: (-1, None),
    'tie': (0, None)
}

def minimax(board, depth, is_maximizing_player):
    """
    Minimax algorithm.
    Returns a tuple (best_score, best_move). 
    """

    # Check if the game is over or the maximum depth has been reached
    winner = find_winner(board)

    if winner is not None:
        return SCORES[winner]

    # Recursive case
    if is_maximizing_player:
        best_score = -inf
        best_move = None

        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = AGENT
                    score, _ = minimax(board, depth + 1, False)
                    board[i][j] = None
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return (best_score, best_move)

    else: # Minimizing player
        best_score = inf
        best_move = None

        for i in range(3):
            for j in range(3):
                if board[i][j] is None: 
                    board[i][j] = PLAYER
                    score, _ = minimax(board, depth + 1, True)
                    board[i][j] = None
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return (best_score, best_move)



test_board = [
    # 0: 0|1|2
    # 1: 0|1|2
    # 2: 0|1|2
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


turn = AGENT

while find_winner(test_board) is None:
    if turn == AGENT:
        _,moves = minimax(test_board, 0, True)
        x,y = moves
        test_board[x][y] = AGENT 
        print(f'Optimal value: {x},{y}')
        turn = PLAYER
    else:
        x,y = input("Enter the move: ").split(',')
        test_board[int(x)][int(y)] = PLAYER
        turn = AGENT
    print(get_board(test_board))

print(f"the winner is: {find_winner(test_board)}")
