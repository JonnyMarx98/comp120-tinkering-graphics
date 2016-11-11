import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

# Creates the screen
WIDTH = 1000
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Loads the image
Bridge = pygame.image.load('Bridge.jpg')
Bridge = pygame.transform.scale(Bridge, (WIDTH, HEIGHT))


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

def BridgeLightsEffect(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            if 100 > Red > 10 and 100 > Green > 10 and 100 > Blue > 10:
                # - 10 from each rgb value to make it slightly darker
                pxarray[X, Y] = (Red - 10, Green - 10, Blue - 10)

# blits the image to the screen
screen.blit(Bridge, [0, 0])

# Resets the image
def resetBridge():
    screen.blit(Bridge, [0, 0])

# status of bridge lights
status = 1
on = 1
off = 0

while True:
    keys_pressed = pygame.key.get_pressed()
    pxarray = pygame.PixelArray(screen)

    if keys_pressed[K_SPACE]:
        # deletes pxarray to unlock the surface
        del pxarray
        resetBridge()
        pxarray = pygame.PixelArray(screen)
    if keys_pressed[K_DOWN]:
        Darker(Bridge)
    if keys_pressed[K_UP]:
        Lighter(Bridge)

    # Hold down right to flicker lights
    if keys_pressed[K_RIGHT]:
        if status == on:
            status = off
            del pxarray
            resetBridge()
            pxarray = pygame.PixelArray(screen)
            clock.tick(5)
        elif status == off:
            status = on
            BridgeLights(Bridge)
            BridgeLightsEffect(Bridge)
            clock.tick(5)

    del pxarray
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            exit()

#clock.tick(5)