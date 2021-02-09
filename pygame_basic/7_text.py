import pygame

pygame.init() #Clearing MUST NEED

# display setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# game title
pygame.display.set_caption("Jae's Game") # name of the game

# FPS
clock = pygame.time.Clock()

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

#moving speed
character_speed = 0.6

#enemy charcater
enemy = pygame.image.load("C:/Users/Jae/Projects/pygame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #size of enemy
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # half of the width
enemy_y_pos = (screen_height / 2)- (enemy_height / 2) # at the bottom


# Font
game_font = pygame.font.Font(None, 40) # create font and adjust font & size

# Total time
total_time = 10

# start time
start_ticks = pygame.time.get_ticks() # get start tick

# Event loop
running = True # is game running?
while running:
    dt = clock.tick(60) # frame per second on the game display

    for event in pygame.event.get(): # what event is running? (MUST NEED to run) 
        if event.type == pygame.QUIT: # closing event happen?
            running = False # no longer running
        
        if event.type == pygame.KEYDOWN: #check if key is pressed
            if event.key == pygame.K_LEFT: #move character left
                to_x -= character_speed # to_x = to_x - 5
                
            elif event.key == pygame.K_RIGHT: #move character right
                to_x += character_speed #to_x = to_x + 5
                
            elif event.key == pygame.K_UP: #move character up
                to_y -= character_speed # to move up it is -
                
            elif event.key == pygame.K_DOWN: # move character down
                to_y += character_speed #to move down it is +
                
        if event.type == pygame.KEYUP: # character stops move when key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # by * dt game speed is fix even fps is changed
    character_y_pos += to_y * dt

    # keeping character inside of background
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # collision rect update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # collision check
    if character_rect.colliderect(enemy_rect):
        print("Game Over")
        running = False



    screen.blit(background, (0, 0))  # x, y grid background
    screen.blit(character, (character_x_pos, character_y_pos)) # displaying character
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # displaying enemy

    # timer
    # total time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # divide total time (ms) by 1000 and display seconds

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # Display letter, True, color
    screen.blit(timer, (10,10))

    # if time is less than 0 game ends
    if total_time - elapsed_time <= 0:
        print("Time Out")
        running = False

    pygame.display.update() # keep up the background! MUST NEED

# wait before close
pygame.time.delay(2000) # wait for 2 sec (ms)

# end pygame
pygame.quit()