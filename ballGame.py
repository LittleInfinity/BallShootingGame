import pygame as py
import random
import time
import UtilPygame as up
import Gun
import Ball
import GlobalConstants as gc
import Bullet as b


py.mixer.pre_init(44100, 16, 2, 4096)
py.init()
fire_sound = py.mixer.Sound("gun.wav")
ball_pop_sound = py.mixer.Sound("pop.wav")
animationExit = False

gameDisplay = py.display.set_mode([gc.screen_width, gc.screen_height], py.RESIZABLE)
py.display.set_caption("Ball Animation")
py.font.init()


class ShootingGame:
    balls = []
    ball_count = 400
    bullets = []
    gun = None
    def __init__(self):
        self.gun = Gun.Gun(gameDisplay)
        
        #creating ten balls for game, we can make it configurable later
        for i in range (1, self.ball_count):
            self.balls.append(Ball.RandomBall(gameDisplay, gc.screen_width, gc.screen_height, ""))

    def gunFired(self):
        #add new bullet in bullet list.
        py.mixer.Sound.play(fire_sound)
        self.bullets.append(b.Bullet(gameDisplay, self.gun.pipeXCo + (self.gun.pipeWidth)/2 - 2.5 , self.gun.pipeYCo, 5, up.Colors.red, 4))
        

    def gunMoveLeft(self):
        self.gun.moveLeft()
    
    def gunMoveRight(self):
        self.gun.moveRight()

    def paintBalls(self):
        for ball in self.balls:
            ball.updatePos()
            ball.paint()
        #ball.paintNameOnBall()

    def paintGun(self):
        if self.gun:
            self.gun.paint()
    
    def paintBullets(self):
        for bullet in self.bullets:
            bullet.updatePos()
            bullet.paint()
        # if not self.bullets:
        #     return 
        # #make a temp copy of bullets
        # updatedBullets = []
        # for bullet in self.bullets:
        #     bullet.updatePos()
        #     if not (self.hasCollidedWithUpperBoundary(bullet) or self.hasCollidedWithBall(bullet) ):
        #         updatedBullets.append(bullet)
        #         bullet.paint()
        # #update bullet list
        # self.bullets = updatedBullets
    def hasBulletCollidedWithBall(self, bullet):
            for ball in self.balls:
                if up.Maths.isPointInsideCircle(bullet.x, bullet.y,ball.x_coordinate, ball.y_coordinate, ball.radius):
                    return True
                else:
                    return False

    def hasCollidedWithUpperBoundary(self, bullet):
        if bullet.y <= 0:
            return True
        else:
            return False

    def collisionHandler(self):
        """ This function detects colllosions and takes necessary actions."""
        bulletListCopy = []
        ballListCopy = []
        for bullet in self.bullets:
            isBulletDestoryed = False
            for index, ball in enumerate(self.balls):
                
                #check if any point of our (square shaped) bullet is inside circle or not. If any point is inside
                #circle then collosion has occurred.
                topLeftPoint = up.Maths.isPointInsideCircle(bullet.x, bullet.y,ball.x_coordinate, ball.y_coordinate, ball.radius)
                topRightPoint = up.Maths.isPointInsideCircle(bullet.x + bullet.size, bullet.y,ball.x_coordinate, ball.y_coordinate, ball.radius)
                bottomLeftPoint = up.Maths.isPointInsideCircle(bullet.x, bullet.y + bullet.size,ball.x_coordinate, ball.y_coordinate, ball.radius)
                bottomRightPoint = up.Maths.isPointInsideCircle(bullet.x + bullet.size, bullet.y,ball.x_coordinate, ball.y_coordinate, ball.radius)

                if not(topLeftPoint or topRightPoint or bottomLeftPoint or bottomRightPoint): #collision has not occurred
                    ballListCopy.append(ball)
                else:
                    #pop up sound as some ball is also destroyed.
                    py.mixer.Sound.play(ball_pop_sound)
                    isBulletDestoryed = True
                    
                    #need to copy remaining balls
                    for i in range(index+1, len(self.balls)):
                        ballListCopy.append(self.balls[i])
                    break
            if not isBulletDestoryed:
                bulletListCopy.append(bullet)

            self.balls = ballListCopy.copy()
            ballListCopy.clear()


        self.bullets = bulletListCopy
        
        
        


game = ShootingGame()
while not animationExit:
    for event in py.event.get():
        if event.type == py.QUIT:
            animationExit = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_x:
                game.gunFired()

        #if event.type == py.KEYDOWN:
    if py.key.get_pressed()[py.K_LEFT] == True:
        game.gunMoveLeft()
    elif py.key.get_pressed()[py.K_RIGHT] == True:
        game.gunMoveRight()
    # if py.key.get_pressed()[py.K_x] == True:
    #     game.gunFired()
    gameDisplay.fill(up.Colors.black)
    game.collisionHandler()
    game.paintBalls()
    game.paintGun()
    game.paintBullets()
    py.display.update()
    time.sleep(0.01)
    py.event.pump()

py.quit()
