import math

# Tic-Tac-Toe board
board = [' ' for _ in range(9)]  # A list to hold the board state
player = 'X'  # Human player
ai = 'O'      # AI player

# Function to print the Tic-Tac-Toe board
def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a winner
def is_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, ai):
        return 1
    elif is_winner(board, player):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI's move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = ai

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print_board()

    while True:
        # Human's move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] == ' ':
            board[human_move] = player
            print_board()
        else:
            print("Invalid move, try again.")
            continue

        # Check if the human won
        if is_winner(board, player):
            print("Congratulations! You win!")
            break

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI's move
        ai_move()
        print("AI played:")
        print_board()

        # Check if the AI won
        if is_winner(board, ai):
            print("AI wins! Better luck next time!")
            break

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            break

# Start the game
play_game()
