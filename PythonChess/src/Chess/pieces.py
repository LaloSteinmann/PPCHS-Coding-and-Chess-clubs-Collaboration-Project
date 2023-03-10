from abc import abstractmethod
from constants import *
import os

#The piece class from which all piece types will inherit from
#All pieces, upon instantiation, will take in a coordinate number,
#and a number that is either 1 or 0 representing whether they are
#part of the white or black pieces
class Piece():
    def __init__(self, name, color, value, row, col, img=None, img_rect=None):
        self.color = color
        self.name = name
        if color == 'white':
            value_sign = 1
        else:
            value_sign = -1
        self.value = value * value_sign
        self.img = img
        self.set_texture()
        self.img_rect = img_rect
        self.moves = []
        self.tile_num_of_moves = []
        self.moved = False
        self.row = row
        self.col = col
    
    #this method will be used to calculate the legal moves respectively for each type of piece.
    # def calculate_legal_moves(self):
    #     pass

    def set_texture(self):
        self.img = os.path.join(f'PieceImages/{self.color}_{self.name}80x80.png')

    def add_move(self, move, tile_num):
        self.moves.append(move)
        self.tile_num_of_moves.append(tile_num)

class Knight(Piece):
    
    def __init__(self, color: chr, row, col):
        super().__init__('knight', color, 3.0, row, col)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
    
    # method to calculate the legal moves for a knight
    

class Bishop(Piece):
    def __init__(self, color: chr, row, col):
        super().__init__('bishop', color, 3.0001, row, col)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1

class Rook(Piece):
    def __init__(self, color: chr, row, col):
        super().__init__('rook', color, 5.0, row, col)    
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1

class Queen(Piece):
    def __init__(self, color: chr, row, col):
        super().__init__('queen', color, 9.0, row, col)    
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1

class King(Piece):
    def __init__(self, color: chr, row, col):
        super().__init__('king', color, 9001.0, row, col)
        self.in_check = False
        self.in_stalemate = False
        self.in_checkmate = False
        self.tile_num = 0
        self.castle_tile_nums = [None, None]
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1

class Pawn(Piece):
    def __init__(self, color: chr, row, col):
        super().__init__('pawn', color, 1.0, row, col)
        self.jumped_two_tiles = False
        self.en_passant_right = False
        self.en_passant_left = False
        self.immediate_en_passant_right = True
        self.immediate_en_passant_left = True
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
