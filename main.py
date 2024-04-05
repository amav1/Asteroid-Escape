import pygame
import sys
from block import IBlock

pygame.init()

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
block = IBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))  
    block.draw(screen)
    pygame.display.flip()  
