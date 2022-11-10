from constants import *

#This function will take in a coordinate variable, and return an int value that represents a coordinate
#on a chess board from 0-63
def return_tile_num (row: int, col: int):
    running_total: int = 0
    for i in range(ROWS):
        for k in range(COLUMNS):
            check_row = i
            check_col = k
            if check_row == row and check_col == col:
                return running_total
            running_total += 1
    return 0