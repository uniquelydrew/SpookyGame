# game/player.py
import pygame
from .config import SKELETON

class Player:
    """
    Represents the player character (the skeleton).
    Handles sprite loading, position, and drawing.
    """
    image: pygame.Surface
    rect: pygame.Rect
    speed: float
    health: int

    def __init__(self):
        self.image = pygame.image.load(SKELETON).convert_alpha()
        self.rect = self.image.get_rect(center=(400, 500))
        self.speed = 5
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        self.rect.x = max(0, min(self.rect.x + dx, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + dy, 600 - self.rect.height))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect.topleft)
