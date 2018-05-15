import pygame

pygame.init()

WIDTH = 650
HEIGHT = 450
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (247, 85, 44)

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('A Small Trip to the Store')
clock = pygame.time.Clock()

catchImg = pygame.image.load('ctb.png')

def catch(x,y):
    coord = (x,y)
    gameDisplay.blit(catchImg, coord)

x = (WIDTH * 0.38)
y = (HEIGHT * 0.5)
leftKeyDown = False
rightKeyDown = False
x_change = 5

done = False
while(not done):

    for event in pygame.event.get():
        # quit the game if "x" button is pressed or if the escape key is pressed
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftKeyDown = True
            elif event.key == pygame.K_RIGHT:
                rightKeyDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftKeyDown = False
            elif event.key == pygame.K_RIGHT:
                rightKeyDown = False
        
        #print(event)

    gameDisplay.fill(ORANGE)
    
    if (leftKeyDown):
        x -= x_change
        
    if (rightKeyDown):
        x += x_change
        
    
    catch(x,y)
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
