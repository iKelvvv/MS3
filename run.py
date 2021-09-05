# Import function to generate random integers
from random import randint

board = []
cpu_board = []

for x in range(7):
    """
    Generates the size of the playing board
    """
    board.append(["-"] * 7)
    cpu_board.append(["_"] * 7)


def p_board(board):
    """
    Formats the correct layout for the player's board
    """
    for row in board:
        print(" ".join(row))


def c_board(cpu_board):
    """
    Formats the correct layout for the computer's board
    """
    for row in cpu_board:
        print(" ".join(row))


def print_boards():
    """
    Print both sets of boards
    """
    print("Players Board:")
    p_board(board)
    print(" ")
    print("Computers Board:")
    c_board(cpu_board)


def location_col(board):
    """
    Generate a random column for the computer's ship
    """
    return randint(0, len(board) - 1)


def location_row(board):
    """
    Generate a random row for the computer's ship
    """
    return randint(0, len(board) - 1)


def cpu_location_row(cpu_board):
    """
    Generate a random column for the player's ship
    """
    return randint(0, len(cpu_board) - 1)


def cpu_location_col(cpu_board):
    """
    Generate a random row for the player's ship
    """
    return randint(0, len(cpu_board) - 1)


ship_row = location_row(board)
ship_col = location_col(board)
while True:
    ship_row2 = location_row(board)
    ship_col2 = location_col(board)
    if ship_row2 != ship_row and ship_col2 != ship_col:
        ship_row3 = location_row(board)
        ship_col3 = location_col(board)
        if (ship_row3 != ship_row2 and ship_col3 != ship_col2) and \
            (ship_row3 != ship_row and ship_col3 != ship_col):
            break


cpu_ship_row = cpu_location_row(cpu_board)
cpu_ship_col = cpu_location_col(cpu_board)
while True:
    cpu_ship_row2 = location_row(board)
    cpu_ship_col2 = location_col(board)
    if cpu_ship_row2 != cpu_ship_row and cpu_ship_col2 != cpu_ship_col:
        cpu_ship_row3 = location_row(board)
        cpu_ship_col3 = location_col(board)
        if (cpu_ship_row3 != cpu_ship_row2 and cpu_ship_col3 != cpu_ship_col2) and \
            (cpu_ship_row3 != cpu_ship_row and cpu_ship_col3 != cpu_ship_col):
            break




def print_cpu_guess():
    """
    Print CPU guess row and col function
    """
    print("The CPU guessed:")
    print(f"Row: {cpu_guess_row + 1}, Col: {cpu_guess_col + 1}")


def welcome_instructions():
    """
    Intructions function to explain the how the game is played.
    """
    print("Welcome to battleships!")
    print("Board size: 7x7. Top left corner is row: 0, col: 0")
    print("Number of ships 1")
    print("You have 3 guesses before you lose!")
    print("Warning guessing the same spot twice will count as a turn!\n")


# Main game logic
welcome_instructions()
board[ship_row][ship_col] = "S"
board[ship_row2][ship_col2] = "S"
board[ship_row3][ship_col3] = "S"

cpu_board[cpu_ship_row][cpu_ship_col] = "S"
cpu_board[cpu_ship_row2][cpu_ship_col2] = "S"
cpu_board[cpu_ship_row3][cpu_ship_col3] = "S"
print_boards()
for guess in range(4):
    if guess == 3:
        print("Game over! Too many incorrect guesses.")
        break

    print("Turn: " + str(guess + 1))

    while True:
        try:
            guess_row = int(input("Guess Row: ")) - 1
            guess_col = int(input("Guess Col: ")) - 1
            break
        except ValueError:
            print("Not an integer. Try Again")
            continue

    cpu_guess_row = randint(0, len(board) - 1)
    cpu_guess_col = randint(0, len(board) - 1)
    
    if (guess_row == cpu_ship_row and guess_col == cpu_ship_col) or \
        (guess_row == cpu_ship_row2 and guess_col == cpu_ship_col2) or \
            (guess_row == cpu_ship_row3 and guess_col == cpu_ship_col3) :
        cpu_board[guess_row][guess_col] = "X"
        print("Congratulations! You sank the CPU battleship!")
        guess = + 1
        print("Game over! You win!")
        break
        if (cpu_guess_row == ship_row and cpu_guess_col == ship_col) or \
            (cpu_guess_row == ship_row2 and cpu_guess_col == ship_col2) or \
                (cpu_guess_row == ship_row3 and cpu_guess_col == ship_col3):
            board[cpu_guess_row][cpu_guess_col] = "X"
            print_boards()
            print_cpu_guess()
            print("The CPU sank your battleship!")
            print("Game over! You lose!")
            break
        else:
            board[cpu_guess_row][cpu_guess_col] = "O"
            print_cpu_guess()
            print("The CPU missed!")
    else:
        if guess_row not in range(7) or guess_col not in range(7):
            print("Oops, value is not in range")
            print_boards()
        elif cpu_board[guess_row][guess_col] == "X" or \
                cpu_board[guess_row][guess_col] == "O":
            print("You already fired here")
            print_boards()
        else:
            cpu_board[guess_row][guess_col] = "O"
            print("You missed!")
            print_boards()
            if (cpu_guess_row == ship_row and cpu_guess_col == ship_col) or \
                (cpu_guess_row == ship_row2 and cpu_guess_col == ship_col2) or \
                    (cpu_guess_row == ship_row3 and cpu_guess_col == ship_col3):
                board[cpu_guess_row][cpu_guess_col] = "X"
                print_boards()
                print_cpu_guess()
                print("The CPU sank your battleship!")
                print("Game over! You lose!")
                break
            else:
                board[cpu_guess_row][cpu_guess_col] = "O"
                print_cpu_guess()
                print("The CPU missed!")
                guess = + 1
    