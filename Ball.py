import random
import GlobalConstants as gc
import pygame as py

class RandomBall:
    def __init__(self, surface, screen_width, screen_height, name):

        #self.textsurface = textsurface
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = surface
        self.color = random.choice(gc.colorList)
        self.x_coordinate = random.randint(0, screen_width)
        self.y_coordinate = random.randint(0, screen_height)
        #self.radius = random.randint(25, 50)
        self.radius = 10
        #self.width = self.radius if self.radius < 5 else 5
        self.width = 0
        self.x_velocity = random.randrange(1, 20)/5
        self.y_velocity = random.randrange(1, 20)/5
        self.myfont = py.font.SysFont('Comic Sans MS', self.radius//2)
        self.textsurface = self.myfont.render(name, False, (0, 0, 0))
        
        
    def updatePos(self, offSetFromBottom = 0):
        if (self.x_coordinate + self.radius) >= self.screen_width and self.x_velocity > 0:
            self.x_velocity = -self.x_velocity
            
        if (self.x_coordinate-self.radius) <= 0 and self.x_velocity < 0:
            self.x_velocity = -self.x_velocity
            
        if (self.y_coordinate - self.radius) <= 0 and self.y_velocity < 0:
            self.y_velocity = -self.y_velocity
        
        if (self.y_coordinate + self.radius + offSetFromBottom) >= self.screen_height and self.y_velocity > 0:
            self.y_velocity = -self.y_velocity

        self.x_coordinate += self.x_velocity
        self.y_coordinate += self.y_velocity

    def paint(self):
        py.draw.circle(self.surface, self.color, (int(self.x_coordinate), int(self.y_coordinate)), self.radius, self.width)
        
        #py.draw.rect(self.surface, red,(self.x_coordinate-self.radius/2, self.y_coordinate, 4, 4))

    def paintNameOnBall(self):
        self.surface.blit(self.textsurface,(int(self.x_coordinate -self.textsurface.get_rect().width/2), int(self.y_coordinate -self.textsurface.get_rect().height/2)))
