import pygame, sys, random, time, math, timeit
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 720
HEIGHT = 540

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sci-Fi Mood Board')
screen.fill((255, 255, 255))
pygame.display.update()

Bridge = pygame.image.load('Bridge.jpg')
imageRect = Bridge.get_rect()
Bridge = pygame.transform.scale(Bridge, (WIDTH, HEIGHT))

def drawBridge():
    screen.blit(Bridge, imageRect)
    pygame.display.flip()

MainLoop = True

while MainLoop is True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #esc key exits
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    drawBridge()