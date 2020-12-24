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

    holes = []
    for xpo in range(walls):
        in_space_down = False
        for event in pygame.event.get()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key ==K_SPACE:
                    in_space_down = True

    edge = holes[-1].copy()
    test = edge.move(0, slope)
    if test.top <= 0 or test.bottom >= 600:
        slope = randint(1,6) *(-1 if slope > 0 else 1)