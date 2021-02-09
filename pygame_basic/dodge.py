# dodging game

# [game requirement]
# 1. character must be at the bottom
# 2. missile drops from top. x grid is random every time
# 3. once character dodge the missile, next missile drops
# 4. game is over once character gets hit by the missile
# 5. FPS is fix to 30

# [game image]
# 1. background : 480 by 640 (width, height) - background.png
# 2. character : 70 by 70 - character.png
# 3, missile : 70 by 70 - enemy.png


import random # importing random
import pygame # very first thing
#######################################################################
# basic initialization
pygame.init() #Clearing MUST NEED

# display setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# game title
pygame.display.set_caption("Dodge the Missile")

# FPS
clock = pygame.time.Clock()
#######################################################################

# 1. user game initialization (background, game image, grid, speed, font, etc.)
# create background
background = pygame.image.load("C:\\Users\\Jae\\Projects\\pygame\\pygame_basic\\sky.jpg")

# create character
character = pygame.image.load("C:\\Users\\Jae\\Projects\\pygame\\pygame_basic\\jet.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_height - character_height

# moving location
character_to_x_LEFT = 0
character_to_x_RIGHT = 0
character_speed = 10

#missile
missile = pygame.image.load("C:\\Users\\Jae\\Projects\\pygame\\pygame_basic\\missile.jpg")
missile_size = missile.get_rect().size
missile_width = missile_size[0]
missile_height = missile_size[1]
missile_x_pos = random.randint(0, screen_width - missile_width)
missile_y_pos = 0
missile_speed = 10


running = True
while running:
    dt = clock.tick(30)

# 2. taking events (input from keyboard, mouse, etc.)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0

    # 3. setting character position
    character_x_pos += character_to_x_LEFT + character_to_x_RIGHT

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    missile_y_pos += missile_speed

    if missile_y_pos > screen_height:
        missile_y_pos = 0
        missile_x_pos = random.randint(0, screen_width - missile_width)
        
    # 4. taking care of collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    missile_rect = missile.get_rect()
    missile_rect.left = missile_x_pos
    missile_rect.top = missile_y_pos

    if character_rect.colliderect(missile_rect):
        print("Game Over")
        running = False

    # 5. display on screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(missile, (missile_x_pos, missile_y_pos))

    pygame.display.update() # keep up the background! MUST NEED

# end pygame
pygame.quit()