import pygame # very first thing
#######################################################################
# basic initialization
pygame.init() #Clearing MUST NEED

# display setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# game title
pygame.display.set_caption("name of Game")

# FPS
clock = pygame.time.Clock()
#######################################################################

# 1. user game initialization (background, game image, grid, speed, font, etc.)

running = True
while running:
    dt = clock.tick(30)

    # 2. taking events (input from keyboard, mouse, etc.)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    # 3. setting character position
        
    # 4. taking care of collision

    # 5. display on screen

    pygame.display.update() # keep up the background! MUST NEED

# end pygame
pygame.quit()