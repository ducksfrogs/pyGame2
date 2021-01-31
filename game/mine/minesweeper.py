import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN


WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.pygame.time.Clock()

def num_of_bomb(field, x_pos,y_pos):
    count = 0
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset,y_pos + yoffset)
            if  <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count

def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset, y_pos +yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos <HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and not(xpos ==x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)

def main():
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!", True, (0,255,255))
    message_over = largefont.render("Game over!!", True, (0,255,255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    game_over = False

    filed = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]


    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0,WIDTH-1), randint(0, HEIGHT-1)
