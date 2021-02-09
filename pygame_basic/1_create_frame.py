import pygame

pygame.init() #Clearing MUST NEED

# display setting
screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("Jae's Game") # name of the game

# Event loop
running = True # is game running?
while running:
    for event in pygame.event.get(): # what event is running? (MUST NEED to run) 
        if event.type == pygame.QUIT: # closing event happen?
            running = False

# end pygame
pygame.quit()