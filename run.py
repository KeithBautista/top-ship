# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
---GLOBAL VARIABLES--
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
-- METHODS --
"""

# Validation for placing ship on grid
def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row and or column to validate the placement of ship
        on the grid"""
    global grid
    global ship_positions

    pass