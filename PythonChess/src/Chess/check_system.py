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
    king.tile_num = get_king_tile_num(tiles, king.color)
    for row in range(ROWS):
        for col in range(COLUMNS):
            if tiles[row][col].piece_on_tile != None and tiles[row][col].piece_on_tile.color != king.color:
                tiles[row][col].piece_on_tile.tile_num_of_moves.clear()
                tiles[row][col].piece_on_tile.moves.clear()
                calculate_legal_moves(tiles, tiles[row][col].piece_on_tile, row, col)
                if king.tile_num in tiles[row][col].piece_on_tile.tile_num_of_moves:
                    king.in_check = True
    return king.in_check

def in_check_mate(tiles, piece_list, king):
    if is_king_in_check(tiles, king):
        for piece in piece_list:
            if piece.color == king.color:
                for move_tile in piece.tile_num_of_moves:
                    move_row, move_col = return_row_and_col(move_tile)
                    if would_remove_check(tiles, king.color, piece, move_row, move_col):
                        king.in_checkmate = False
                        return king.in_checkmate
                        # return king.in_checkmate
                    else:
                        king.in_checkmate = True
        return king.in_checkmate

def in_stale_mate(tiles, piece_list, king: King):
    if not king.in_check:
        for piece in piece_list:
            if piece.color == king.color:
                for move_tile in piece.tile_num_of_moves:
                    move_row, move_col = return_row_and_col(move_tile)
                    if would_put_in_check(tiles, king.color, piece, move_row, move_col):
                        king.in_stalemate = True
                        # return king.in_checkmate
                    else:
                        king.in_stalemate = False
                        return king.in_stalemate
        return king.in_stalemate

def would_put_in_check(tiles, color, piece, move_row, move_col):
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
        return True
    else:
        temp_board[move_row][move_col].piece_on_tile = None
        return False

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
        return False
    else:
        return True

def return_opposite_color(color):
    if color == 'white':
        return 'black'
    else:
        return 'white'