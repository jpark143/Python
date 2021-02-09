import pygame

pygame.init() #Clearing MUST NEED

# display setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# game title
pygame.display.set_caption("Jae's Game") # name of the game

#background from folder
background = pygame.image.load("C:/Users/Jae/Projects/pygame/pygame_basic/background.png")

# calling sprite (character)
character = pygame.image.load("C:/Users/Jae/Projects/pygame/pygame_basic/char.png")
character_size = character.get_rect().size #size of character
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # half of the width
character_y_pos = screen_height - character_height # at the bottom

#moving grid
to_x = 0
to_y = 0


# Event loop
running = True # is game running?
while running:
    for event in pygame.event.get(): # what event is running? (MUST NEED to run) 
        if event.type == pygame.QUIT: # closing event happen?
            running = False # no longer running
        
        if event.type == pygame.KEYDOWN: #check if key is pressed
            if event.key == pygame.K_LEFT: #move character left
                to_x -= 1 # to_x = to_x - 1
                
            elif event.key == pygame.K_RIGHT: #move character right
                to_x += 1 #to_x = to_x + 1
                
            elif event.key == pygame.K_UP: #move character up
                to_y -= 1 # to move up it is -
                
            elif event.key == pygame.K_DOWN: # move character down
                to_y += 1 #to move down it is +
                
        if event.type == pygame.KEYUP: # character stops move when key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # keeping character inside of background
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0))  # x, y grid background

    screen.blit(character, (character_x_pos, character_y_pos)) # displaying character

    pygame.display.update() # keep up the background! MUST NEED

# end pygame
pygame.quit()