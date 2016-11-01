
import pygame, sys, time, random, math
from pygame.locals import *

pygame.init()
pygame.mixer.init()



Width = 900
Height = 600
updates = 0

window = pygame.display.set_mode((Width, Height))

# Insert picture name to load below
picture = pygame.image.load('Wreckage.jpg')
picture = pygame.transform.scale(picture, (Width, Height))

window.blit(picture, (0, 0))




def darkenAll(n):
    updates = n
    for y in xrange(1, Height - 1):
        for x in xrange(1, Width - 1):
            if updates <= 10:
                    darkenPixel(x, y, updates)
            else:
                newUpdates = (20 - updates)
                redUpdates = (updates - 10)
                darkenPixel(x, y, newUpdates)
                reddenPixel(x, y, redUpdates)




def darkenPixel(x, y, n):
    darkenAmount = 10 * n
    red = window.get_at((x, y)).r
    green = window.get_at((x, y)).g
    blue = window.get_at((x, y)).b
    if red > darkenAmount:
        red -= darkenAmount
    if green > darkenAmount:
        green -= darkenAmount
    if blue > darkenAmount:
        blue -= darkenAmount
    window.set_at((x, y), (red, green, blue))

def reddenPixel(x, y, n):
    Amount = 10 * n
    Limit = 255 - Amount
    red = window.get_at((x, y)).r
    green = window.get_at((x, y)).g
    blue = window.get_at((x, y)).b
    if red <= Limit:
        red += Amount
    window.set_at((x, y), (red, green, blue))

def alienTorch():
    (mousePosX, mousePosY) = pygame.mouse.get_pos()
    torchRadius = 40
    for y in xrange(1, Height - 1):
        for x in xrange(1, Width - 1):
            if ((x - mousePosX)**2 + (y - mousePosY)**2) <= (torchRadius**2):
                window.set_at((x, y),(picture.get_at((x, y))))









while True:
    keys = pygame.key.get_pressed()
    px_array = pygame.PixelArray(window)
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    clock.tick(1)
    del px_array
    window.blit(picture, (0, 0))
    updates += 1
    darkenAll(updates)
    alienTorch()




    pygame.display.update()
