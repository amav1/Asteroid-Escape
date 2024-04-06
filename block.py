import pygame
from colors_block import Colors
import random



class Block:
    Shapes = {
        'I' : [[1, 5, 9, 13], [4, 5, 6, 7]],
        'O' : [[4, 5, 9, 10], [2, 6, 5, 9]],
        'L' : [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J' : [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]
}   

    Types = ['I', 'O', 'L', 'J']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(Block.Types)
        self.shape = self.Shapes[self.type]
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation]
    
    

