import math

def print_board(board):
    print("\n-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("-------------")

def check_winner(board):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != ' ':
            return board[state[0]]
    if ' ' not in board:
        return 'Draw'
    return None

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif winner == 'Draw':
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                val = minimax(board, depth + 1, False)
                board[i] = ' '
                best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                val = minimax(board, depth + 1, True)
                board[i] = ' '
                best = min(best, val)
        return best

def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            val = minimax(board, 0, False)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i
    return move

def play_game():
    board = [' '] * 9
    current_player = 'X'

    print("Initial Board:")
    print_board(board)

    while True:
        if current_player == 'X':
            move = best_move(board)
            board[move] = 'X'
            print(f"\nPlayer X chooses position {move}")
        else:
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    print(f"\nPlayer O chooses position {i}")
                    break

        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("\nGame Result: Draw!")
            else:
                print(f"\nWinner: {winner}")
            break

        current_player = 'O' if current_player == 'X' else 'X'
        
play_game()

