import pygame

# a class for any object that moves in shopping.py
class MovingObject:

    # to do: decide on public / private attributes

    def __init__(self, xpos, ypos, spd, width, height):
        self.objX = xpos
        self.objY = ypos 
        self.objSpeed = spd
        self.objWidth = width
        self.objHeight = height

    def setX(self, newX):
        self.objX = newX
    def setY(self, newY):
        self.objY = newY

    # sets this object's list of collision points
    def setCollisionPoints(self, points):
        self.collisionPoints = points

    #def resetPosition

    def moveLeft(self):
        self.objX -= self.objSpeed
    def moveRight(self):
        self.objX += self.objSpeed  
    def moveDown(self):
        self.objY += self.objSpeed

    # checks that the object hasn't moved out of bounds
    # horizontally, and if so, fix the obj at bounds
    def checkOutOfBounds(self, screenWidth):
        if (self.objX < 0):
            self.objX = 0
        elif (self.objX > screenWidth - self.objWidth):
            self.objX = screenWidth - self.objWidth

    # vertical collsion: we check if their y values are alligned then check if their x values are alligned
    # returns True if any of self's collision points lie within movingObj's width coords
    def checkVerticalCollision(self, movingObj):
        if (movingObj.objY + movingObj.objHeight >= self.objY + 20): # 20 is an specific num just for the catcher instance, todo: redraw catchImg
            for collisionPoint in self.collisionPoints:
                if ((collisionPoint[0] >= movingObj.objX) and (collisionPoint[0] <= movingObj.objX + movingObj.objWidth)):
                    return True
        return False

    # draws an obj on a given display using pygame
    def drawObj(self, display, color):
        pygame.draw.rect(display, color, [self.objX, self.objY, self.objWidth, self.objHeight])
    
    # blit img on display at this object's current x and y position
    def blitObj(self, display, img): 
        display.blit(img, (self.objX, self.objY))