import pygame as pg
from calculate_legal_moves import *
from check_system import *
from constants import *
from pieces import Piece
from pieces import Pawn

class Mouse():
    def __init__(self, tiles, piece_list, screen):
        self.piece: Piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.tiles = tiles
        self.piece_list = piece_list
        self.screen = screen

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

    def save_piece_pos(self):
        self.piece.initial_row = self.initial_row
        self.piece.initial_col = self.initial_col

    def drag_piece(self, piece):
        self.dragging = True
        self.piece = piece
        # if isinstance(self.piece, Pawn) and self.piece.en_passant and self.piece.immediate_en_passant:
        #     #If en passant is not done during the turn in which it becomes available, it cannot be done afterwards
        #     self.piece.immediate_en_passant = False

    def move(self, current_player, rook_pairs):
        self.current_col = int(self.mouseX / TILE_SIZE)
        self.current_row = int(self.mouseY / TILE_SIZE)
        current_col = self.current_col
        current_row = self.current_row
        #if self.tiles[current_row][current_col] in self.piece.moves:
        # king_tile = get_king_tile(self.tiles, return_opposite_color(self.piece.color))
        # in_check = is_king_in_check(self.tiles, self.tiles[king_tile.row][king_tile.col].piece_on_tile)

                            # king = get_king(tiles, queen.color)
                            # if (not is_king_in_check(tiles, king)) or (is_king_in_check(tiles, king)
                            # and would_remove_check(tiles, queen.color, queen, possible_row, possible_col)):

        if self.piece != None and (current_row < 8 and current_row >= 0) and (current_col < 8 and current_col >= 0):
            king = get_king(self.tiles, self.piece.color)
            in_check = king.in_check
            tile_num = return_tile_num(self.tiles[current_row][current_col])
            if tile_num in self.piece.tile_num_of_moves:
                if (not in_check and not would_put_in_check(self.tiles, self.piece.color, self.piece, current_row, current_col)) or (in_check and would_remove_check(self.tiles, self.piece.color, self.piece, current_row, current_col)):
                    if (current_player == self.piece.color):

                        #checks if the piece is a pawn in order to later address special moves if needed
                        if isinstance(self.piece, Pawn):

                            #checks for the initial pawn jump
                            if current_row == (self.initial_row + (2 * self.piece.dir)):
                                self.piece.jumped_two_tiles = True

                            #checks for en passant on the right side
                            elif (current_row == self.initial_row + self.piece.dir and current_col == self.initial_col + 1) and self.piece.en_passant_right:
                                if self.piece.immediate_en_passant_right:
                                    if self.tiles[self.initial_row][self.initial_col + 1].has_enemy_piece(self.piece.color):
                                        self.piece_list.remove(self.tiles[self.initial_row][self.initial_col + 1].piece_on_tile )
                                        self.tiles[self.initial_row][self.initial_col + 1].piece_on_tile = None
                                        self.piece.en_passant = False
                                else:
                                    return False
                            
                            #checks for en passant on the left side
                            if (current_row == self.initial_row + self.piece.dir and current_col == self.initial_col - 1) and self.piece.en_passant_left:
                                if self.piece.immediate_en_passant_left:
                                    if self.tiles[self.initial_row][self.initial_col - 1].has_enemy_piece(self.piece.color):
                                        self.piece_list.remove(self.tiles[self.initial_row][self.initial_col - 1].piece_on_tile)
                                        self.tiles[self.initial_row][self.initial_col - 1].piece_on_tile = None
                                        self.piece.en_passant = False
                                else:
                                    return False

                        elif isinstance(self.piece, King):
                            if tile_num in self.piece.castle_tile_nums:
                                if self.piece.color == WHITE:
                                        rook_row = 0
                                else:
                                        rook_row = 1
                                if tile_num == self.piece.castle_tile_nums[0]:
                                    self.tiles[current_row][current_col + 1].piece_on_tile = rook_pairs[rook_row][0]
                                    self.tiles[self.initial_row][0].piece_on_tile = None
                                    rook_pairs[rook_row][0].row = current_row
                                    rook_pairs[rook_row][0].col = current_col + 1
                                    rook_pairs[rook_row][0].moved = True
                                else:
                                    self.tiles[current_row][current_col - 1].piece_on_tile = rook_pairs[rook_row][1]
                                    self.tiles[self.initial_row][7].piece_on_tile = None
                                    rook_pairs[rook_row][1].row = current_row
                                    rook_pairs[rook_row][1].col = current_col - 1
                                    rook_pairs[rook_row][1].moved = True

                        self.piece.moved = True 
                        self.piece.row = current_row
                        self.piece.col = current_col
                        if self.tiles[current_row][current_col].piece_on_tile != None and self.tiles[current_row][current_col].piece_on_tile.color != self.piece.color:
                            self.piece_list.remove(self.tiles[current_row][current_col].piece_on_tile)
                        self.tiles[current_row][current_col].piece_on_tile = self.piece
                        # if self.tiles[current_row][current_col].is_tile_occupied() and self.tiles[current_row][current_col].has_enemy_piece(self.piece.color):
                        #     enemy_piece = self.tiles[current_row][current_col].get_piece()
                        #     del enemy_piece
                        self.tiles[self.initial_row][self.initial_col].piece_on_tile = None
                        self.piece.moves.clear()
                        self.piece.tile_num_of_moves.clear()

                        #pawn promotion move
                        if (isinstance(self.piece, Pawn) and (self.piece.color == WHITE and self.piece.row == 0)) or (
                        isinstance(self.piece, Pawn) and (self.piece.color == BLACK and self.piece.row == 7)):
                            pawn_promotion(self.screen, self.piece, self.tiles, self.piece_list)

                        return True


    def drop_piece(self, current_player, turn, rook_pairs):
        self.dragging = False
        if self.move(current_player, rook_pairs):
            turn += 1
            immediate_en_passant_register(current_player, self.piece_list)
        self.piece = None
        return turn