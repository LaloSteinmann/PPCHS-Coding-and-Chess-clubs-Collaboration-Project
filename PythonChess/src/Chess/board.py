import pygame as pg
from tile import *
from constants import *
from pieces import *
from calculate_legal_moves import *
from check_system import *
from mouse import Mouse

class Board:
    def __init__(self, screen):
        self.tiles = [[None, None, None, None, None, None, None, None] for col in range(COLUMNS)]
        self.king = None
        self.black_king = None
        self.white_king = None
        self.piece_list = []
        self.set_up_empty_board()
        self.put_pieces()
        self.mouse = Mouse(self.tiles, self.piece_list, screen)
        self.current_king = self.white_king

    #method to display the board
    def display_board(self, screen):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = (160, 82, 45) #dark blue
                else:
                    color = (255, 211, 155) #light blue
                rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)

                pg.draw.rect(screen, color, rect)

    def display_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.tiles[row][col].is_tile_occupied():
                    piece = self.tiles[row][col].piece_on_tile
                    
                    #all pieces except the piece being dragged by the mouse
                    if piece is not self.mouse.piece:
                        img = pg.image.load(piece.img)
                        img_centering = col * TILE_SIZE + (TILE_SIZE / 2), row * TILE_SIZE + (TILE_SIZE / 2)
                        piece.img_rect = img.get_rect(center=img_centering)
                        screen.blit(img, piece.img_rect)

    #Sets up an empty board with empty tiles
    def set_up_empty_board(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.tiles[row][col] = Tile(row, col)

    def get_tile(self, row, col):
        return self.tiles[row, col]

    def show_moves(self, piece: Piece, screen):
        for tile_num in piece.tile_num_of_moves:
            highlight_row, highlight_col = return_row_and_col(tile_num)
            king = get_king(self.tiles, piece.color)
            in_check = king.in_check
            if (not in_check and not would_put_in_check(self.tiles, piece.color, piece, highlight_row, highlight_col)) or (in_check and would_remove_check(self.tiles, piece.color, piece, highlight_row, highlight_col)):
                if self.tiles[highlight_row][highlight_col].has_enemy_piece(piece.color):
                    img = pg.image.load('PieceImages/white_circle.png')
                else:
                    img = pg.image.load('PieceImages/gray_dot.png')
                img_centering = highlight_col * TILE_SIZE + (TILE_SIZE / 2), highlight_row * TILE_SIZE + (TILE_SIZE / 2)
                img_rect = img.get_rect(center=img_centering)
                screen.blit(img, img_rect)

    #sets the pieces on the tiles list
    def put_pieces(self):

        #The rows where the pieces will be put on
        black_pawn_row = 1
        black_pieces_row = 0
        white_pawn_row = 6
        white_pieces_row = 7

        #sets up the black pawns
        for col in range(COLUMNS):
            self.tiles[black_pawn_row][col] = Tile(black_pawn_row, col, Pawn('black', black_pawn_row, col))
            self.piece_list.append(self.tiles[black_pawn_row][col].piece_on_tile)

        #black knights
        self.tiles[black_pieces_row][1] = Tile(black_pieces_row, 1, Knight('black', black_pieces_row, 1))
        self.tiles[black_pieces_row][6] = Tile(black_pieces_row, 6, Knight('black', black_pieces_row, 6))
        self.piece_list.append(self.tiles[black_pieces_row][1].piece_on_tile)
        self.piece_list.append(self.tiles[black_pieces_row][6].piece_on_tile)

        #black bishops
        self.tiles[black_pieces_row][2] = Tile(black_pieces_row, 2, Bishop('black', black_pieces_row, 2))
        self.tiles[black_pieces_row][5] = Tile(black_pieces_row, 5, Bishop('black', black_pieces_row, 5))
        self.piece_list.append(self.tiles[black_pieces_row][2].piece_on_tile)
        self.piece_list.append(self.tiles[black_pieces_row][5].piece_on_tile)

        #black rooks
        self.tiles[black_pieces_row][0] = Tile(black_pieces_row, 0, Rook('black', black_pieces_row, 0))
        self.tiles[black_pieces_row][7] = Tile(black_pieces_row, 7, Rook('black', black_pieces_row, 7))
        self.piece_list.append(self.tiles[black_pieces_row][0].piece_on_tile)
        self.piece_list.append(self.tiles[black_pieces_row][7].piece_on_tile)

        #black queen
        self.tiles[black_pieces_row][4] = Tile(black_pieces_row, 4, Queen('black', black_pieces_row, 4))
        self.piece_list.append(self.tiles[black_pieces_row][4].piece_on_tile)

        #black king
        self.tiles[black_pieces_row][3] = Tile(black_pieces_row, 3, King('black', black_pieces_row, 3))
        self.black_king = self.tiles[black_pieces_row][3].piece_on_tile
        self.piece_list.append(self.tiles[black_pieces_row][3].piece_on_tile)

        #sets up the white pawns
        for col in range(COLUMNS):
            self.tiles[white_pawn_row][col] = Tile(white_pawn_row, col, Pawn('white', white_pawn_row, col))
            self.piece_list.append(self.tiles[white_pawn_row][col].piece_on_tile)

        #white knights
        self.tiles[white_pieces_row][1] = Tile(white_pieces_row, 1, Knight('white', white_pieces_row, 1))
        self.tiles[white_pieces_row][6] = Tile(white_pieces_row, 6, Knight('white', white_pieces_row, 6))
        self.piece_list.append(self.tiles[white_pieces_row][1].piece_on_tile)
        self.piece_list.append(self.tiles[white_pieces_row][6].piece_on_tile)

        #white bishops
        self.tiles[white_pieces_row][2] = Tile(white_pieces_row, 2, Bishop('white', white_pieces_row, 2))
        self.tiles[white_pieces_row][5] = Tile(white_pieces_row, 5, Bishop('white', white_pieces_row, 5))
        self.piece_list.append(self.tiles[white_pieces_row][2].piece_on_tile)
        self.piece_list.append(self.tiles[white_pieces_row][5].piece_on_tile)

        #white rooks
        self.tiles[white_pieces_row][0] = Tile(white_pieces_row, 0, Rook('white', white_pieces_row, 0))
        self.tiles[white_pieces_row][7] = Tile(white_pieces_row, 7, Rook('white', white_pieces_row, 7))
        self.piece_list.append(self.tiles[white_pieces_row][0].piece_on_tile)
        self.piece_list.append(self.tiles[white_pieces_row][7].piece_on_tile)

        #white queen
        self.tiles[white_pieces_row][4] = Tile(white_pieces_row, 4, Queen('white', white_pieces_row, 4))
        self.piece_list.append(self.tiles[white_pieces_row][4].piece_on_tile)

        #white king
        self.tiles[white_pieces_row][3] = Tile(white_pieces_row, 3, King('white', white_pieces_row, 4))
        self.white_king = self.tiles[white_pieces_row][3].piece_on_tile
        self.piece_list.append(self.tiles[white_pieces_row][3].piece_on_tile)
