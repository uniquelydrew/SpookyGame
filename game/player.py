import os
import sys

import pygame
from .config import WHITE, SKELETON


class Player:
    def __init__(self, x=200, y=400):
        self.image = pygame.image.load(SKELETON)
        # self.image = pygame.Surface((80, 80))
        # self.image.fill(WHITE)
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        return os.path.join(base_path, relative_path)