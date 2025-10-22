import pygame as pg
from .base import Entity
from ..settings import GRAVITY, GROUND_Y
from ..assets import image

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 36, 54, image("player_skeleton.png", (36,54)))
        self.on_ground=False; self.facing=1
        self.speed=3.2; self.jump=12
        self.invuln=0; self.attack_cd=0
        self.health=self.max_health=10; self.score=0; self.dead=False

    def handle_input(self, keys):
        ax=0
        if keys.left: ax -= self.speed; self.facing=-1
        if keys.right: ax += self.speed; self.facing= 1
        if keys.jump and self.on_ground:
            self.vy = -self.jump; self.on_ground=False
        if keys.attack and self.attack_cd<=0: self.attack_cd=10
        self.vx = ax

    def attack_box(self):
        if self.attack_cd<=0: return None
        reach=28
        if self.facing>0: return pg.Rect(self.rect.right, self.rect.top+8, reach, self.rect.height-16)
        return pg.Rect(self.rect.left-reach, self.rect.top+8, reach, self.rect.height-16)

    def update(self, dt):
        self.vy += GRAVITY
        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)
        if self.rect.bottom>=GROUND_Y: self.rect.bottom=GROUND_Y; self.vy=0; self.on_ground=True
        else: self.on_ground=False
        self.attack_cd = max(0, self.attack_cd-1)
        self.invuln = max(0, self.invuln-1)
        if self.health<=0: self.dead=True
