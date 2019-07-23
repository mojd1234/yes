import random
import pygame
pygame.init()
scrninf = pygame.display.Info()
w = pygame.display.set_mode((900,800))
w.fill((0,0,0))
speed = 15
ballxspeed = speed
ballyspeed = speed
ballx = 0
bally = 0
yes = 0
while yes < 1000:
    #w.fill((0, 0, 0))
    red = random.randint(1,255)
    green = random.randint(1,255)
    blue = random.randint(1,255)
    ballx += ballxspeed
    bally += ballyspeed
    if bally >= 790:
        ballyspeed *= -1
    if bally <= 10:
        ballyspeed *= -1
    pygame.draw.circle(w,(255,255,255),(ballx,bally),3)
    pygame.draw.circle(w,(red,green,blue),(ballx,bally),2)
    if ballx >= 890 or ballx <= 10:
        ballxspeed *= -1
    pygame.display.flip()
    pygame.time.wait(1)