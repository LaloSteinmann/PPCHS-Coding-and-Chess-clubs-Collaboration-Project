import pygame as pg
from calculate_legal_moves import *
from constants import *
from pieces import Piece
from pieces import Pawn

class Mouse():
    def __init__(self, tiles):
        self.piece: Piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.tiles = tiles
    
    #blit method
    def update_blit(self, screen):
        #self.piece.set_texture(size=128)
        #the piece image

        #load image
        img = pg.image.load(self.piece.img)
        #create image center
        img_center = (self.mouseX, self.mouseY)
        self.piece.img_rect = img.get_rect(center = img_center)
        #blit
        screen.blit(img, self.piece.img_rect)

    def update_mouse (self, pos):
        self.mouseX, self.mouseY = pos
    
    def save_initial_pos(self, pos):
        self.initial_row = int(pos[1] / TILE_SIZE)
        self.initial_col = int(pos[0] / TILE_SIZE)

    def drag_piece(self, piece):
        self.dragging = True
        self.piece = piece

    def drop_piece(self):
        self.dragging = False
        current_col = int(self.mouseX / TILE_SIZE)
        current_row = int(self.mouseY / TILE_SIZE)
        #if self.tiles[current_row][current_col] in self.piece.moves:
        # king_tile = get_king_tile(self.tiles, return_opposite_color(self.piece.color))
        # in_check = is_king_in_check(self.tiles, self.tiles[king_tile.row][king_tile.col].piece_on_tile, king_tile.row, king_tile.col)
        if self.piece != None and (current_row < 8 and current_row >= 0) and (current_col < 8 and current_col >= 0):
            tile_num = return_tile_num(self.tiles[current_row][current_col])
            if tile_num in self.piece.tile_num_of_moves:
                if isinstance(self.piece, Pawn):
                    if current_row == (self.initial_row + (2 * self.piece.dir)):
                        self.piece.jumped_two_tiles = True
                    elif (current_row == self.initial_row + self.piece.dir and current_col == self.initial_col + 1):
                        self.tiles[self.initial_row][self.initial_col + 1].piece_on_tile = None
                    elif (current_row == self.initial_row + self.piece.dir and current_col == self.initial_col - 1):
                        self.tiles[self.initial_row][self.initial_col - 1].piece_on_tile = None
                self.piece.moved = True 
                self.tiles[current_row][current_col] = Tile(current_row, current_col, self.piece)
                # if self.tiles[current_row][current_col].is_tile_occupied() and self.tiles[current_row][current_col].has_enemy_piece(self.piece.color):
                #     enemy_piece = self.tiles[current_row][current_col].get_piece()
                #     del enemy_piece
                self.tiles[self.initial_row][self.initial_col] = Tile(self.initial_row, self.initial_col)
                self.piece.moves.clear()
                self.piece.tile_num_of_moves.clear()
        self.piece = None