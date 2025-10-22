# ==========================================
# file: entities/zombie.py
# ==========================================
import pygame as pg


RED=(220,60,60)


class Zombie(pg.sprite.Sprite):
    def __init__(self, x, y, tier=0, base_speed=1.2, base_hp=3):
        super().__init__()
        self.rect = pg.Rect(x, y, 40, 60)
        self.vx = 0.0; self.vy = 0.0
        self.base_speed = base_speed + 0.15 * tier
        self.hp = base_hp + 1 * tier
        self.damage = 1 + (tier // 2)
        self.touch_cooldown = 0
        self.score_worth = 10 + 5 * tier


    def update_ai(self, player, ground_y):
        dirx = 1 if player.rect.x > self.rect.x else -1
        self.vx = dirx * self.base_speed
        self.vy += 0.7 # gravity constant; keep in sync with settings if needed
        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.vy = 0
        if self.touch_cooldown > 0:
            self.touch_cooldown -= 1
        if self.rect.colliderect(player.rect) and self.touch_cooldown == 0 and not player.dead:
            if player.invuln == 0:
                player.health -= self.damage
                player.invuln = 40
            self.touch_cooldown = 40

    def draw(self, surf, cam):
        pg.draw.rect(surf, (100, 180, 100), (self.rect.x - cam.x, self.rect.y, self.rect.w, self.rect.h), border_radius=6)
        for i in range(self.hp):
            pg.draw.rect(surf, RED, (self.rect.x - cam.x + 5 + i*8, self.rect.y - 8, 6, 4))