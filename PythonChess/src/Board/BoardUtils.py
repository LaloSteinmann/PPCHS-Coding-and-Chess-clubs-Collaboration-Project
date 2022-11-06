import sys
from Pieces import Position as Pos

num_of_rows = 8

num_of_columns = 8

def return_tile_num (pos):
    running_total = 0
    for i in range(8):
        for k in range(8):
            check_position = Pos.Position(i, k)
            if check_position.get_x_pos == pos.get_x_pos and check_position.get_y_pos == pos.get_y_pos:
                return running_total
            running_total += 1
    return 0