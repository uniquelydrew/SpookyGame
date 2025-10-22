# ==========================================
# file: entities/pumpkin.py
# ==========================================
import pygame as pg


ORANGE=(240,150,40)


class Pumpkin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pg.Rect(x, y, 28, 28)
        self.hp = 2
        self.heal_amount = 3


    def draw(self, surf, cam):
        pg.draw.ellipse(surf, ORANGE, (self.rect.x - cam.x, self.rect.y, self.rect.w, self.rect.h))
        pg.draw.rect(surf, (60, 120, 60), (self.rect.centerx - cam.x - 2, self.rect.y - 6, 4, 8))