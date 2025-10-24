# game/projectile.py
import pygame
import os
import math

from .config import SKULL


class SkullProjectile:
    def __init__(self, x, y):
        self.image = pygame.image.load(SKULL).convert_alpha()
        self.start_x = x
        self.start_y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10
        self.damage = 0
        self.arc_height = 80  # pixels high
        self.distance = 300  # pixels forward distance for full arc
        self.t = 0  # progress through the arc (0 to 1)

    def update(self):
        self.t += self.speed / self.distance
        if self.t >= 1:
            self.t = 1
        # Parabolic arc based on t
        new_x = self.start_x + self.t * self.distance
        peak = -4 * self.arc_height * (self.t - 0.5) ** 2 + self.arc_height
        new_y = self.start_y - peak
        self.rect.center = (new_x, new_y)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def off_screen(self, width):
        return self.rect.x > width or self.t >= 1

    def collides_with(self, target_rect):
        return self.rect.colliderect(target_rect)