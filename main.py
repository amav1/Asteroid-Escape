import random
import pygame
from block import Figure, Colors

# Initialize Pygame
pygame.init()

# Set up the display
pygame.display.set_caption('Space Game')
win_icon = pygame.image.load("./Assets/spaceship.png")
pygame.display.set_icon(win_icon)
screen = pygame.display.set_mode((900,550))

#Background image
bg = pygame.image.load("./Assets/bg.jpg")


# Create grid 
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

# Draw grid
ROWS, COLS = 12, 9
Square = 53
grid_width = COLS * Square
grid_height = ROWS * Square

# background_color = (0, 0, 0)  
object_color = (255, 0, 0)        

# object_x = random.randint(grid_x, grid_x + grid_width - Square)  
# object_y = -Square  
object_speed = 5
is_paused = False

# creating the player object
player_image = pygame.image.load("./Assets/spaceship.png")
player_x = 410
player_y = 480
change_in_x_pos = 0
change_in_y_pos = 0

def player(player_x, player_y):
    screen.blit(player_image, (player_x, player_y))

# Game clock
start_time = pygame.time.get_ticks()  
font = pygame.font.SysFont('cambria', 30)

# Main game loop
global grid
locked_positions = {}
grid = create_grid(locked_positions)

running = True 
figure = None  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Logic for a controllable spaceship sprite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_in_x_pos = -3
            elif event.key == pygame.K_RIGHT:
                change_in_x_pos = 3
            elif event.key == pygame.K_UP:
                change_in_y_pos = -3
            elif event.key == pygame.K_DOWN:
                change_in_y_pos = 3
# Check for keystroke release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_in_x_pos = 0
        

    screen.fill((0, 0, 0 ))

    if player_x <= 0:
        player_x = 0
    elif player_x >= 900:
        player_x = 900

    if player_y <= 0:
        player_y = 0
    elif player_y >= 500:
        player_y = 500

    player_x += change_in_x_pos
    player_y += change_in_y_pos

    # timer_text = font.render("Time: " + str(elapsed_seconds), True, (255, 255, 255))
    # screen.blit(timer_text, (10, 10))
    screen.blit(bg, (0,0))
    player(player_x, player_y)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()