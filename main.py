import pygame, sys, random, time
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

#Sets screen resolution and caption
screen = pygame.display.set_mode((720, 540))
pygame.display.set_caption('Sci-Fi Mood Board')

#Loads image
Biodome = pygame.image.load('C:\Users\JM190359\PycharmProjects\TinkeringGraphicsAssignment\Images\Biodome.jpg')
imageRect = Biodome.get_rect()

#Draws the image onto screen
def drawBiodome():
    screen.blit(Biodome, imageRect)
    pygame.display.flip()
    Biodome.set_alpha(alpha)

alpha = 250
alpha1 = 100
alpha2 = 150
alpha3 = 200
alpha4 = 50

clock = pygame.time.Clock()


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
            #draws biodome
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drawBiodome()
            #Selects a random alpha variable and draws biodome with new alpha value
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    alpha = random.choice([alpha4, alpha3, alpha2, alpha1])
                    drawBiodome()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    alpha = 200
                    drawBiodome()
            #sets background colour to white
            screen.fill((255, 255, 255))


pygame.display.update()
