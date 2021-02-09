import pygame

pygame.init() #Clearing MUST NEED

# display setting
screen_width = 480
screen_height = 640
screen= pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("Jae's Game") # name of the game

#background from folder
background = pygame.image.load("C:/Users/Jae/Projects/pygame/pygame_basic/background.png")

# Event loop
running = True # is game running?
while running:
    for event in pygame.event.get(): # what event is running? (MUST NEED to run) 
        if event.type == pygame.QUIT: # closing event happen?
            running = False # no longer running
            
    screen.blit(background, (0, 0))  # x, y grid

    #just filling backgroud with color
    #screen.fill((0,0,255))

    pygame.display.update() # keep up the background! MUST NEED

# end pygame
pygame.quit()