# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(0)
        pygame.display.flip()


if __name__ == "__main__":
    main() 