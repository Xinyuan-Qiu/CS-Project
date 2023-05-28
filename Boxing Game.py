import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT,MOUSEBUTTONDOWN

pygame.init()


#score 
score = 0
pygame.font.init()
myfont = pygame.font.Font(None,60)
life_times, is_over = 3, False
#screen
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("King of Fighters")
clock = pygame.time.Clock()
clock.tick(30)

bar_min_color = pygame.Color(200, 0, 0)
bar_max_color = pygame.Color(0, 200, 0)
bar_x1 = 0
bar_y1 = 50
max_bar_width1 = 400
bar_height1 = 50
bar_x2 = 600
bar_y2 = 50
max_bar_width2 = 400
bar_height2 = 50
health_percent = 0.5
health_percent = 0.5
bar_width1 = max_bar_width1 * health_percent
bar_width2 = max_bar_width2 * health_percent
bar_foreground_color = bar_min_color.lerp(bar_max_color, health_percent)

# jump
jumping = False
y_gravity = 1
jump_height = 30
y_speed = jump_height
player1x_position = 60
player1y_position = 340
player2x_position = 685
player2y_position = 300

#punching
fireball = 0
fireball_speed = 0

#player
player1_img = pygame.image.load("fireman1.png")
player1_a = pygame.transform.scale(player1_img,(160,160))
player1 = pygame.Rect(player1x_position, player1y_position, 160, 160)
player2_img = pygame.image.load("fireman2.png")
player2_a = pygame.transform.scale(player2_img,(200,200))
player2 = pygame.Rect(player2x_position, player2y_position, 200, 200)
player_speed = 30
life_bars = 0
def player():
    screen.blit(player1_a,(player1.x,player1.y))
    screen.blit(player2_a,(player2.x,player2.y))

# Get the current dimensions of the image
#original_size = bg_image.get_size()

# Define the new dimensions for the scaled image
#new_size = (original_size[0] / 5, original_size[1] / 5)

# Scale the image to the new size
#scaled_image = pygame.transform.scale(bg_image, new_size)


def start():
    bg_image = pygame.image.load("background.png")
    screen.blit(bg_image, (0, 0))  
    button_img = pygame.image.load("Press_enter.png")
    screen.blit(button_img, (370, 500 ))
def mainscreen():
    main_image = pygame.image.load("playground.png")
    screen.blit(main_image, (0, 0))  
        
def main():
    global startacreen_run
    startacreen_run = True
    global running
    running = False
    #global turnaround
    #turnaround = False
    
    while startacreen_run:
        start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startacreen_run = False  
            elif event.type == MOUSEBUTTONDOWN:
                print(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    startacreen_run = False
                if event.key == pygame.K_RETURN:
                    running = True
                    startacreen_run = False
        pygame.display.update()

    while running:
        mainscreen()
    # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        player()
        bar()
        # Handle player 1 movement

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x > 0:
            player1.x -= player_speed
        
          
        # elif keys[pygame.K_SPACE]:
        #     jumping = True

        # elif jumping:
        #     player1y_position -= y_speed
        #     y_speed -= y_gravity
        #     if y_speed < -jump_height:
        #         jumping = False
        #         y_speed = jump_height
            
            
            #if not turnaround:
                #player1_img = pygame.transform.flip(player1_img, True, False)
            #turnaround = True
        elif keys[pygame.K_d] and player1.x < WINDOW_WIDTH - player1.width:
            player1.x += player_speed
        # elif keys[pygame.K_w] and player1.y > 0:
        #     player1.y -= player_speed
        # elif keys[pygame.K_s] and player1.y < WINDOW_HEIGHT - player1.height:
        #     player1.y += player_speed
        
        # Handle player 2 movement
        if keys[pygame.K_LEFT] and player2.x > 0:
            player2.x -= player_speed
        elif keys[pygame.K_RIGHT] and player2.x < WINDOW_WIDTH - player2.width:
            player2.x += player_speed
        # elif keys[pygame.K_UP] and player2.y > 0:
        #     player2.y -= player_speed
        # elif keys[pygame.K_DOWN] and player2.y < WINDOW_HEIGHT - player2.height:
        #     player2.y += player_speed
        
        # Handle punching
        if keys[pygame.K_SPACE]:
            if player1.colliderect(player2):
                    print("Player 1 punches Player 2!")
            
            elif player2.colliderect(player1):          
                    print("Player 2 punches Player 1!")
    
        pygame.display.update()
if player1.colliderect(player2):
        print('The red square collided with the green square')
        # In order to see the collision result conveniently, directly break returns
        score -= 10
if life_times <= 0:
      is_over = True

def bar():
    
# bar background
    pygame.draw.rect(screen, bar_min_color, (bar_x1, bar_y1, max_bar_width1, bar_height1), 2)
    
# bar foreground
    pygame.draw.rect(screen, bar_foreground_color, (bar_x1, bar_y1, bar_width1, bar_height1))
     
    pygame.draw.rect(screen, bar_min_color, (bar_x2, bar_y2, max_bar_width1, bar_height1), 2)
    
    pygame.draw.rect(screen, bar_foreground_color, (bar_x2, bar_y2, bar_width2, bar_height2))

if __name__ == "__main__":
    main()

#life bar
    textImage = myfont.render("score: " + 
str(score), True, (0, 0, 255))
    screen.blit(textImage, (10,10))
    if is_over:
        gameOverTextImage = myfont.render('GAME OVER!', True, (255, 0, 0))
    screen.blit(gameOverTextImage, (80,150))


