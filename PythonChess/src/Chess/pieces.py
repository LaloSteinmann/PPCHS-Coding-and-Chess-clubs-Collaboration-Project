from abc import abstractmethod
import os

#The piece class from which all piece types will inherit from
#All pieces, upon instantiation, will take in a coordinate number,
#and a number that is either 1 or 0 representing whether they are
#part of the white or black pieces
class Piece():
    def __init__(self, name, color, value, img=None, img_rect=None):
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
    
    #this method will be used to calculate the legal moves respectively for each type of piece.
    def calculate_legal_moves(self):
        pass

    def set_texture(self):
        self.img = os.path.join(f'PieceImages/{self.color}_{self.name}80x80.png')

class Knight(Piece):
    
    def __init__(self, color: chr):
        super().__init__('knight', color, 3.0)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
    
    def calculate_legal_moves(self):
        legal_moves = []

class Bishop(Piece):
    def __init__(self, color: chr):
        super().__init__('bishop', color, 3.0001)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
    
    def calculate_legal_moves(self):
        legal_moves = []

class Rook(Piece):
    def __init__(self, color: chr):
        super().__init__('rook', color, 5.0)    
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
    
    def calculate_legal_moves(self):
        legal_moves = []

class Queen(Piece):
    def __init__(self, color: chr):
        super().__init__('queen', color, 9.0)    
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1

    def calculate_legal_moves(self):
        legal_moves = []

class King(Piece):
    def __init__(self, color: chr):
        super().__init__('king', color, 9001.0)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
         
    def calculate_legal_moves(self):
        legal_moves = []

class Pawn(Piece):
    def __init__(self, color: chr):
        super().__init__('pawn', color, 1.0)
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
    
    def calculate_legal_moves(self):
        legal_moves = []
