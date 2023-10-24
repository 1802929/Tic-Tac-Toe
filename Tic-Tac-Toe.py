import random

# Tic-Tac-Toe board representation
board = [' ' for _ in range(9)]

# Define winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

# Function to check if the board is full
def is_full(board):
    return ' ' not in board

# Function to check if a player has won
def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to evaluate the board
def evaluate(board):
    if check_win(board, 'X'):
        return 1
    if check_win(board, 'O'):
        return -1
    return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player):
    if check_win(board, 'X'):
        return 1
    if check_win(board, 'O'):
        return -1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Function to make the AI's move using Minimax with Alpha-Beta Pruning
def make_ai_move(board):
    best_move = -1
    best_eval = float('-inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False)
            board[i] = ' '

            if eval > best_eval:
                best_eval = eval
                best_move = i

    board[best_move] = 'X'

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= player_move < 9 and board[player_move] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")

        board[player_move] = 'O'
        print_board(board)

        if check_win(board, 'O'):
            print("You win! Congratulations!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        make_ai_move(board)
        print_board(board)

        if check_win(board, 'X'):
            print("AI wins! Better luck next time!")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()