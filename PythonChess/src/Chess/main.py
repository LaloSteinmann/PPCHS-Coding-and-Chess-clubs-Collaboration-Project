import pygame as pg
import sys as system
from constants import *
from board import Board

#The main class
#It will actually run the game
class Main:
    def __init__(self):
        #initializes the game
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Chess")
        self.board = Board()
    
    #keeps the game running and updating it
    def gameLoop(self):
        board = self.board
        screen = self.screen
        while True:
            board.display_board(screen)
            board.display_pieces(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    system.exit()

            pg.display.update()

if __name__ == "__main__":
    main = Main()
    main.gameLoop()