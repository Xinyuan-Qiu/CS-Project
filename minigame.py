import pygame, sys
import random
#rules: If the green bar touches by the ground, the game is over.
# Initialize
pygame.init()
SCREEN = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Mini game')
def main():
    print("Hello")

# The green square is fixed at the bottom, moves left and right, and the y value remains unchanged
green_x = 110
green_y = 110
# The red square moves from top to bottom, and the x value remains the same


red_y = 0
red_y_speed = 5
# game loop
score = 0
pygame.font.init()
myfont = pygame.font.Font(None,60)
red_x = 35

life_times, is_over = 3, False
while True: 
    for event in pygame.event.get():
        # Handle exit events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # keyboard press event
        elif event.type == pygame.KEYDOWN:
            # 'a' key is pressed
            if event.key == pygame.K_a:
                green_x -= 5
            elif event.key == pygame.K_d:
                green_x += 5
    keys = pygame.key.get_pressed()

    red_y += red_y_speed * 2

    if keys[119] == True:  # w
        green_y -= 10

    if keys[97] == True:  # a
        green_x -= 10

    if keys[115] == True:  # s
        green_y  += 10

   
    if keys[100] == True:  # d
        green_x  += 10
        
    green_rect = pygame.Rect(green_x, 250, 100, 50)
    if green_rect.colliderect(red_x, red_y, 20, 50):
        print('collision')
        # In order to see the collision result conveniently, directly break returns
        score += 1
        red_y = 0
        red_x = random.randint(50, 350)
    if red_y == 800:
        life_times -= 1
        if life_times <= 0:
            is_over = True
        red_y = 0
        red_x = random.randint(50, 350)
        
    SCREEN.fill((255, 255, 255))
    # Call the pygame.display.update() method to update the entire screen display
    pygame.draw.rect(SCREEN, (255, 0, 0), (red_x, red_y, 20, 50))
    pygame.draw.rect(SCREEN, (0, 255, 0), (green_x, 250, 100, 50))
    textImage = myfont.render("score: " + str(score), True, (0, 0, 255))
    SCREEN.blit(textImage, (10,10))
    if is_over:
        gameOverTextImage = myfont.render('GAME OVER!', True, (255, 0, 0))
         
        SCREEN.blit(gameOverTextImage, (80,150))
    pygame.display.update()
    pygame.time.delay(50)


   
