import numpy as np
import pygame
import pygame_gui
import matplotlib.pyplot as plt
import math
from helpers import *

pygame.init()





def main():
    # setup
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1600, 900))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()
        # fps limit
        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()


