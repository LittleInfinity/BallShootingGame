import pygame as py
import UtilPygame as up
class Bullet:
    def __init__(self, gamedisplay, x, y, size, color, vel):
        self.gameDisplay = gamedisplay
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vel = vel
    
    def paint(self):
        py.draw.rect(self.gameDisplay, up.Colors.green, (self.x, self.y, self.size, self.size))

    def updatePos(self):
        self.y = self.y - self.vel

