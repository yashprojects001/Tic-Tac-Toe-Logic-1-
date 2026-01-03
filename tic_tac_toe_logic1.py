# STEP 1: Board Representation
# 0 = blank, 1 = X (Human), 2 = O (AI)

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

# STEP 2: Display Board

def print_board(board):
    symbols = [' ', 'X', 'O']
    print()
    for i in range(0, 9, 3):
        print(" ", symbols[board[i]], "|", symbols[board[i+1]], "|", symbols[board[i+2]])
        if i < 6:
            print(" ---+---+---")
    print()

print_board(board)

# STEP 3: Board to Base-3 Number Conversion

def board_to_number(board):
    number = 0
    power = 1
    for cell in board:
        number += cell * power
        power *= 3
    return number

print("Board Number:", board_to_number(board))

# STEP 4: Move Table (Knowledge Base)

movetable = {}

# Rule 1: Empty board → take center
movetable[0] = 4

# Rule 2: If human plays center first → AI plays corner
center_move = 1 * (3 ** 4)
movetable[center_move] = 0

# STEP 5: AI Move Logic (Logic-1)

def ai_move(board):
    board_num = board_to_number(board)

    if board_num in movetable:
        return movetable[board_num]

    # Fallback: choose first empty square
    for i in range(9):
        if board[i] == 0:
            return i

# STEP 6: Human Move

def human_move(board):
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == 0:
            return move
        print("Invalid move. Try again.")

# STEP 7: Win Checking

win_positions = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_winner(player):
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# STEP 8: Main Game Loop

turn = 0

while True:
    print_board(board)

    # Human (X)
    move = human_move(board)
    board[move] = 1
    turn += 1

    if check_winner(1):
        print_board(board)
        print("🎉 You win!")
        break

    if turn == 9:
        print("It's a draw!")
        break

    # AI (O)
    ai = ai_move(board)
    board[ai] = 2
    turn += 1

    if check_winner(2):
        print_board(board)
        print("🤖 AI wins!")
        break
