import pygame
import random
import math

pygame.init()

sw = 800
sh = 800

pygame.display.set_caption('Space Game')
win_icon = pygame.image.load("./Assets/spaceship.png")
pygame.display.set_icon(win_icon)
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

player_image = pygame.image.load("./Assets/spaceship.png")
player_x = 350
player_y = 480
change_in_x_pos = 0
change_in_y_pos = 0

asteroids = []

def player(player_x, player_y):
    win.blit(player_image, (player_x, player_y))

def bg_image():
    bg = pygame.transform.scale(pygame.image.load("./Assets/bg.jpg").convert_alpha(), (sw, sh))
    win.blit(bg, (0, 0))

def Asteroid(x, y):
    asteroid_image = pygame.transform.scale(pygame.image.load('./Assets/asteroids.png').convert_alpha(), (120, 120))
    win.blit(asteroid_image, (x, y))

def update_asteroids():
    for asteroid in asteroids:
        asteroid['rect'].y += asteroid['speed']
        if asteroid['rect'].y > sh:
            asteroid['rect'].y = -120
            asteroid['rect'].x = random.randint(0, sw)

def is_collided_with(x, y, player_x, player_y):
    distance = math.sqrt((x - player_x) ** 2 + (y - player_y) ** 2)
    return distance < 30

def create_asteroid():
    if random.randint(0, 400) < 10:
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            x = random.randint(0, sw)
            y = -120
        elif side == 'bottom':
            x = random.randint(0, sw)
            y = sh + 120
        elif side == 'left':
            x = -120
            y = random.randint(0, sh)
        else:
            x = sw + 120
            y = random.randint(0, sh)
        asteroids.append({'rect': pygame.Rect(x, y, 120, 120), 'speed': random.randint(1, 3)})

def pause_game():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
        pause_text = font.render("Paused", True, (255, 255, 255))
        win.blit(pause_text, (sw // 2 - 50, sh // 2))
        pygame.display.update()

def lost_game(): 
    lost = True
    while lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        lost_text = font.render("You Lost!", True, (255, 255, 255))
        win.blit(lost_text, (sw // 2 -50, sh //2))
        pygame.display.update()

start_ticks = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 36)

run = True
paused = False
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_in_x_pos = -6
            elif event.key == pygame.K_RIGHT:
                change_in_x_pos = 6
            elif event.key == pygame.K_UP:
                change_in_y_pos = -6
            elif event.key == pygame.K_DOWN:
                change_in_y_pos = 6
            elif event.key == pygame.K_SPACE:
                paused = True
                pause_game()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_in_x_pos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_in_y_pos = 0

    player_x += change_in_x_pos
    player_y += change_in_y_pos

    if player_x < 0:
        player_x = 0
    elif player_x > sw:
        player_x = sw

    if player_y < 0:
        player_y = 0
    elif player_y > sh:
        player_y = sh

    bg_image()
    player(player_x, player_y)
        

    # Collision detection
    for asteroid in asteroids:
        Asteroid(asteroid['rect'].x, asteroid['rect'].y)
        if asteroid['rect'].colliderect(pygame.Rect(player_x, player_y, 30, 30)): # fix hitbox
            # Handle collision here, for example:
            # End game or deduct player health
            lost_game()

    update_asteroids()
    create_asteroid()

    # Timer
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_seconds = max(0, 120 - elapsed_seconds)
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    timer_text = f"Time: {minutes:02}:{seconds:02}"
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    win.blit(timer_surface, (330, 10))

    if remaining_seconds == 0:
        win.fill((0,0,0))
        pygame.display.flip()
        win_statement = "You won!"
        win_surface = font.render(win_statement, True, (255, 255, 255))
        win.blit(win_surface, (330, 400))
        pygame.display.flip()
        run = False

    pygame.display.update()

pygame.quit()
