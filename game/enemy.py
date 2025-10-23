import pygame
from .config import RED, GREEN

class Enemy:
    def __init__(self, x=500, y=300):
        self.max_health = 30
        self.health = self.max_health
        self.x = x
        self.y = y
        self.image = pygame.Surface((80, 80))
        self.image.fill(RED)

    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        bar_width = 80 * (self.health / self.max_health)
        pygame.draw.rect(surface, GREEN, (self.x, self.y - 10, bar_width, 5))

    def is_defeated(self):
        return self.health <= 0
