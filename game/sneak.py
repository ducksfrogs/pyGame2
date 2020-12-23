import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN,\
                        K_LEFT,K_RIGHT,K_UP,K_DOWN, Rect

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()


FOODS = []
SNAKE = []
(W,H) = (20,20)

def add_food():
    """set food at random """
    while True:
        pos = (random.randint(0,W-1), random.randint(0,H-1))
        if
