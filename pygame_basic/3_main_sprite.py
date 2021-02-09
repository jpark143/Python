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


# Event loop
running = True # is game running?
while running:
    for event in pygame.event.get(): # what event is running? (MUST NEED to run) 
        if event.type == pygame.QUIT: # closing event happen?
            running = False # no longer running
            
    screen.blit(background, (0, 0))  # x, y grid

    screen.blit(character, (character_x_pos, character_y_pos)) # displaying character

    pygame.display.update() # keep up the background! MUST NEED

# end pygame
pygame.quit()