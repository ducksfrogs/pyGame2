import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE


pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()


def main():

    walls = 80
    ship_y = 250
    velocity = 0
    score = 0
    slope = randint(1,6)
    sysfont = pygame.font.SysFont(None, 36)
    Ship_image = pygame.image.load('ship.png')
    bang_image = pygame.image.load('bang.png')
