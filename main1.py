import pygame
import sys
import random
from block import IBlock, OBlock, Block
from colors_block import Colors  



Block()
Colors()


s_width = 800
s_height = 700
play_width = 300  
play_height = 600  
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 


# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catching Falling Objects')

#Shape types
shapes = [IBlock, OBlock]

#Create grid 
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

#Draw grid
def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))

#Random shape
def get_shape():
    return random.choice(shapes)
    return random.choice(Colors)

# Define colors
background_color = (255, 255, 255)  # White
object_color = (255, 0, 0)          # Red



# Define the falling object and player properties
object_size = 50
object_x = screen_width // 2
object_y = 0
object_speed = 5
is_paused = False



# Game clock

start_time = pygame.time.get_ticks()  
font = pygame.font.SysFont('cambria', 30)



# Main game loop
global grid
locked_positions = {}  
grid = create_grid(locked_positions)
change_piece = False
running = True
current_piece = get_shape()
next_piece = get_shape()
while running:
    fall_speed = 0.27
    grid = create_grid(locked_positions)
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
        object_x = random.randint(0, screen_width - object_size)
        object_y = 0

    # Boundary checking
    if object_x <= 0:
        object_x = 0
    if object_x >= screen_width - object_size:
        object_x = screen_width - object_size

    # Drawing
    screen.fill(background_color)
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_size, object_size))

    elapsed_time = pygame.time.get_ticks() - start_time

    elapsed_seconds = elapsed_time // 1000

    
    timer_text = font.render("Time: " + str(elapsed_seconds), True, (0, 0, 0))
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(30)
pygame.quit()

