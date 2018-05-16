import pygame
import random

pygame.init()

WIDTH = 650
HEIGHT = 450
CENTER_TOP = (WIDTH/2, HEIGHT/4)
CENTER = (WIDTH/2, HEIGHT/2)
CENTER_BOT = (WIDTH/2, HEIGHT*3/4)

BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (247, 85, 44)

CATCH_WIDTH = 78

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('A Small Trip to the Store')
clock = pygame.time.Clock()

catchImg = pygame.image.load('ctb.png')

# draws things and objects into our game
def things(thingX, thingY, thingW, thingH, thingColor):
    pygame.draw.rect(gameDisplay, thingColor, [thingX, thingY, thingW, thingH])

def thingsCaught(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Caught: " + str(count), True, BLACK)
    gameDisplay.blit(text, (0,0))

# displays catchImg at coord (x,y)
def catch(x,y):
    coord = (x,y)
    gameDisplay.blit(catchImg, coord)

# return a text surface and a text rect from a given text, font, and color
def textObjects(text, font, color):
    textSurface = font.render(text, True, color) # render text, anti aliasing, and color
    return textSurface, textSurface.get_rect()

# displays 115 size text at location
def messageDisplay(text, location):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = textObjects(text, largeText, BLACK)
    TextRect.center = location
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def gameLoop():
    x = (WIDTH * 0.38)
    y = (HEIGHT * 0.75)

    # set collision point at left, middle, and right of bag
    # note, these values will vary heavily depending on the image
  
    collisionPointLeft = (x + CATCH_WIDTH/3,y+20) # -20 is the dist from the head to the bag LUL
    collisionPointMid = (x + CATCH_WIDTH/2, y+20) 
    collisionPointRight = (x + CATCH_WIDTH*3/4, y+20)

    x_change = 10 # how much change in the x position. Increase to go faster
    
    thingStartX = random.randrange(0, WIDTH)
    thingStartY = -600 # start a fair bit off screen at first
    thingSpeed = 3
    thingWidth = 100
    thingHeight = 100

    #thingCount = n # to do: have a loop for multiple things (make sure it's still doable tho)\
    # todo 2: add blocks that will decrease your score

    caught = 0

    leftKeyDown = False
    rightKeyDown = False
    shiftKeyDown = False # left shift
    gameExit = False

    while(not gameExit):

        for event in pygame.event.get():
            # quit the game if "x" button is pressed or if the escape key is pressed
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

            # as long as a key is held down, x position will change
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    x_change *= 1.5
                if event.key == pygame.K_LEFT:
                    leftKeyDown = True
                elif event.key == pygame.K_RIGHT:
                    rightKeyDown = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    x_change /= 1.5
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

        # prevents moving out of bounds
        if (x < 0):
            x = 0
            
        elif (x > WIDTH - CATCH_WIDTH):
            x = WIDTH - CATCH_WIDTH
            
            
        catch(x,y)
        

        # Update collision points
        collisionPointLeft = (x + CATCH_WIDTH/3,y+20)  
        collisionPointMid = (x + CATCH_WIDTH/2, y+20) 
        collisionPointRight = (x + CATCH_WIDTH*3/4, y+20)
        
        things(thingStartX, thingStartY, thingWidth, thingHeight, WHITE)
        thingStartY += thingSpeed # redraw the thing 7 pixels lower each frame

        # bottom right corner of thing is thingWidth, thingHeight
        # iterate from 0 to thingWidth, keeping thingHeight constant. 

        # OR, when a thingStartY + thingHeight comes to y + 20 (height of our catch bag), 
        # check if a collision point x exists between thingStartX and thingStartX + thingWidth
        if (thingStartY + thingHeight >= y+20):
            if ((collisionPointMid[0] >= thingStartX) and (collisionPointMid[0] <= thingStartX + thingWidth)):
                thingStartY = 0 - thingHeight/2
                thingStartX = random.randrange(0, WIDTH)
                caught +=1
                thingSpeed *=1.15
                thingWidth *= 1.05
                

        #if (thingStartY )
        # repeat the thing in a new location if it leaves the screen
        if (thingStartY > HEIGHT):
            messageDisplay('LUL', CENTER) # LUL
            thingStartY = 0 - thingHeight
            thingStartX = random.randrange(0, WIDTH)

        thingsCaught(caught) 
        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
