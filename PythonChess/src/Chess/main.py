import pygame as pg
import sys as system
from constants import *
from board import Board
from game import Game
from calculate_legal_moves import *
from check_system import *
from time import sleep

#The main class
#It will actually run the game
class Main:
    def __init__(self):
        #initializes the game
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Chess")
        self.board = Board()
        self.game = Game()
    
    #keeps the game running and updating it
    def gameLoop(self):
        board = self.board
        screen = self.screen
        mouse = self.board.mouse
        while True:
            if (not in_check_mate(board.tiles, board.piece_list, board.black_king)):
                board.display_board(screen)
                board.display_pieces(screen)

                if mouse.dragging:
                    board.show_moves(piece, screen)
                    mouse.update_blit(screen)

                for event in pg.event.get():

                    #click
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse.update_mouse(event.pos)
                        clicked_row = int(mouse.mouseY / TILE_SIZE)
                        clicked_column = int(mouse.mouseX / TILE_SIZE)

                        # print(clicked_column)
                        # print(clicked_row)

                        #check if the clicked square has a piece on it
                        if clicked_column < 8 and clicked_row < 8:
                            if board.tiles[clicked_row][clicked_column].is_tile_occupied():
                                piece = board.tiles[clicked_row][clicked_column].piece_on_tile
                                # calculate_legal_moves(board.tiles, piece, clicked_row, clicked_column)
                                board.show_moves(piece, screen)
                                mouse.save_initial_pos(event.pos)
                                mouse.drag_piece(piece)
                                mouse.save_piece_pos()

                    elif event.type == pg.MOUSEMOTION: #drag
                        if mouse.dragging:
                            mouse.update_mouse(event.pos)
                            board.display_board(screen)
                            board.display_pieces(screen)
                            board.show_moves(piece, screen)
                            mouse.update_blit(screen)
                    elif event.type == pg.MOUSEBUTTONUP: #drop
                        mouse.drop_piece()
                    elif event.type == pg.QUIT: #if the player exits the game, then close it
                        pg.quit()
                        system.exit()
                        
                calculate_legal_moves_loop(board.piece_list, board.tiles)
                pg.display.update()
            else:
                print("Checkmate!")
                pg.quit()
                system.exit()
        
if __name__ == "__main__":
    main = Main()
    main.gameLoop()