from game import AGENT, PLAYER, GAME_BOARD, attempt_human_move, find_winner, get_board_draw
from minimax import minimax
from util import ask_question, clean, delay


def main():
    clean()
    start_first = ask_question("\nDeseas iniciar primero? [S/N]: ", ['S','N'])
    # set whos going first.
    turn = PLAYER if start_first == 'S' else AGENT

    while find_winner(GAME_BOARD) is None:
        if turn == AGENT:
            _,moves = minimax(GAME_BOARD, 0, True)
            i,j = moves
            turn = PLAYER
            GAME_BOARD[i][j] = AGENT 
            print(f'\n[AI]: Movida optima encontrada: [{i},{j}]')
            delay(2)
        else:
            move = ask_question("\nIngresa tu movida (1,9): ", [f'{x}' for x in range(1,10)])
            try:
                attempt_human_move(int(move))
                turn = AGENT
            except (Exception): 
                print(f"\n[!] Esa posicion ya esta ocupada!")
                delay(1)

        clean()
        print(get_board_draw())

    winer = find_winner(GAME_BOARD)
    print(f"\nEL GANADOR ES: {winer.upper()}")
    

if __name__ == "__main__":
    main()
