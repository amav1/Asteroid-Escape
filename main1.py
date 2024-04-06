import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Free falling object')

# Define colors
background_color = (255, 255, 255)  # White
object_color = (255, 0, 0)          # Red


object_size = 50
object_x = screen_width // 2
object_y = 0
object_speed = 5


# Game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                object_x -= object_size
            elif event.key == pygame.K_RIGHT:
                object_x += object_size

    object_y += object_speed
    if object_y > screen_height:
        object_x = screen_width //2 
        object_y = 0

    # Boundary checking
    if object_x <= 0:
        object_x = 0
    if object_x >= screen_width - object_size:
        object_x = screen_width - object_size

    # Drawing
    screen.fill(background_color)
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_size, object_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

