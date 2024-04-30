import pygame
import random

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

# def player(player_x, player_y):
#     win.blit(player_image, (player_x, player_y))
def player(player_x, player_y):
    player_sprite = pygame.sprite.Sprite()
    player_sprite.image = player_image
    player_sprite.rect = player_image.get_rect(topleft=(player_x, player_y))
    return player_sprite

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(center=(sw // 2, sh // 2))

class bg_image(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./Assets/Cbg.jpg").convert_alpha(), (800, 800))
        self.rect = self.image.get_rect(center=(400, 400))
        self.prev_x = 400 
        self.prev_y = 400  


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image1 = pygame.transform.scale(pygame.image.load('./Assets/asteroids.png').convert_alpha(), (120, 120))
        self.image = self.image1.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0
        self.speed = random.randint(1, 3)
        self.prev_x = x  
        self.prev_y = y  

    def update(self):
        # rotate
        self.angle += 0.5
        rotated_image = pygame.transform.rotate(self.image1, self.angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)
        self.image = rotated_image

        
        self.rect.y += self.speed
        if self.rect.top > sh:
            self.rect.y = -120
            self.rect.x = random.randint(0, sw)

asteroids_on_screen = pygame.sprite.Group()


new_asteroid = Asteroid(random.randint(0, sw), random.randint(0, sh))
while pygame.sprite.spritecollide(new_asteroid, asteroids_on_screen, False):
    new_asteroid.rect.x = random.randint(0, sw)
    new_asteroid.rect.y = random.randint(0, sh)

asteroids_on_screen.add(new_asteroid)



def unpause_game():
    for asteroid in asteroids_on_screen:
        asteroid.rect.x, asteroid.rect.y = asteroid.prev_x, asteroid.prev_y
    bg_image.rect.x, bg_image.rect.y = bg_image.prev_x, bg_image.prev_y

background = bg_image()


#boundaries
def create_asteroid():
    if random.randint(0,400) < 0.075:
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
        asteroid = Asteroid(x, y)
        asteroids_on_screen.add(asteroid)
        asteroids_on_screen.add(asteroid)

# timer
start_ticks = pygame.time.get_ticks()
elapsed_seconds = 0
font = pygame.font.SysFont(None, 36)

# pause
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

        

# main game loop
run = True
paused = False
while run:
    clock.tick(60)
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                paused = True
                pause_game()
        # if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_in_x_pos = -3
            elif event.key == pygame.K_RIGHT:
                change_in_x_pos = 3
            elif event.key == pygame.K_UP:
                change_in_y_pos = -3
            elif event.key == pygame.K_DOWN:
                change_in_y_pos = 3
        # Check for keystroke release
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_in_x_pos = 0


    if player_x <= 0:
        player_x = 0
    elif player_x >= 900:
        player_x = 900

    if player_y <= 0:
        player_y = 0
    elif player_y >= 800:
        player_y = 800

    player_x += change_in_x_pos
    player_y += change_in_y_pos

    # more timer stuff
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_seconds = max(0, 120 - elapsed_seconds)
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    timer_text = f"Time: {minutes:02}:{seconds:02}"
    
    if remaining_seconds == 0:
        run = False


    create_asteroid()
    
    win.blit(background.image, background.rect)


    player_sprite = player(player_x, player_y)
    win.blit(player_sprite.image, player_sprite.rect)
    asteroids_on_screen.update()
    asteroids_on_screen.draw(win)


# collision = pygame.sprite.spritecollide(player, asteroids_on_screen, False)
# if collision:
#     run = False
# if not run:
#     win.fill((0,0,0))
#     pygame.display.update()

    
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    win.blit(timer_surface, (330, 10))

    pygame.display.update()

pygame.quit()