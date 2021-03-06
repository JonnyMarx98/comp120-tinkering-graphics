import pygame
from pygame.locals import *
import sys
import random

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Creates the screen
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Loads the image
bridge = pygame.image.load('images/Bridge.jpg')
# Scales image to fit screen
bridge = pygame.transform.scale(bridge, (WIDTH, HEIGHT))
wreckage = pygame.image.load('images/wreckage.jpg')
wreckage = pygame.transform.scale(wreckage, (WIDTH, HEIGHT))
biodome = pygame.image.load('images/biodome.jpg')
biodome = pygame.transform.scale(biodome, (WIDTH, HEIGHT))


def darker():
    """Makes the image darker by dividing the pixels by 3"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            pxarray[X, Y] = (red/3, green/3, blue/3)


def lighter():
    """Makes the image lighter"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            if red < 86 and green < 86 and blue < 86:
                pxarray[X, Y] = (red*3, green*3, blue*3)


def invert():
    """inverts the image colours"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            red = 255 - red
            green = 255 - green
            blue = 255 - blue
            pxarray[X, Y] = (red, green, blue)


def greyscale():
    """converts the image to greyscale"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            grey = (red + green + blue)/3
            pxarray[X, Y] = (grey, grey, grey)


def bridge_lights():
    """Makes the lights turn off (go dark)"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            if red > 150 and green > 150 and blue > 150:
                pxarray[X, Y] = (red/3, green/3, blue/3)


def bridge_lights_red():
    """Makes the lights red"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            if red > 150 and green > 150 and blue > 150:
                red = red
                green /= 2
                blue /= 2
                pxarray[X, Y] = (red, green, blue)


def bridge_lights_red_effect():
    """Makes the bridge more"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            if 120 > red > 15 and 100 > green > 15 and 100 > blue > 15:
                # - 10 from each rgb value to make it slightly darker

                pxarray[X, Y] = (red + 35, green - 15, blue - 15)



def bridge_lights_effect():
    """Makes the bridge slightly darker"""
    for Y in xrange(HEIGHT):
        for X in xrange(WIDTH):
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            if 100 > red > 15 and 100 > green > 15 and 100 > blue > 15:
                # - 10 from each rgb value to make it slightly darker
                pxarray[X, Y] = (red - 15, green - 15, blue - 15)


def draw_bridge():
    """blits the images to the screen"""
    screen.blit(bridge, [0, 0])
    bridge.set_alpha(alpha)


def draw_wreckage():
    screen.blit(wreckage, [0, 0])
    wreckage.set_alpha(alpha)


def draw_biodome():
    screen.blit(biodome, [0, 0])
    biodome.set_alpha(alpha)


# status of bridge lights (on)
status = 1

# Setting different transparency values
alpha = 255
alphas = [255, 210, 170, 130, 100, 75]

# Setting different background colours
back_colour = (255, 255, 255)
back_colours = [(255, 255, 255), (255, 0, 0), (0, 188, 255), (0, 0, 0), (5, 255, 43), (242, 252, 45), (247, 27, 247)]

# wreckage image functions

updates = 0


def darken_all(n):
    update = n
    for y in xrange(1, HEIGHT - 1):
        for x in xrange(1, WIDTH - 1):
            if update <= 10:
                    darken_pixel(x, y, update)
            else:
                new_updates = (20 - update)
                red_updates = (updates - 10)
                darken_pixel(x, y, new_updates)
                redden_pixel(x, y, red_updates)


def darken_pixel(x, y, n):
    darken_amount = 10 * n
    red = screen.get_at((x, y)).r
    green = screen.get_at((x, y)).g
    blue = screen.get_at((x, y)).b
    if red > darken_amount:
        red -= darken_amount
    if green > darken_amount:
        green -= darken_amount
    if blue > darken_amount:
        blue -= darken_amount
    screen.set_at((x, y), (red, green, blue))


def redden_pixel(x, y, n):
    amount = 10 * n
    limit = 255 - amount
    red = screen.get_at((x, y)).r
    green = screen.get_at((x, y)).g
    blue = screen.get_at((x, y)).b
    if red <= limit:
        red += amount
    screen.set_at((x, y), (red, green, blue))


def alien_torch():
    (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
    torch_radius = 40
    for y in xrange(1, HEIGHT - 1):
        for x in xrange(1, WIDTH - 1):
            if ((x - mouse_pos_x)**2 + (y - mouse_pos_y)**2) <= (torch_radius**2):
                screen.set_at((x, y), (wreckage.get_at((x, y))))


# Main loop
while True:
    key_pressed = pygame.key.get_pressed()

    # Press 1, 2, and 3 to display each image
    if key_pressed[pygame.K_1]:
        # Resets alpha to 255 (no transparency)
        alpha = 255
        draw_biodome()
    if key_pressed[K_2]:
        alpha = 255
        draw_bridge()
    if key_pressed[K_3]:
        alpha = 255
        draw_wreckage()

    pxarray = pygame.PixelArray(screen)

    # Resets the bridge image
    if key_pressed[K_SPACE]:
        # deletes pxarray to unlock the surface
        del pxarray
        draw_bridge()
        pxarray = pygame.PixelArray(screen)

    # Press/hold down to make image darker
    if key_pressed[K_DOWN]:
        darker()

    # Press/hold down to make image lighter
    if key_pressed[K_UP]:
        lighter()

    # Hold down right to flicker lights on bridge
    if key_pressed[K_RIGHT]:
        if status == 1:
            status = 0
            del pxarray
            draw_bridge()
            pxarray = pygame.PixelArray(screen)
            clock.tick(4)
        elif status == 0:
            status = 1
            bridge_lights()
            bridge_lights_effect()
            clock.tick(25)

    # Hold down left to flicker red lights on bridge
    if key_pressed[K_LEFT]:
        if status == 1:
            status = 0
            del pxarray
            draw_bridge()
            pxarray = pygame.PixelArray(screen)
            clock.tick(4)
        elif status == 0:
            status = 1
            bridge_lights_red()
            bridge_lights_red_effect()
            clock.tick(25)

    # Press i to invert image colours, press i again to undo invert effect
    if key_pressed[pygame.K_i]:
        invert()

    # Press g to convert image to greyscale
    if key_pressed[pygame.K_g]:
        greyscale()

    del pxarray

    # Hold down 4 to see wreckage effect and use alien torch
    if key_pressed[K_4]:
        clock.tick(60)
        screen.blit(wreckage, (0, 0))
        updates += 1
        darken_all(updates)
        alien_torch()

    # Hold down a to see flashing effect on biodome
    if key_pressed[pygame.K_a]:
        # Selects a random background colour and fills the screen with it.
        back_colour = random.choice(back_colours)
        screen.fill(back_colour)
        # Selects a random alpha variable and draws biodome with new alpha value
        alpha = random.choice(alphas)
        draw_biodome()
        # changes how frequently the colours and transparency changes
        clock.tick(5)

    # Hold down a to see flashing effect on bridge
    if key_pressed[pygame.K_s]:
        back_colour = random.choice(back_colours)
        screen.fill(back_colour)
        alpha = random.choice(alphas)
        draw_bridge()
        clock.tick(5)

    # Hold down a to see flashing effect on wreckage
    if key_pressed[pygame.K_d]:
        back_colour = random.choice(back_colours)
        screen.fill(back_colour)
        alpha = random.choice(alphas)
        draw_wreckage()
        clock.tick(5)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Press esc to exit
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()