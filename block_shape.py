import pygame
from colors_block import Colors

class Block:
    def __init__ (self, id):
        self.id = id
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()


    def draw(self, screen):
        print("Hello")
        pass
