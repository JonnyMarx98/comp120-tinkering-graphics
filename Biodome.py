import pygame, sys, random, time, math, timeit
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 720
HEIGHT = 540

# Sets screen resolution and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sci-Fi Mood Board')
screen.fill((255, 255, 255))
pygame.display.update()



#Loads image
Biodome = pygame.image.load('Biodome.jpg') #Image must be saved in same place as program
imageRect = Biodome.get_rect()


#Draws the image onto screen
def drawBiodome():
    screen.blit(Biodome, imageRect)
    pygame.display.flip()
    Biodome.set_alpha(alpha)

alpha = 250
alpha0 = 250
alpha1 = 175
alpha2 = 125
alpha3 = 75
alpha4 = 50
alpha5 = 20

BackColour = (255, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 188, 255)
BLACK = (0, 0, 0)
colour1 = (5, 255, 43)
colour2 = (242, 252, 45)
colour3 = (247, 27, 247)


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
                if event.key == pygame.K_1:
                    drawBiodome()
            #Selects a random alpha variable and draws biodome with new alpha value
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
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
        #Selects a random alpha variable and draws biodome with new alpha value (constantly while key is held)
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
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


clock.tick(1)
pygame.display.update()
