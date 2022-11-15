import pygame as pg
from tile import *
from constants import *
from pieces import *
from mouse import Mouse

class Board:
    def __init__(self):
        self.tiles = [[None, None, None, None, None, None, None, None] for col in range(COLUMNS)]
        self.set_up_empty_board()
        self.put_pieces()
        self.mouse = Mouse(self.tiles)

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
                        piece.img_rect = img.get_rect(center = img_centering)
                        screen.blit(img, piece.img_rect)

    def show_moves(self, screen):
        
        if self.mouse.dragging:
            piece = self.mouse.piece

            # for move in piece.moves:

            #     #color

    #Sets up an empty board with empty tiles
    def set_up_empty_board(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.tiles[row][col] = Tile(row, col)

    def get_tile(self, row, col):
        return self.tiles[row, col]

    #sets the pieces on the tiles list
    def put_pieces(self):

        #The rows where the pieces will be put on
        black_pawn_row = 1
        black_pieces_row = 0
        white_pawn_row = 6
        white_pieces_row = 7

        #sets up the black pawns
        for col in range(COLUMNS):
            self.tiles[black_pawn_row][col] = Tile(black_pawn_row, col, Pawn('black'))

        #black knights
        self.tiles[black_pieces_row][1] = Tile(black_pieces_row, 1, Knight('black'))
        self.tiles[black_pieces_row][6] = Tile(black_pieces_row, 6, Knight('black'))

        #black bishops
        self.tiles[black_pieces_row][2] = Tile(black_pieces_row, 2, Bishop('black'))
        self.tiles[black_pieces_row][5] = Tile(black_pieces_row, 5, Bishop('black'))

        #black rooks
        self.tiles[black_pieces_row][0] = Tile(black_pieces_row, 0, Rook('black'))
        self.tiles[black_pieces_row][7] = Tile(black_pieces_row, 7, Rook('black'))

        #black queen
        self.tiles[black_pieces_row][4] = Tile(black_pieces_row, 4, Queen('black'))

        #black king
        self.tiles[black_pieces_row][3] = Tile(black_pieces_row, 3, King('black'))

        #sets up the white pawns
        for col in range(COLUMNS):
            self.tiles[white_pawn_row][col] = Tile(white_pawn_row, col, Pawn('white'))

        #white knights
        self.tiles[white_pieces_row][1] = Tile(white_pieces_row, 1, Knight('white'))
        self.tiles[white_pieces_row][6] = Tile(white_pieces_row, 6, Knight('white'))

        #white bishops
        self.tiles[white_pieces_row][2] = Tile(white_pieces_row, 2, Bishop('white'))
        self.tiles[white_pieces_row][5] = Tile(white_pieces_row, 5, Bishop('white'))

        #white rooks
        self.tiles[white_pieces_row][0] = Tile(white_pieces_row, 0, Rook('white'))
        self.tiles[white_pieces_row][7] = Tile(white_pieces_row, 7, Rook('white'))

        #white queen
        self.tiles[white_pieces_row][4] = Tile(white_pieces_row, 4, Queen('white'))

        #white king
        self.tiles[white_pieces_row][3] = Tile(white_pieces_row, 3, King('white'))