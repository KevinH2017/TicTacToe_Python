# Milestone Project 1: Create simple Tic-Tac-Toe board that takes user input
############################################################################


test_board_full = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
test_board = [' '] * 10

# Displays board
def display_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    #print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    #print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])


# Checks if player input X or O
def player_input():
    marker = ' '
    acceptable_values = ['X', 'O']
    while marker not in acceptable_values:
        marker = input("Player 1, choose 'X' or 'O': ").upper() # Converts to uppercase letter
        if marker not in acceptable_values:
            print("Invalid Choice! Try Again!")
    player1 = marker  
    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Takes board and puts X or O on it
def place_marker(board, marker, position):
    values = range(0,10)
    while position in values:
        board[position] = marker
        break    
    return board[position]


# Checks if a marker wins
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark))


# Checks if a space is empty
def space_check(board, position):
    # empty = ' '
    # if empty in board[position]:
    #     return True     # Space is empty
    # else:
    #     return False    # Space is taken
    return board[position] == ' '


# Checks if the board is full
def full_board_check(board):
    # empty = ' '
    # if empty in board:
    #     return False    # Board still has empty spaces
    # else:
    #     return True     # Board is full
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Takes and tests input for player's next position (1-9)
# Follows Numpad order
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Enter Next Position (1-9): "))
    return position
    

# Asks player if they want to play again
def replay():
    play_again = input("Rematch? (Y or N): ").upper()
    return play_again == "Y"

# Randomly chooses who goes first
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Start of game
print("Welcome to Tic Tac Toe!")

while True:
    # Set the game up here
    game_on = True
    game_board = [' '] * 10
    p1, p2 = player_input()                   # Player 1 and 2 chooses marker
    # turn = choose_first()
    # print(turn + " will go first")
    display_board(game_board)


    while game_on:
        # Player 1's Turn
        print("Player 1's Turn")
        tile_place = player_choice(game_board)    # Player chooses position (1-9)
        place_marker(game_board, p1, tile_place)
        display_board(game_board)

        if win_check(game_board, p1):
            print("Player 1 Wins")
            game_on = False
            break
        else: 
            if full_board_check(game_board):
                print("Draw")
                game_on = False
                break

        # Player 2's turn
        print("Player 2's Turn")
        tile_place = player_choice(game_board)   # Player chooses position (1-9)
        place_marker(game_board, p2, tile_place)
        display_board(game_board)

        if win_check(game_board, p2):
            print("Player 2 Wins")
            game_on = False
            break
        else:
            if full_board_check(game_board):
                print("Draw")
                game_on = False
                break

    if not replay():
        print("Closing Game...")
        break