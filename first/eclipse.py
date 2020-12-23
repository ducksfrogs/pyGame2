import sys
import pygame
from pygame.locals import QUIT, Rect


pygame.init()
SURFACE = pygame.display.set_mode((400,250))
FPSCLOCK = pygame.time.Clock()


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        pygame.draw.ellipse(SURFACE, (255,0,0), (50,50,140,60))
        pygame.draw.ellipse(SURFACE, (255,0,0))
