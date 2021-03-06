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


def cpu_location_col(cpu_board):
    """
    Generate a random row for the player's ship
    """
    return randint(0, len(cpu_board) - 1)


def cpu_location_row(cpu_board):
    """
    Generate a random column for the player's ship
    """
    return randint(0, len(cpu_board) - 1)


# Logic for the user ships to not generate the same coordinates
ship_col = location_col(board)
ship_row = location_row(board)
while True:
    ship_col2 = location_col(board)
    ship_row2 = location_row(board)
    if ship_row2 != ship_row and ship_col2 != ship_col:
        ship_col3 = location_col(board)
        ship_row3 = location_row(board)
        if (ship_row3 != ship_row2 and ship_col3 != ship_col2) and \
                (ship_row3 != ship_row and ship_col3 != ship_col):
            break


# Logic for the CPU ships to not generate the same coordinates
cpu_ship_col = cpu_location_col(cpu_board)
cpu_ship_row = cpu_location_row(cpu_board)
while True:
    cpu_ship_col2 = location_col(board)
    cpu_ship_row2 = location_row(board)
    if cpu_ship_row2 != cpu_ship_row and cpu_ship_col2 != cpu_ship_col:
        cpu_ship_col3 = location_col(board)
        cpu_ship_row3 = location_row(board)
        if (cpu_ship_row3 != cpu_ship_row2 and
            cpu_ship_col3 != cpu_ship_col2) and \
            (cpu_ship_row3 != cpu_ship_row and
                cpu_ship_col3 != cpu_ship_col):
            break


def print_cpu_guess():
    """
    Print CPU guess row and col function
    """
    print("The CPU guessed:")
    print(f"Column: {cpu_guess_col + 1}, Row: {cpu_guess_row + 1}")


def welcome_instructions():
    """
    Intructions function to explain the how the game is played.
    """
    print("Welcome to battleships!")
    print("A Column goes from left to right")
    print("A Row goes from up to down")
    print("Board size: 7x7. Top left corner is col: 1, row: 1")
    print("Number of ships: 3 each")
    print("You have 8 guesses before you lose!")
    print("To run the game again, select run program")


# Main game logic
hit_count = 0
cpu_hit_count = 0
welcome_instructions()
# Display user ships on user board
board[ship_col][ship_row] = "S"
board[ship_col2][ship_row2] = "S"
board[ship_col3][ship_row3] = "S"
print_boards()
guess = 0
cpu_guess_col_row_validation = []
while guess < 9:
    # After 8 turns the game will end.
    if guess == 8:
        print("Game over! Too many incorrect guesses.")
        break

    print("Turn: " + str(guess + 1))

    # Validation to check that user input is an integer
    while True:
        try:
            guess_col = int(input("Guess Column: ")) - 1
            guess_row = int(input("Guess Row: ")) - 1
            break
        except ValueError:
            print("Not an integer. Try Again")
            continue

# Generates CPU guess, if its already been generated then try new coordinates
    while True:
        cpu_guess_col = randint(0, len(board) - 1)
        cpu_guess_row = randint(0, len(board) - 1)

        if [cpu_guess_row, cpu_guess_col] in cpu_guess_col_row_validation:
            continue
        else:
            cpu_guess_col_row_validation.append([cpu_guess_row, cpu_guess_col])
            break

    # Logic for if user guesses correctly
    if (guess_row == cpu_ship_row and
        guess_col == cpu_ship_col) \
        or (guess_row == cpu_ship_row2 and guess_col == cpu_ship_col2) \
            or (guess_row == cpu_ship_row3 and guess_col == cpu_ship_col3):
        cpu_board[guess_row][guess_col] = "X"
        hit_count = hit_count + 1
        if hit_count == 1:
            print("You sank the first CPU battleship!")
        elif hit_count == 2:
            print("You sank the second CPU battleship!")
        elif hit_count == 3:
            print("Congratulations! You sunk all CPU battleships!")
            print("Game over! You win!")
            print_boards()
            break
        # Logic for if CPU guesses correctly
        if (cpu_guess_row == ship_row and cpu_guess_col == ship_col) or \
            (cpu_guess_row == ship_row2 and cpu_guess_col == ship_col2) or \
                (cpu_guess_row == ship_row3 and cpu_guess_col == ship_col3):
            board[cpu_guess_row][cpu_guess_col] = "X"
            print_boards()
            print_cpu_guess()
            cpu_hit_count = cpu_hit_count + 1
            if cpu_hit_count == 1:
                print("The CPU sank your first battleship!")
            elif cpu_hit_count == 2:
                print("The CPU sank your second battleship!")
            elif cpu_hit_count == 3:
                print("Game over! The CPU sank all your ships!")
                print("Game over! You lost!")
                print_boards()
                break
        else:
            # Logic for if CPU guesses incorrectly
            board[cpu_guess_row][cpu_guess_col] = "O"
            print_boards()
            print_cpu_guess()
            print("The CPU missed!")
        guess += 1
    else:
        # Logic for if user guesses a value that is not in range
        if guess_row not in range(7) or guess_col not in range(7):
            print("Oops, value is not in range")
            print_boards()
        # Logic for if user guesses coordinates that they have already guessed
        elif cpu_board[guess_row][guess_col] == "X" or \
                cpu_board[guess_row][guess_col] == "O":
            print("You already fired here")
            print_boards()
        else:
            # Logic for if user guesses incorrectly
            cpu_board[guess_row][guess_col] = "O"
            print("You missed!")
            # Logic for if CPU guesses correctly
            if (cpu_guess_row == ship_row and
                cpu_guess_col == ship_col) or \
                (cpu_guess_row == ship_row2 and
                    cpu_guess_col == ship_col2) or \
                (cpu_guess_row == ship_row3 and
                    cpu_guess_col == ship_col3):
                board[cpu_guess_row][cpu_guess_col] = "X"
                print_boards()
                print_cpu_guess()
                cpu_hit_count = cpu_hit_count + 1
                if cpu_hit_count == 1:
                    print("The CPU sank your first battleship!")
                    guess = + 1
                elif cpu_hit_count == 2:
                    print("The CPU sank your second battleship!")
                    guess = + 1
                elif cpu_hit_count == 3:
                    print("The CPU sunk all your battleships!")
                    guess = + 1
                    print("Game over! You lost!")
                    print_boards()
                    break
            else:
                # Logic for if CPU guesses incorrectly
                board[cpu_guess_row][cpu_guess_col] = "O"
                print_boards()
                print_cpu_guess()
                print("The CPU missed!")
            guess += 1

print("To run the game again, select run program")
