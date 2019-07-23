import pygame
pygame.init()
yes = True
w = pygame.display.set_mode([700,700])
cookies = 0
while yes:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yes = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x <= 950 and x >= 50:
                    if y <= 950 and y >= 50:
                        cookies += 1
                        print(cookies)
    w.fill((0, 0, 255))
    pygame.draw.polygon(w,(244,116,0),[(50,50),(650,50),(650,650),(50,650)])
    pygame.display.flip()
