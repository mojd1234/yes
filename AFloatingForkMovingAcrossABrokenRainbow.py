import pygame
import random
pygame.init()
scrninf = pygame.display.Info()
w = pygame.display.set_mode([scrninf.current_w,scrninf.current_h])
c = pygame.time.Clock()
fork_var = pygame.image.load("goodfork.png")
fork_var = pygame.transform.scale(fork_var,(100,100))
fork_rect = fork_var.get_rect()
speed = 100
fork_speed = pygame.math.Vector2(speed,speed)
def main():
    r = 0
    g = 0
    b = 0
    yes = True
    while yes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yes = False
        pygame.event.pump()
        c.tick(60)
        shmooving()
        #r = random.randint(0,255)
        #g = random.randint(0,255)
        #b = random.randint(0,255)
        w.fill((r,g,b))
        w.blit(fork_var, fork_rect)
        pygame.display.flip()
def shmooving():
    width = scrninf.current_w
    height = scrninf.current_h
    if fork_rect.right > width:
        fork_speed.x *= -1
    if fork_rect.left < 0:
        fork_speed.x *= -1
    if fork_rect.bottom > height:
        fork_speed.y *= -1
    if fork_rect.top < 0:
        fork_speed.y *= -1
    fork_rect.move_ip(fork_speed)
if __name__ == "__main__":
    main()