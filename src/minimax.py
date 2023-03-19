from pickle import TRUE
from game import AGENT, PLAYER, find_winner

# score to return based on the type of winner.
score_ref = {
    'X': 1,
    'O': -1,
    'tie': 0
}

def optimal_move(board):
    bestScore = float('-inf')
    # position on the board with the optimal move.
    bestMove = (None,None)

    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                continue


def get_initial_score(maximizing):
    if maximizing:
        return float('-inf')
    else:
        return float('inf')

def get_player(maximizing):
    if maximizing:
        return AGENT
    else:
        return PLAYER

def calculate_score(cScore, bScore, maximizing):
    if maximizing:
        return max(cScore, bScore)
    else:
        return min(cScore, bScore)


def minimax(board, depth, maximizing):
    bestScore = get_initial_score(maximizing)
    winner = find_winner(board)

    if winner is not None:
        return score[winner]

    for i in range(3):
        for j in range(3):
            # avoid non empty spots.
            if board[i][j] is not None:
                continue

            # place the next move.
            board[i][j] = get_player(maximizing)
            # compute the new score.
            score = minimax(board, depth+1, not maximizing)
            # store the best score.
            bestScore = calculate_score(score, bestScore, maximizing)

    # finally return the best score.
    return bestScore
    
print(get_player(True))
