# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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

    pass

# Based on directions will try place ship on grid
def try_to_place_ship_on_grid(row, col, direction, length):
    global grid_size

    pass

    return validate_grid_and_place_ship(0, 0, 0, 0)

# Creating the Grid
def create_grid():
    """
    Will create a grid based on user input and randomly place
    down ships of different sizes and in different directions.
    Has no Return but will use try_to_place_ship_on_grid
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    pass

    try_to_place_ship_on_grid(0, 0, 0, 0)

def print_grid():
    """
    This method will print the grid while rows using the alphabet
    and the columns using integers
    """
    global grid
    global alphabet

def accept_valid_bullet_placement():
    """
    Will validate row and column that has been placed by user on board
    Has Return and row, col are both integers
    """
    global alphabet
    global grid

    pass

    return 0, 0

def check_for_ship_sunk(row, col):
    """Checks if all parts of the ship has been shot, if so then increment 
       amount of ships sunk
       Return True or False"""
    global ship_positions
    global grid

    pass

def shoot_bullet():
    """
    Updates the grid and ships based on where the bullet was shot
    Has no return but will use accept_valid_bullet_placement
    """
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()

    pass

def check_for_game_over():
    """
    Will check if all ships have sunk or have either ran out of missiles then its game over
    Has no Return
    """
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    pass