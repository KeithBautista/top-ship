# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import time

"""
----- GLOBAL VARIABLES -----
"""

# Grid as a whole
grid = [[]]

# Grid Size, To be manipulated based on input of user
grid_size = 10

# The amount of Ships user can place on Grid
num_of_ships = 8

# Bullets Left
bullets_left = 50

# If Game is Over
game_over = False

# Number of ships sunk
num_of_ships_sunk = 0

# Ship Positions on Grid
ship_positions = [[]]

# Alphabet to be used on the x axis of the board
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""
----- METHODS -----
"""

# Validation for placing ship on grid


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row and or column to validate the placement of ship
       on the grid.
       This will also return either True or False"""
    global grid
    global ship_positions

    """
    All valid is true, if not valid and grid does not contain . then false.
    """
    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    """
    If all valid then append the ships positions as '0'
    """
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "0"
    return all_valid

# Based on directions will try place ship on grid


def try_place_ship_grid(row, col, direction, length):
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

# Creating the Grid


def create_grid():
    """
    Will create a grid based on user input and randomly place
    down ships of different sizes and in different directions.
    Has no Return but will use try_place_ship_grid
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_sunk = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_place_ship_grid(random_row, random_col, direction, ship_size):
            num_of_ships += 1

# Print Grid


def print_grid():
    """
    This method will print the grid while rows using the alphabet
    and the columns using integers
    """
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=")")
        for col in range(len(grid[row])):
            if grid[row][col] == "0":
                if debug_mode:
                    print("0", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")

# Check Valid Bullet Placement


def accept_valid_bullet_placement():
    """
    Will validate row and column that has been placed by user on board
    Has Return and row, col are both integers
    """
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.alpha() or not col.isnumeric():
            print('''Error: Please enter letter (A-J) for row and (0-9) for
            column''')
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print('''Error: Please enter letter (A-J) for row and (0-9) for
            column''')
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print('''Error: Please enter letter (A-J) for row and (0-9) for
            column''')
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick another spot!")
            continue
        if grid[row][col] == "." or grid[row][col] == "0":
            is_valid_placement = True

    return row, col

# Check if Ship Sunk


def check_for_ship_sunk(row, col):
    """
    Checks if all parts of the ship has been shot,if so then increment
    amount of ships sunk
    Return True or False
    """
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found,now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return false
    return True

# Method to shoot bullet


def shoot_bullet():
    """
    Updates the grid and ships based on where the bullet was shot
    Has no return but will use accept_valid_bullet_placement
    """
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("------------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "0":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A Ship was completely sunk!")
            num_of_ships_sunk += 1
        else:
            print("A ship was shot!")

    bullets_left -= 1

# Check if Game Over


def check_for_game_over():
    """
    Will check if all ships have sunk or have either ran out of missiles
    then its game over
    Has no Return
    """
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congratulations you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True

# Main Point of Entry


def main():
    """
    Main entry point of application that runs the game on a loop
    Has no Return but will use create_grid, print_grid, shoot_bullet and
    check_for_game_over
    """
    global game_over

    print("Welcome to Top Ship")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()

    while game_over is False:
        print_grid()
        print('''Number of ships
        remaining: ''' + str(num_of_ships - num_of_ships_sunk))
        print("Number of bullets left: " + str(bullets_left))
        shoot_bullet()
        print("------------------------------")
        print("")
        check_for_game_over()

if __name__ == '__main__':
    """Will only be called when program is run from terminal
    or an IDE like PyCharms"""
    main()
