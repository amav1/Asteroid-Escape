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

# creating the player object
player_image = pygame.image.load("./Assets/spaceship.png")
player_x = 410
player_y = 480
change_in_x_pos = 0
change_in_y_pos = 0

def player(player_x, player_y):
    win.blit(player_image, (player_x, player_y))

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  
        self.rect = self.image.get_rect(center=(sw//2, sh//2))

class bg_image(pygame.sprite.Sprite):
    def __init__(self):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load("./Assets/Cbg.jpg").convert_alpha(), (800, 800))
       self.rect = self.image.get_rect(center=(400, 400))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image1 = pygame.transform.scale(pygame.image.load('asteroids.png').convert_alpha(), (120, 120)) 
        self.image = self.image1.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0
        self.speed = random.randint(1, 3)  

    def update(self):
        # rotates asteroids
        self.angle += 0.5  
        rotated_image = pygame.transform.rotate(self.image1, self.angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)
        self.image = rotated_image
        
        
        self.rect.y += self.speed
        if self.rect.top > sh:  
            self.rect.y = -120  # puts asteroid at the top of the screen
            self.rect.x = random.randint(0, sw)  


asteroidz = Object()
bg1_image = bg_image()
all_sprites = pygame.sprite.Group()
all_sprites.add(asteroidz)
all_sprites.add(bg1_image)

asteroids = pygame.sprite.Group()

#boundaries
def create_asteroid():
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
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

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
                if event.key == pygame.K_p:  
                    paused = False
                    #need to figure out how to save previous progress to continue
        win.fill((0, 0, 0))
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
            if event.key == pygame.K_p: 
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

    
    if not paused:
        all_sprites.update()

        # collision between asteroids and sprite (WIP)
        # hits = pygame.sprite.spritecollide(spaceship, asteroids, True)
        # if hits:
        #     print("Oops!") or print("Be careful!") or print("Watch it!!")

        # asteroids
        if random.randint(0, 100) < 1:  
            create_asteroid()

    
    win.fill((0, 0, 0))  # clears screen
    all_sprites.draw(win)

    # draws timer
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    timer_rect = timer_surface.get_rect(midtop=(sw // 2, 10))
    win.blit(timer_surface, timer_rect)

    player(player_x, player_y)

    pygame.display.update()

pygame.quit()