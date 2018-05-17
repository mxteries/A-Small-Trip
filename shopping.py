import pygame
import random
from moving_object import MovingObject

pygame.init()

WIDTH = 650
HEIGHT = 450
CENTER_TOP = (WIDTH/2, HEIGHT/4)
CENTER = (WIDTH/2, HEIGHT/2)
CENTER_BOT = (WIDTH/2, HEIGHT*3/4)

BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (247, 85, 44)

# pixel dimensions of catchImg
CATCH_WIDTH = 78
CATCH_HEIGHT = 93

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('A Small Trip to the Store')
clock = pygame.time.Clock()

catchImg = pygame.image.load('ctb.png')

def thingsCaught(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Caught: " + str(count), True, BLACK)
    gameDisplay.blit(text, (0,0))

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
    x_change = 10 # how much change in the x position. Increase to go faster
    # define a collision point at the middle of catchImg (for now)
    # note: these values will vary heavily depending on the image
    collisionPointMid = (x + CATCH_WIDTH/2, y+20) # -20 is the dist from the head to the bag LUL

    catcher = MovingObject(x, y, x_change, CATCH_WIDTH, CATCH_HEIGHT) 
    catcher.setCollisionPoint(collisionPointMid) 

    thingStartX = random.randrange(0, WIDTH)
    thingStartY = -600 # start a fair bit off screen at first
    thingSpeed = 3
    thingWidth = 100
    thingHeight = 100
    thing = MovingObject(thingStartX, thingStartY, thingSpeed, thingWidth, thingHeight)

    #thingCount = n # to do: have a loop for multiple things (make sure it's still doable tho)\
    # todo 2: add blocks that will decrease your score

    caught = 0

    leftKeyDown = False
    rightKeyDown = False
    shiftKeyDown = False # left shift
    gameExit = False

    while(not gameExit):

        for event in pygame.event.get():
            # quit the game if (top right) x button is pressed or if the escape key is pressed
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

            # as long as a key is held down, x position will change
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    catcher.objSpeed *= 1.5
                if event.key == pygame.K_LEFT:
                    leftKeyDown = True
                elif event.key == pygame.K_RIGHT:
                    rightKeyDown = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    catcher.objSpeed /= 1.5
                if event.key == pygame.K_LEFT:
                    leftKeyDown = False
                elif event.key == pygame.K_RIGHT:
                    rightKeyDown = False
        

        gameDisplay.fill(ORANGE)
            
        if (leftKeyDown):
            catcher.moveLeft()
        if (rightKeyDown):
            catcher.moveRight()
           
        # prevents moving out of bounds
        catcher.checkOutOfBounds(WIDTH)
        
        # display the catcher
        catcher.blitObj(gameDisplay, catchImg)
        
        # Update collision point 
        catcher.setCollisionPoint( (catcher.objX + CATCH_WIDTH/2, catcher.objY+20) ) 
        
        # display the (falling) thing
        thing.drawObj(gameDisplay, WHITE)
        thing.moveDown()
         

        # OR, when a thingStartY + thingHeight comes to y + 20 (height of our catch bag), 
        # check if a collision point x exists between thingStartX and thingStartX + thingWidth
        if (thing.objY + thing.objHeight >= catcher.objY+20):
            if ((catcher.collisionPoint[0] >= thing.objY) and (catcher.collisionPoint[0] <= thing.objY + thing.objHeight)):
                thing.setY(0-thing.objY/2)
                thing.setX(random.randrange(0, WIDTH))
                caught +=1
                

        # repeat the thing in a new location if it leaves the screen
        if (thing.objY > HEIGHT):
            messageDisplay('LUL', CENTER) # LUL
            thing.setY(0-thing.objY)
            thing.setX(random.randrange(0, WIDTH))

        thingsCaught(caught) 
        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
