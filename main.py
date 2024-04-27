import random
import pygame
from block import Figure, Colors

# Initialize Pygame
pygame.init()

# Set up the display
pygame.display.set_caption('Space Game')
win_icon = pygame.image.load("./Assets/spaceship.png")
pygame.display.set_icon(win_icon)
screen = pygame.display.set_mode((900,600))

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
# grid_x = (screen_width - grid_width) // 2
# grid_y = (screen_height - grid_height) // 2 

# def draw_grid(locked_positions={}):
#     for x in range(0, COLS):
#         for y in range(0, ROWS):
#             grid = pygame.Rect(grid_x + x * Square, grid_y + y * Square, Square, Square)
#             pygame.draw.rect(screen, (128, 128, 128), grid, 1)
#             if (y,x) in locked_positions:
#                 print("hello")
#                 color = locked_positions[
#                     (x,y)]
#                 grid[y][x] = color

            


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

def player():
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
                pass
            elif event.key == pygame.K_RIGHT:
                pass

    
    # Calculate falling speed
    # elapsed_time = pygame.time.get_ticks() - start_time
    # elapsed_seconds = elapsed_time / 1000  
    # if elapsed_seconds % 50 == 0 and elapsed_seconds != 0:
    #     object_speed += 1  

    # if figure is None or object_y >= screen_height - Square:  
    #     object_x = random.randint(grid_x, grid_x + grid_width - Square)
    #     object_y = -Square  
    #     figure = Figure(object_x, grid_y)  
    # else:
    #     object_y += object_speed  

    # Boundary checking
    # if object_x < grid_x:
    #     object_x = grid_x
    # elif object_x > grid_x + grid_width - Square:
    #     object_x = grid_x + grid_width - Square
    # # checking screen boundaries to lock objects:
    # if object_y == grid_y:
    #     object_y = grid_y
    # if object_y > grid_y + grid_height - Square:
    #     object_y = grid_y + grid_height - Square
    # # This generates the next object when the object hits the bottom of the y-axis
    #     object_x = random.randint(grid_x, grid_x + grid_width - Square)
    #     object_y = -Square  
    #     figure = Figure(object_x, grid_y)


    # Drawing
    # draw_grid()
    # for i in range(4):
    #     for j in range(4):
    #         p = i * 4 + j
    #         if p in figure.image():
    #             pygame.draw.rect(screen, figure.color,
    #                              [object_x + Square * j + 1,
    #                               object_y + Square * i + 1,
    #                               Square - 2, Square - 2])

    # timer_text = font.render("Time: " + str(elapsed_seconds), True, (255, 255, 255))
    # screen.blit(timer_text, (10, 10))
    screen.blit(bg, (0,0))
    player()

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()