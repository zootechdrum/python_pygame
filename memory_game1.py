#Memory Puzzle
#By Cesar Gomez

import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8 #speed boxes' sliding speed
BOXSIZE = 40 #size of box height & width in pixels.
GAPSIZE = 10 #SIZE OF GAP BETWEEN BOXES IN PIXELS
BOARDWIDTH = 10
BOARDHEIGHT = 7 #Number of rown of icons

#USE AND ASSERT METHOD FOR EASY DEBUGGING THIS SHOULD ALWAYS RETURN TRUE OR ELSE
#SECONDS PARAMATER WILL BE DISPLAYED. 
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of pais of matches'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT- (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

GRAY =     (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE =    (255, 255, 255)
RED =      (255, 0, 0)
GREEN =    (0, 255, 0)
BLUE =     (0, 255, 0)
YELLOW =   (255, 255, 0)
ORANGE =   (255, 128, 0)
PURPLE =   (255, 0, 255)
CYAN =     (0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

#The below checks to see if we have enough color/shape combinations for the size of board.
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,"Board is too big fo the number of shapes/colors defined."

def main():
    global FPSCLOCK,DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.CLock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate the mouse event
    mousey = 0 # used to store y coordinate the mouse event
    pygame.display.set_caption("Memory Game")

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False) # passing false to this function covers up

    firstSelection = None # stores the (x, y) of the first box clicked.

    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey == event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True


        boxx, boxy = getBoxAtPixel(mousex, mousey)  #boxx and boxxy are equal to mouseX and mouseY
        if boxx != None and boxy != None:
            #the mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard,[(boxx,boxy)])
                revealedBoxes[boxx][boxy] = True #set the box as revealed

                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else: #the current box was the second box clicked
                      # Check if there is a match between the icons.
                      icon1shape, icone1color = getShapeAndColor(mainBoard, firstSelection[0],firstSelection[1])
                      icon2shape, icone2color = getShapeAndColor(mainBoard, boxx, boxy)

                      if icon1shape != icon2shape or icone1color != icone2color:
                        #icons don't match. Re-cover up both selections.

                        pygame.time.wait(1000) #1000 milliseconds = 1 sec
                        #firs
                        coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                      elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        #show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.wait(1000)

                        #Replay the start game animation
                        startGameAnimation(mainBoard)
                      firstSelection = None # reset firstSelection variable


        #Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )                        
             