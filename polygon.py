import pygame, sys
from pygame.locals import *

#Sets the background size and the bit color to 32
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Draw on this bitch")

WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0, 0, 0)


#colors the background to white. 
DISPLAYSURF.fill(WHITE)

pygame.draw.polygon(DISPLAYSURF, GREEN, ((144,0), (291,106), (236,277),(56,277),(0,106),1))
#sets individual pixels to the color black on the screen.
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[10][40] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()