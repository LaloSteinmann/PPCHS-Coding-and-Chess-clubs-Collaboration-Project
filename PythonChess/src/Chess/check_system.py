from pieces import *
from move import Move
from tile import *
from constants import *
import copy
from calculate_legal_moves import *

def get_king_tile(tiles, color):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if isinstance(tiles[row][col].piece_on_tile, King) and tiles[row][col].piece_on_tile.color == color:
                return Tile(row, col)

def get_king_tile_num(tiles, color):
    running_total = 0
    for row in range(ROWS):
        for col in range(COLUMNS):
            if isinstance(tiles[row][col].piece_on_tile, King) and tiles[row][col].piece_on_tile.color == color:
                return running_total
            running_total += 1

def get_king(tiles, color):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if tiles[row][col].piece_on_tile != None:
                if isinstance(tiles[row][col].piece_on_tile, King) and tiles[row][col].piece_on_tile.color == color:
                    king = tiles[row][col].piece_on_tile
                    return king

def is_king_in_check(tiles, king: King):
    king.in_check = False
    tile_num_of_king = get_king_tile_num(tiles, king.color)
    for row in range(ROWS):
        for col in range(COLUMNS):
            if tiles[row][col].piece_on_tile != None and tiles[row][col].piece_on_tile.color != king.color:
                tiles[row][col].piece_on_tile.tile_num_of_moves.clear()
                tiles[row][col].piece_on_tile.moves.clear()
                calculate_legal_moves(tiles, tiles[row][col].piece_on_tile, row, col)
                if tile_num_of_king in tiles[row][col].piece_on_tile.tile_num_of_moves:
                    king.in_check = True
    return king.in_check

def would_remove_check(tiles, color, piece, move_row, move_col):
    temp_board = copy.deepcopy(tiles)
    # temp_board = tiles.copy()
    temp_board[move_row][move_col].piece_on_tile = piece
    temp_board[piece.row][piece.col].piece_on_tile = None
    king = get_king(tiles, color)
    temp_king = copy.deepcopy(king)
    # for row in range(ROWS):
    #     for col in range(COLUMNS):
    #         if temp_board[row][col].piece_on_tile != None and temp_board[row][col].piece_on_tile.color != king.color:
    #             temp_board[row][col].piece_on_tile.tile_num_of_moves.clear()
    #             calculate_legal_moves(temp_board, temp_board[row][col].piece_on_tile, row, col)
    # king = get_king(tiles, color)
    in_check = is_king_in_check(temp_board, temp_king)
    if in_check:
        temp_board[move_row][move_col].piece_on_tile = None
        return False
    else:
        temp_board[move_row][move_col].piece_on_tile = None
        return True

def return_opposite_color(color):
    if color == 'white':
        return 'black'
    else:
        return 'white'