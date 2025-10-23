import pygame
from .config import WHITE

class Player:
    def __init__(self, x=200, y=300):
        self.image = pygame.Surface((80, 80))
        self.image.fill(WHITE)
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
