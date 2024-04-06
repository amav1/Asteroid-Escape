import pygame
import sys
import random
from block import IBlock, OBlock 
from colors_block import Colors  

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

def create_random_block():
    block_type = random.choice([IBlock, OBlock])
    return block_type()

current_block = create_random_block()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0)) 

    current_block.draw(screen)

    pygame.display.flip()
    clock.tick(30)
