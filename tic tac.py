import math


board = [' ' for _ in range(9)]


def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")


def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False


def is_full(b):
    return ' ' not in b


def get_available_moves(b):
    return [i for i, spot in enumerate(b) if spot == ' ']


def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'): return 1
    if check_winner(b, 'X'): return -1
    if is_full(b): return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(b):
            b[move] = 'O'
            score = minimax(b, depth + 1, False)
            b[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(b):
            b[move] = 'X'
            score = minimax(b, depth + 1, True)
            b[move] = ' '
            best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'


def human_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number from 0 to 8.")


def play_game():
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")
    print_board()
    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("🎉 You win!")
            break
        if is_full(board):
            print("🤝 It's a tie!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("💻 AI wins! Better luck next time.")
            break
        if is_full(board):
            print("🤝 It's a tie!")
            break


play_game()
