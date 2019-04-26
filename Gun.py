import UtilPygame as up
import GlobalConstants as gc
import pygame as py
### Gun Class ###
class Gun:
    gameDisplay = None
    #baseHeight = 10
    baseRadius = 50
    pipeHeight = 35
    bulletXCo = 0
    bulletYCo = 0
    bullseSpeed = 2
    bullet = None
    def __init__(self,gameDisplay, position = (0, 0), color = up.Colors.red, size = 5):
        self.gameDisplay = gameDisplay
        self.x, self.y = position
        self.color = color
        self.size = size

       
        #self.baseWidth = 80
        #self.baseXCo = screen_width/2 - self.baseWidth/2
        self.baseXCo = gc.screen_width/2
        self.baseYCo = gc.screen_height

        
        self.pipeWidth = 20 
        #self.pipeXCo = self.baseXCo + self.baseWidth/2 - self.pipeWidth/2
        self.pipeXCo = self.baseXCo - self.pipeWidth/2
        self.pipeYCo = self.baseYCo-self.baseRadius - self.pipeHeight

    def paint(self):
        self.paintPipe()
        self.paintBase()
        
    
    def paintBase(self):
        py.draw.circle(self.gameDisplay, up.Colors.red, (int(self.baseXCo), int(self.baseYCo)), int(self.baseRadius))
        #py.draw.rect(gameDisplay, up.Colors.red, (self.baseXCo, self.baseYCo, self.baseWidth, self.baseHeight))
    def paintPipe(self):
        py.draw.rect(self.gameDisplay, up.Colors.green, (self.pipeXCo, self.pipeYCo, self.pipeWidth, self.pipeHeight))

    @staticmethod
    def gunHeight():
        return Gun.baseRadius


    def moveLeft(self):
        #print("Inside moveLeft()")
        if self.baseXCo - self.baseRadius - 2 >= 0 and self.pipeXCo - 2 >= 0:
            self.baseXCo = self.baseXCo - 2
            self.pipeXCo = self.pipeXCo - 2
    

    def moveRight(self):
        if self.baseXCo + self.baseRadius + 2 <= gc.screen_width and self.pipeXCo + self.pipeWidth + 2 <= gc.screen_width:
            self.baseXCo = self.baseXCo + 2
            self.pipeXCo = self.pipeXCo + 2

    def fire(self):
        if not self.bullet:
            self.bullet =  Bullet(self.pipeXCo, self.pipeYCo, 5, up.Colors.red, 2)

    def paintBullet(self):
        if self.bullet:
            self.bullet.updatePos()
            if self.bullet.hasCollidedWithUpperBoundary():
                #destroy bullet
                self.bullet = None
            else:
                self.bullet.paint(gameDisplay)
