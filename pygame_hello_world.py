import pygame,sys,os
from pygame.locals import* #load constant

red = [255,0,0]

# Initialize Pygame
pygame.init()

# Set Up Windows

Windows=pygame.display.set_mode((1000,600))
pygame.display.set_caption('Slither.eat-The Snack Game')

# set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
    print("Slither.eat - The snake game!")
    pass