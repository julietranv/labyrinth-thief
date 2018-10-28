import pygame
from pygame.locals import *

class Guard:
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY

        self.images= [pygame.image.load("guardfront.png"), pygame.image.load("guardback.png"), pygame.image.load("guardright.png"), pygame.image.load("guardleft.png")]

        self.cos = 0

    def draw(self, window):
        window.blit(self.images[self.cos], (self.x, self.y))

    def paceReg1(self):
        self.cos = 1
        myRec = self.getRec()
        width = myRec[2]
        height = myRec[3]
        self.y -= 10
        self.y -= 10
        self.y -= 10
        self.y -= 10
        self.y -= 10
        self.cos = 0
        self.y += 10
        self.y += 10
        self.y += 10
        self.y += 10
        self.y += 10    

    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        
        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
            return True
        return False


    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.images[self.cos].get_rect()
        return (self.x, self.y, myRec[2], myRec[3])

        
