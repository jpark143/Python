import os
import pygame # very first thing
#######################################################################
# basic initialization
pygame.init() #Clearing MUST NEED

# display setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


# game title
pygame.display.set_caption("Pang of Game")

# FPS
clock = pygame.time.Clock()
#######################################################################

# 1. user game initialization (background, game image, grid, speed, font, etc.)
current_path = os.path.dirname(__file__) # locate current file location
image_path = os.path.join(current_path, "images") #images folder

# background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # locate character above stage

# character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# moving character
character_to_x = 0

# character speed
character_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# weapon can be used multiple times
weapons = []

# weapon speed
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. taking events (input from keyboard, mouse, etc.)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    
    # 3. setting character position
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # weapon location
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # shoot the weapon
    
    # weapon disappear when it hits to top
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
        
    # 4. taking care of collision

    # 5. display on screen
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons: # by coding weapon before the stage and character, the weapon will display above the character.
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos)) 

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    

    pygame.display.update() # keep up the background! MUST NEED

# end pygame
pygame.quit()