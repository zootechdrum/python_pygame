import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

#set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation For Cat")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

#Below sets code to play sounds
soundObj = pygame.mixer.Sound('ray_gun.wav')
soundObj.play()

catImg = pygame.image.load("cat.png")
catx = 10
caty = 10
direction = 'right'


#below sets text to the surface object. 
fontObj = pygame.font.Font("freesansbold.ttf",32)
textSurfaceObj = fontObj.render('Hello World', True, GREEN, BLUE)

textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

while True: # The main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            soundObj.play()

            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            soundObj.play()

    elif direction == "left":
        catx -= 5
        if catx == 10:
            direction ='up'
    elif direction == "up":
        caty -= 5
        if caty == 10:
            direction = 'right'
     # must be called in order for the image to stay on the screen
    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
#needs to be called once per each iteration of the loop
    fpsClock.tick(FPS)
