import pygame
import random
pygame.init()
w = pygame.display.set_mode([1000,1000])
while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    w.fill((r,g,b))
    pygame.display.flip()