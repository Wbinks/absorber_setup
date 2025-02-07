from pygame_functions import *
import math, random, time, pickle

SCREEN_MAX_X = 10000
SCREEN_MAX_Y = 10000
screenSize(1800,900)
setBackgroundColour("black")
setAutoUpdate(False)

#die = makeSound("thump.mp3")

class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.speed = random.randint(4,8)
        self.angle = random.randint(1,360)
        
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, self.angle, self.size/100)
        showSprite(self.sprite)

    def move(self,player):
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        # change the x position and y position of this creature
        self.x = (self.x + xspeed) % SCREEN_MAX_X
        self.y = (self.y + yspeed) % SCREEN_MAX_Y
        # move the sprite
        
        moveSprite(self.sprite, 900+(self.x - player.x),450+(self.y-player.y) , centre=True)


class Player(Creature):
    def __init__(self,x,y,image, size):
        super().__init__(x,y,image, size)
        moveSprite(self.sprite,   900, 450, centre=True)
        self.invulnerable = True
        self.invulnerable_period = 3000
        self.start = clock()
    def move(self, creatures):
        # work out the angle from the player to the mouse
        dx = mouseX() - 900
        dy = mouseY() - 450
        dist = math.sqrt(dx**2 + dy**2)
        self.speed = dist /400 * 10
        self.angle = math.degrees(math.atan2(dy, dx))
        transformSprite(self.sprite, self.angle, self.size/100)
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        # change the x position and y position of this creature
        self.x = (self.x + xspeed) % SCREEN_MAX_X
        self.y = (self.y + yspeed) % SCREEN_MAX_Y
       
        if self.invulnerable and clock()-self.start >= self.invulnerable_period:
            self.invulnerable = False

        for c in creatures:
            if touching(self.sprite, c.sprite):
                if self.size > c.size:
                    print("Nom")
                    creatures.remove(c)
                    hideSprite(c.sprite)
                    self.size += 5

                elif self.invulnerable == True:
                    pass
                elif self.size < c.size:
                    return False
        return True

creatures= [ ]
for i in range(100):
    creatures.append(Creature(random.randint(0,10000),random.randint(0,10000), "enemy.png", random.randint(5,50)))       

p = Player(5000,5000,"player.png",20)

def drawBoundary(player):
    clearShapes()
    drawRect(900-player.x,450-player.y, SCREEN_MAX_X,SCREEN_MAX_Y, (0,0,40),0)
    drawRect(900-player.x,450-player.y, SCREEN_MAX_X,SCREEN_MAX_Y, (255,255,255),5)
while True:
    for c in creatures:
        c.move(p)
    alive = p.move(creatures)
    if not alive:
        break
    p.move(creatures)
    drawBoundary(p)
    updateDisplay()
    tick(20)
endWait()
