from CoordinateFile import Coordinate
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, pos: Coordinate, color_num: int):
        self.pos = pos
        self.colorNum = color_num
        if color_num == 0:
            color: chr = 'w'
        else:
            color: chr = 'b'
    
    @abstractmethod
    def calculate_legal_moves(self):
        pass

class Knight(Piece):
    def __init__(self, pos: Coordinate, color_num: int):
        super().__init__(pos, color_num)
    
    def calculate_legal_moves(self):
        legal_moves = []

class Bishop(Piece):
    def __init__(self, pos: Coordinate, color_num: int):
        super().__init__(pos, color_num)
    
    def calculate_legal_moves(self):
        legal_moves = []

class Rook(Piece):
    def __init__(self, pos: Coordinate, color_num: int):
        super().__init__(pos, color_num)
    
    def calculate_legal_moves(self):
        legal_moves = []

class Queen(Piece):
    def __init__(self, pos: Coordinate, color_num: int):
        super().__init__(pos, color_num)
    
    def calculate_legal_moves(self):
        legal_moves = []

class King(Piece):
    def __init__(self, pos: Coordinate, color_num: int):
        super().__init__(pos, color_num)
    
    def calculate_legal_moves(self):
        legal_moves = []

class Pawn(Piece):
    def __init__(self, pos: Coordinate, color_num: int):
        super().__init__(pos, color_num)
    
    def calculate_legal_moves(self):
        legal_moves = []
