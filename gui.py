import numpy as np
from itertools import compress
import copy
import pygame
from classes import *


# VARIABLES
# ------------------------------------------------------------------------------------------------

# colours
black = (0,0,0)
white = (255,255,255)
blue = (0,128,255)
yellow = (255,255,0)
red = (255,0,0)

# coords
width = 320
height = 400
board_coords = [20, 20, 280, 280]   # [x, y, width, height]
col1_x = 20 + int(280/8)
col2_x = 20 + int(280/8)*3
col3_x = 20 + int(280/8)*5
col4_x = 20 + int(280/8)*7
col_y = [20 + int(280/8)*7, 20 + int(280/8)*5, 20 + int(280/8)*3, 20 + int(280/8)]
col1_button_coords = [20+0*(280/4)+4,310,280/4-8,30]
col2_button_coords = [20+1*(280/4)+4,310,280/4-8,30]
col3_button_coords = [20+2*(280/4)+4,310,280/4-8,30]
col4_button_coords = [20+3*(280/4)+4,310,280/4-8,30]

# ------------------------------------------------------------------------------------------------


# GUI FUNCTIONS
# ------------------------------------------------------------------------------------------------

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def draw_board(screen):
    board = pygame.draw.rect(screen, blue, board_coords)
    # col1
    for i in range(4):
        pygame.draw.circle(screen, black, [col1_x, col_y[i]], 30)
    # col2
    for i in range(4):
        pygame.draw.circle(screen, black, [col2_x, col_y[i]], 30)
    # col3
    for i in range(4):
        pygame.draw.circle(screen, black, [col3_x, col_y[i]], 30)
    # col4
    for i in range(4):
        pygame.draw.circle(screen, black, [col4_x, col_y[i]], 30)


def buttons(screen, mouse):
    def button_text(center_x, center_y):
        button_text = pygame.font.Font('freesansbold.ttf', 10)
        textSurf, textRect = text_objects('DROP', button_text)
        textRect.center = (center_x, center_y)
        screen.blit(textSurf, textRect)
    # button 1
    if (col1_button_coords[0] < mouse[0] < col2_button_coords[0]) and (310 < mouse[1] < 340):
        col1_button = pygame.draw.rect(screen, red, col1_button_coords)
    else:
        col1_button = pygame.draw.rect(screen, blue, col1_button_coords)
    button_text(col1_button_coords[0]+col1_button_coords[2]/2, 325)
    # button 2
    if (col2_button_coords[0] < mouse[0] < col3_button_coords[0]) and (310 < mouse[1] < 340):
        col2_button = pygame.draw.rect(screen, red, col2_button_coords)
    else:
        col2_button = pygame.draw.rect(screen, blue, col2_button_coords)
    button_text(col2_button_coords[0]+col2_button_coords[2]/2, 325)
    # button 3
    if (col3_button_coords[0] < mouse[0] < col4_button_coords[0]) and (310 < mouse[1] < 340):
        col3_button = pygame.draw.rect(screen, red, col3_button_coords)
    else:
        col3_button = pygame.draw.rect(screen, blue, col3_button_coords)
    button_text(col3_button_coords[0]+col3_button_coords[2]/2, 325)
    # button 4
    if (col4_button_coords[0] < mouse[0] < 300-4) and (310 < mouse[1] < 340):
        col4_button = pygame.draw.rect(screen, red, col4_button_coords)
    else:
        col4_button = pygame.draw.rect(screen, blue, col4_button_coords)
    button_text(col4_button_coords[0]+col4_button_coords[2]/2, 325)

# ------------------------------------------------------------------------------------------------


# MAIN LOOP
# ------------------------------------------------------------------------------------------------

def main():
    pygame.init()   # initialize
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()


    running = True   # controls main loop
    # main loop
    while running:

        # event loop
        for event in pygame.event.get():

            # QUIT
            if event.type == pygame.QUIT:
                #pygame.display.quit()
                running = False

            # button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click')


        mouse = pygame.mouse.get_pos()

        draw_board(screen)
        buttons(screen, mouse)

        pygame.display.update()
        clock.tick(15)

# ------------------------------------------------------------------------------------------------
