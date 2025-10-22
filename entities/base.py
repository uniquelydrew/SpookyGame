import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, img=None):
        super().__init__()
        self.image = img or pg.Surface((w, h), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vx = 0.0; self.vy = 0.0

    def update(self, dt:float):
        pass  # override
