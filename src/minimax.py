from game import AGENT, PLAYER, find_winner
from math import inf

SCORES = {
    AGENT: (1, None),
    PLAYER: (-1, None),
    'tie': (0, None)
}

def minimax(board, depth, maximazing):
    """
    Minimax algorithm.
    Returns a tuple with the best_score and the best_move). 
    """
    # Check if the game is over 
    winner = find_winner(board)

    if winner is not None:
        return SCORES[winner]

    if maximazing:
        # Maximazing player
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

    else: 
        # Minimizing player
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
