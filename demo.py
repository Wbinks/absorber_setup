from pygame_functions import *
import math, random, time, pickle

screenSize(1800,1000)
setBackgroundColour("black")
setAutoUpdate(False)

class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)
        self.angle = random.randint(1,360)
        
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, self.angle, self.size/100)
        showSprite(self.sprite)

    def move(self):
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        # change the x position and y position of this creature
        self.x = (self.x + xspeed) % 1800
        self.y = (self.y + yspeed) % 1000
        # move the sprite
        moveSprite(self.sprite,   self.x, self.y, centre=True)



creatures= [ ]
for i in range(10):
    creatures.append(Creature(random.randint(0,1000),random.randint(0,1000), "enemy.png", random.randint(10,200)))       


while True:
    for c in creatures:
        c.move()
    updateDisplay()
    tick(50)
endWait()