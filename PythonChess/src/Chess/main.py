import pygame as pg
import sys as system
from constants import *
from board import Board
from calculate_legal_moves import *
from check_system import *
from button import Button

#The main class
#It will actually run the game
class Main:
    def __init__(self):
        #initializes the game
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Chess")
        self.board = Board(self.screen)
    
    def get_font(self, size):
        return pg.font.Font('PieceImages/Speedy.ttf', size)

    def game_menu(self):
        screen = self.screen
        background = pg.image.load("PieceImages/menuImage.png")
        while True:
            screen.blit(background, (0, 0))

            menu_pos = pg.mouse.get_pos()
            menu_text = self.get_font(100).render('Chess', True, '#b68f40')
            menu_rect = menu_text.get_rect(center=(500, 200))

            play_button = Button(pg.image.load('PieceImages/button_image.png'), (500, 400), 'PvP', self.get_font(75), 'aliceblue')
            
            screen.blit(menu_text, menu_rect)

            for button in [play_button]:
                button.update(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    system.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if play_button.check_input(menu_pos):
                        self.pvp_game_loop()

            pg.display.update()

    #keeps the game running and updating it
    def pvp_game_loop(self):
        board = self.board
        screen = self.screen
        mouse = self.board.mouse
        screen.fill('black')
        turn: int = 1
        current_player = WHITE
        while True:
            if (not in_check_mate(board.tiles, board.piece_list, board.current_king)):
                if turn % 2 == 0:
                    current_player = BLACK
                    board.current_king = board.black_king
                else:
                    current_player = WHITE
                    board.current_king = board.white_king

                board.display_board(screen)
                board.display_pieces(screen)

                if mouse.dragging:
                    if current_player == piece.color:
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
                                if current_player == piece.color:
                                    board.show_moves(piece, screen)
                                mouse.save_initial_pos(event.pos)
                                mouse.drag_piece(piece)
                                mouse.save_piece_pos()

                    elif event.type == pg.MOUSEMOTION: #drag
                        if mouse.dragging:
                            mouse.update_mouse(event.pos)
                            board.display_board(screen)
                            board.display_pieces(screen)
                            if current_player == piece.color:
                                board.show_moves(piece, screen)
                            mouse.update_blit(screen)
                    elif event.type == pg.MOUSEBUTTONUP: #drop
                        turn = mouse.drop_piece(current_player, turn)
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
    main.game_menu()