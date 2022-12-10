import pygame as pg
import os

class Button:
    def __init__(self, image, pos, text_input, font, base_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_input(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

class Promotion_Button(Button):
    def __init__(self, pos, color, name, tile_rect):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.image = pg.image.load(os.path.join(f'PieceImages/{color}_{name}80x80.png'))
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.tile_rect = tile_rect
        # (self.x_pos, self.y_pos, TILE_SIZE, TILE_SIZE)

    def update(self, screen):
        pg.draw.rect(screen, 'white', self.tile_rect)
        screen.blit(self.image, self.rect)
    
    def check_input(self, position):
        return super().check_input(position)