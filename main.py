import pygame
import random
import math

pygame.init()

sw = 800
sh = 800

pygame.display.set_caption('Asteroidz')
win_icon = pygame.image.load("./Assets/spaceship.png")
pygame.display.set_icon(win_icon)
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

player_image = pygame.image.load("./Assets/spaceship.png")
player_x = 350
player_y = 480
change_in_x_pos = 0
change_in_y_pos = 0
default_player_size = (60,60)
boom_img = pygame.image.load("./Assets/boom.png").convert_alpha()

asteroids = []
flowers = []

def player(player_x, player_y):
    win.blit(player_image, (player_x, player_y))


star_image = pygame.transform.scale(pygame.image.load('./Assets/starbit.png').convert_alpha(), (40, 40))
flower_image = pygame.transform.scale(pygame.image.load('./Assets/satelitte.png').convert_alpha(), (40, 40))

# power ups
power_ups = []
spawn_timer = 0
power_up_active = False
power_up_timer = 0
power_up_duration = 15  
star_power_up_start_time = 0

def spawn_power_up():
    x = random.randint(0, sw - 40)
    y = random.randint(0, sh - 40)
    power_up_type = random.choice(['star', 'flower'])
    if power_up_type == 'star':
        power_ups.append({'image': star_image, 'rect': pygame.Rect(x, y, 40, 40)})
    elif power_up_type == 'flower':
        power_ups.append({'image': flower_image, 'rect': pygame.Rect(x, y, 40, 40)})



def handle_collisions():
    global power_up_active, power_up_timer, star_power_up_start_time
    for power_up in power_ups:
        if not power_up_active:
            if power_up['rect'].colliderect(pygame.Rect(player_x, player_y, 60, 60)):
                if power_up['image'] == star_image:
                    power_up_active = True
                    power_up_timer = pygame.time.get_ticks() // 1000
                    star_power_up_start_time = power_up_timer  
                    power_up['collected_time'] = power_up_timer
        else:
            if power_up['rect'].colliderect(pygame.Rect(player_x, player_y, 60, 60)):
                if power_up['image'] == star_image:
                    power_ups.remove(power_up)


def update_power_ups():
    global power_up_active, power_up_timer, star_power_up_start_time
    if power_up_active:
        current_time = pygame.time.get_ticks() // 1000
        elapsed_time = current_time - power_up_timer
        if elapsed_time >= power_up_duration:
            power_up_active = False
            power_up_timer = 0
            star_power_up_start_time = 0  #reset power up time

def draw_power_ups():
    for power_up in power_ups:
        win.blit(power_up['image'], power_up['rect'])
    if power_up_active and pygame.time.get_ticks() // 1000 - star_power_up_start_time < power_up_duration:
        remaining_time = max(0, power_up_duration - (pygame.time.get_ticks() // 1000 - star_power_up_start_time))
        timer_text = f"Star Power-Up: {remaining_time} sec"
        timer_surface = font.render(timer_text, True, (255, 255, 255))
        win.blit(timer_surface, (sw - timer_surface.get_width() - 10, 10))




def bg_image():
    bg = pygame.transform.scale(pygame.image.load("./Assets/bg.jpg").convert_alpha(), (sw, sh))
    win.blit(bg, (0, 0))

def Asteroid(x, y, angle):
    asteroid_image = pygame.transform.scale(pygame.image.load('./Assets/asteroids.png').convert_alpha(), (120, 120))
    rotated_image = pygame.transform.rotate(asteroid_image, angle)
    win.blit(rotated_image, (x, y))


    
def update_asteroids():
    for asteroid in asteroids:
        asteroid['rect'].y += asteroid['speed']
        asteroid['angle'] += 0.5  
        if asteroid['angle'] >= 360:
            asteroid['angle'] -= 360

        
        asteroid['speed'] += 0.01
        if asteroid['speed'] > 3:  # max speed
            asteroid['speed'] = 3

        # resets asteroid
        if asteroid['rect'].y > sh:
            asteroid['rect'].y = -120
            asteroid['rect'].x = random.randint(0, sw)


def create_asteroid():
    if random.randint(0, 500) < 2: 
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            x = random.randint(0, sw - 120)
            y = -120
        elif side == 'bottom':
            x = random.randint(0, sw - 120)
            y = -120
        elif side == 'left':
            x = -120
            y = random.randint(0, sh - 120)
        else:
            x = sw + 120
            y = random.randint(0, sh - 120)
        angle = random.randint(0,360)
        asteroids.append({'rect': pygame.Rect(x, y, 120, 120), 'speed': random.randint(1, 3), 'angle': angle})


def pause_game():
    paused = True
    pause_ticks = pygame.time.get_ticks() 
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
    return pygame.time.get_ticks() - pause_ticks

def lost_game(): 
    lost = True
    replay = False  
    while lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  
        
        lost_text = font.render("You Lost!", True, (255, 255, 255))
        win.blit(lost_text, (350, 300))

        replay_text = font.render("Press the r key to restart", True, (255, 255, 255))
        win.blit(replay_text, (275, 380))

        pygame.display.update()


    return False 

start_ticks = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 36)

run = True
replay = False
paused = False
while run:
    clock.tick(60)
    if replay:
        replay = False
        start_ticks = pygame.time.get_ticks()  
        player_x = 350
        player_y = 480
        change_in_x_pos = 0  
        change_in_y_pos = 0
        asteroids = []  

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
                pause_duration = pause_game()
                start_ticks += pause_duration
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_in_x_pos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_in_y_pos = 0
            
            spawn_timer += 1
            if spawn_timer >= 90:  # spawn frequency
                spawn_timer = 0
                spawn_power_up()

        if not power_up_active:  # check not active
            for power_up in power_ups:
                if power_up['rect'].colliderect(pygame.Rect(player_x, player_y, 60, 60)): 
                    if power_up['image'] == star_image:
                        power_up_active = True

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

    for asteroid in asteroids:
        Asteroid(asteroid['rect'].x, asteroid['rect'].y, asteroid['angle'])

        

    for asteroid in asteroids:
        if not power_up_active:  # check if active
            if asteroid['rect'].colliderect(pygame.Rect(player_x, player_y, 60, 60)):  
                asteroid['rect'] = (pygame.Rect(player_x, player_y, 30, 30))
                boom_img_scaled = pygame.transform.scale(boom_img, (int(boom_img.get_width() * 0.8), int(boom_img.get_height() * 0.8)))
                boom_x = player_x - boom_img_scaled.get_width() / 2
                boom_y = player_y - boom_img_scaled.get_height() / 2
                win.blit(boom_img_scaled, (boom_x, boom_y))
                replay = lost_game()
        else:
            if asteroid['rect'].colliderect(pygame.Rect(player_x, player_y, 60, 60)): 
                asteroids.remove(asteroid)



    update_asteroids()
    create_asteroid()

    draw_power_ups()
    handle_collisions()
    update_power_ups()

    # timer
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_seconds = max(0, 120 - elapsed_seconds)
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    timer_text = f"Time: {minutes:02}:{seconds:02}"
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    win.blit(timer_surface, (10, 10))

    if remaining_seconds == 0:
        win.fill((0, 0, 0))
        win_statement = "You won!"
        win_surface = font.render(win_statement, True, (255, 255, 255))
        win.blit(win_surface, (330, 400))
        pygame.display.flip()
        pygame.time.delay(3000)
        run = False


    pygame.display.update()

pygame.quit()