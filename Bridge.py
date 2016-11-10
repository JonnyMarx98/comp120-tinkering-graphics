import pygame, sys
from pygame.locals import *

pygame.init()

#Create window
WIDTH = 1000
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#Background
Bridge = pygame.image.load('Bridge.jpg')
Bridge = pygame.transform.scale(Bridge, (WIDTH, HEIGHT))



def LightsOff(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (Red/3, Green/3, Blue/3)

def LightsOn(Bridge):
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            Red = screen.get_at((X, Y)).r
            Green = screen.get_at((X, Y)).g
            Blue = screen.get_at((X, Y)).b
            if Red < 86 and Green < 86 and Blue < 86:
                pxarray[X, Y] = (Red*3, Green*3, Blue*3)

screen.blit(Bridge, [0, 0])
for Y in xrange(HEIGHT):
    for X in xrange(WIDTH):
        Red1 = screen.get_at((X, Y)).r
        Green1 = screen.get_at((X, Y)).g
        Blue1 = screen.get_at((X, Y)).b

def resetBridge():
    screen.blit(Bridge, [0, 0])


while True:
    keys_pressed = pygame.key.get_pressed()
    pxarray = pygame.PixelArray(screen)

    if keys_pressed[K_SPACE]:
        del pxarray
        resetBridge()
        pxarray = pygame.PixelArray(screen)
    if keys_pressed[K_DOWN]:
        LightsOff(Bridge)
    if keys_pressed[K_UP]:
        LightsOn(Bridge)

    del pxarray
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            sys.exit()