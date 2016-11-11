import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Creates the screen
WIDTH = 1000
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Loads the image
Bridge = pygame.image.load('Bridge.jpg')
Bridge = pygame.transform.scale(Bridge, (WIDTH, HEIGHT))
Wreckage = pygame.image.load('Wreckage.jpg')
Wreckage = pygame.transform.scale(Wreckage, (WIDTH, HEIGHT))
Biodome = pygame.image.load('Biodome.jpg')
Biodome = pygame.transform.scale(Biodome, (WIDTH, HEIGHT))

# Makes the image darker by dividing the pixels by 3
def Darker(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (Red/3, Green/3, Blue/3)

# # Makes the image lighter by multiplying the pixels by 3
def Lighter(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            if Red < 86 and Green < 86 and Blue < 86:
                pxarray[X, Y] = (Red*3, Green*3, Blue*3)

# Makes the lights turn off (go dark)
def BridgeLights(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            # If the rgb values are all above 150 divide them by 3. This makes the light areas darker.
            if Red > 150 and Green > 150 and Blue > 150:
                pxarray[X, Y] = (Red/3, Green/3, Blue/3)

# Makes the bridge slightly darker
def BridgeLightsEffect(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            if 100 > Red > 10 and 100 > Green > 10 and 100 > Blue > 10:
                # - 10 from each rgb value to make it slightly darker
                pxarray[X, Y] = (Red - 10, Green - 10, Blue - 10)

# blits the images to the screen
def drawBridge():
    screen.blit(Bridge, [0, 0])

def drawWreckage():
    screen.blit(Wreckage, [0, 0])

def drawBiodome():
    screen.blit(Biodome, [0, 0])
    pygame.display.flip()
    Biodome.set_alpha(alpha)

# status of bridge lights
status = 1
on = 1
off = 0

# Setting different transparency values
alpha = 255
alpha0 = 255
alpha1 = 210
alpha2 = 170
alpha3 = 130
alpha4 = 90
alpha5 = 50

# Setting different background colours
BackColour = (255, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 188, 255)
BLACK = (0, 0, 0)
colour1 = (5, 255, 43)
colour2 = (242, 252, 45)
colour3 = (247, 27, 247)

# Wreckage image functions

updates = 0

def darkenAll(n):
    updates = n
    for y in xrange(1, HEIGHT - 1):
        for x in xrange(1, WIDTH - 1):
            if updates <= 10:
                    darkenPixel(x, y, updates)
            else:
                newUpdates = (20 - updates)
                redUpdates = (updates - 10)
                darkenPixel(x, y, newUpdates)
                reddenPixel(x, y, redUpdates)

def darkenPixel(x, y, n):
    darkenAmount = 10 * n
    red = screen.get_at((x, y)).r
    green = screen.get_at((x, y)).g
    blue = screen.get_at((x, y)).b
    if red > darkenAmount:
        red -= darkenAmount
    if green > darkenAmount:
        green -= darkenAmount
    if blue > darkenAmount:
        blue -= darkenAmount
    screen.set_at((x, y), (red, green, blue))

def reddenPixel(x, y, n):
    Amount = 10 * n
    Limit = 255 - Amount
    red = screen.get_at((x, y)).r
    green = screen.get_at((x, y)).g
    blue = screen.get_at((x, y)).b
    if red <= Limit:
        red += Amount
    screen.set_at((x, y), (red, green, blue))

def alienTorch():
    (mousePosX, mousePosY) = pygame.mouse.get_pos()
    torchRadius = 40
    for y in xrange(1, HEIGHT - 1):
        for x in xrange(1, WIDTH - 1):
            if ((x - mousePosX)**2 + (y - mousePosY)**2) <= (torchRadius**2):
                screen.set_at((x, y),(Wreckage.get_at((x, y))))

while True:
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_1]:
        # Resets alpha to 255 (no transparency)
        alpha = 255
        drawBiodome()
    if key_pressed[K_2]:
        drawBridge()
    if key_pressed[K_3]:
        drawWreckage()

    pxarray = pygame.PixelArray(screen)

    # Resets the bridge image
    if key_pressed[K_SPACE]:
        # deletes pxarray to unlock the surface
        del pxarray
        drawBridge()
        pxarray = pygame.PixelArray(screen)
    if key_pressed[K_DOWN]:
        Darker(Bridge)
    if key_pressed[K_UP]:
        Lighter(Bridge)

    # Hold down right to flicker lights on bridge
    if key_pressed[K_RIGHT]:
        if status == on:
            status = off
            del pxarray
            drawBridge()
            pxarray = pygame.PixelArray(screen)
            clock.tick(5)
        elif status == off:
            status = on
            BridgeLights(Bridge)
            BridgeLightsEffect(Bridge)
            clock.tick(5)

    del pxarray

    if key_pressed[K_4]:
        clock.tick(60)
        screen.blit(Wreckage, (0, 0))
        updates += 1
        darkenAll(updates)
        alienTorch()

    if key_pressed[pygame.K_a]:
        # Selects a random alpha variable and draws biodome with new alpha value
        if alpha == alpha0:
            alpha = random.choice([alpha4, alpha3, alpha2, alpha1, alpha5])
        elif alpha == alpha1:
            alpha = random.choice([alpha4, alpha3, alpha2, alpha0, alpha5])
        elif alpha == alpha2:
            alpha = random.choice([alpha4, alpha3, alpha0, alpha1, alpha5])
        elif alpha == alpha3:
            alpha = random.choice([alpha4, alpha0, alpha2, alpha1, alpha5])
        elif alpha == alpha4:
            alpha = random.choice([alpha0, alpha3, alpha2, alpha1, alpha5])
        elif alpha == alpha5:
            alpha = random.choice([alpha0, alpha3, alpha2, alpha1, alpha4])
        drawBiodome()

        # Selects a random background colour and fills the screen with it.
        if BackColour == WHITE:
            BackColour = random.choice([RED, BLACK, BLUE, colour1, colour2, colour3])
        elif BackColour == RED:
            BackColour = random.choice([WHITE, BLACK, BLUE, colour1, colour2, colour3])
        elif BackColour == BLUE:
            BackColour = random.choice([WHITE, BLACK, WHITE, colour1, colour2, colour3])
        elif BackColour == BLACK:
            BackColour = random.choice([WHITE, WHITE, BLUE, colour1, colour2, colour3])
        elif BackColour == colour1:
            BackColour = random.choice([WHITE, BLACK, BLUE, RED, colour2, colour3])
        elif BackColour == colour2:
            BackColour = random.choice([WHITE, BLACK, WHITE, colour1, BLUE, colour3])
        elif BackColour == colour3:
            BackColour = random.choice([WHITE, WHITE, BLUE, colour1, colour2, BLACK])
        screen.fill((BackColour))
        # changes how frequently the colours and transparency changes
        clock.tick(6)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            exit()