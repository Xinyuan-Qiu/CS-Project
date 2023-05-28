import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
from math import pi
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Ocean water')
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables
boat_x = 100
boat_y = 60
boat_speed = 5

fish_x = 300
fish_y = 200
fish_x_speed = 3
fish_y_speed = 3

wave_x = 100
wave_y = 200
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
    if boat_x + 260 > WIDTH or boat_x < 0:
      boat_speed *= -1

    if fish_x + 260 > WIDTH or fish_x < 0:
      fish_x_speed *= -1 
    if fish_y + 200 > HEIGHT  or fish_y < 172:
      fish_y_speed *= -1

    boat_x += boat_speed
    fish_x += fish_x_speed
    fish_y += fish_y_speed
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    #boat
    pygame.draw.arc(screen, (204, 204, 0), (boat_x, boat_y, 150, 125), pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen,(204,204,0), (boat_x, boat_y, 150, 125), 3 * pi / 2, 2 * pi, 2)
    pygame.draw.line(screen,(204,204,0),(boat_x, boat_y + 61), (boat_x + 149, boat_y + 64))
    pygame.draw.line(screen, (255,0,0), (boat_x + 73, boat_y + 65), (boat_x + 70, boat_y - 21))
    pygame.draw.line(screen,(255,0,0), (boat_x + 70, boat_y - 19), (boat_x + 135, boat_y))
    pygame.draw.line(screen,(255,0,0),(boat_x + 72, boat_y + 26), (boat_x +134, boat_y + 2))
    #fish
    pygame.draw.circle(screen, (0,0,0), (fish_x + 76,fish_y-4), 5)
    pygame.draw.line(screen,(0,0,0),(fish_x + 53,fish_y -4),(fish_x+109,fish_y-29))
    pygame.draw.line(screen,(0,0,0),(fish_x+53,fish_y-4),(fish_x + 109,fish_y+13))
    
    pygame.draw.line(screen, (0,0,0),(fish_x+109, fish_y-29),(fish_x+109,fish_y+13))
    
    pygame.draw.line(screen,(0,0,0),(fish_x+109,fish_y-29),(fish_x+178,fish_y-3)) 
    pygame.draw.line(screen,(0,0,0),(fish_x+109,fish_y+13),(fish_x+178,fish_y-3)) 
    
    pygame.draw.line(screen,(0,0,0),(fish_x+178,fish_y-3),(fish_x+207,fish_y-20)) 
    pygame.draw.line(screen,(0,0,0),(fish_x+178,fish_y-3),(fish_x+207,fish_y+15))
    
    pygame.draw.line(screen,(0,0,0),(fish_x+207,fish_y-20),(fish_x+207,fish_y+15)) 
   
    #wave
    pygame.draw.arc(screen, (0,105,148), [65, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [65, 173, 150, 125], pi / 2, pi, 2)  
    pygame.draw.arc(screen, (0,105,148), [15, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [15, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [105, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [105, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [155, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen,(0,105,148), [155, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [205, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [205, 173, 150, 125], pi / 2, pi, 2) 
    pygame.draw.arc(screen, (0,105,148), [245, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [245, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen,(0,105,148), (285,173,150,125), pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [285, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [325, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [325, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [365, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [365, 173, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, (0,105,148), [405, 173, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, (0,105,148), [405, 173, 150, 125], 0, pi / 2, 2)
    
    
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
