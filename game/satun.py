import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT,\
                        K_DOWN, K_UP

pygame.init()
SURFACE = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()

def main():
    game_over = False
    score = 0
    speed = 25
    stars = []
    keymap = []
    
