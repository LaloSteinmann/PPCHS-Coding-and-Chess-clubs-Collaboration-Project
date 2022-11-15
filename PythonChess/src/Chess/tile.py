from pieces import *

class Tile():

    #constructor for the tile
    def __init__(self, row: int, col: int, piece_on_tile: Piece = None):
        self.row = row
        self.col = col
        self.piece_on_tile = piece_on_tile

    #returns the piece if there is one on the tile
    def get_piece(self):
        if(self.piece_on_tile != None):
            return self.piece_on_tile

    #returns true if there is a piece on the board, otherwise, returns false
    def is_tile_occupied(self):
        return self.piece_on_tile != None

    def has_enemy_piece(self, color):
        return self.piece_on_tile.color != color

def is_valid_coordinate(row, col):
    return (row < 8 and row >= 0) and (col < 8 and col >= 0)

def get_tile(tiles, row, col):
    return tiles[row][col]