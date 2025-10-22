# ==========================================
# file: world/world.py
# ==========================================
import random
import pygame as pg
from dataclasses import dataclass


from utils import clamp


# soft dependencies on settings; values can be injected from game
@dataclass
class WorldSettings:
    world_len: int
    ground_y: int
    spawn_density: float
    pumpkin_density: float
    zombie_scale_per_1000px: float


class World:
    def __init__(self, settings: WorldSettings, rng: random.Random, ZombieCls, PumpkinCls):
        self.s = settings
        self.rng = rng
        self.graves: list[pg.Rect] = []
        self.zombies = pg.sprite.Group()
        self.pumpkins = pg.sprite.Group()
        self.ZombieCls = ZombieCls
        self.PumpkinCls = PumpkinCls
        self.generate()


    def level_tier_at(self, x: int) -> int:
        return int((x // 1000) * self.s.zombie_scale_per_1000px * 3)


    def generate(self):
        # graves (decor)
        for _ in range(200):
            gx = self.rng.randint(0, self.s.world_len - 30)
            gy = self.s.ground_y - 40 - self.rng.randint(0, 20)
            w, h = self.rng.randint(16, 32), self.rng.randint(24, 48)
            self.graves.append(pg.Rect(gx, gy, w, h))
        # enemies & pumpkins
        x = 300
        while x < self.s.world_len - 200:
            if self.rng.random() < self.s.spawn_density * 50:
                tier = self.level_tier_at(x) + self.rng.randint(0, 1)
                self.zombies.add(self.ZombieCls(x, self.s.ground_y - 60, tier))
            if self.rng.random() < self.s.pumpkin_density * 50:
                self.pumpkins.add(self.PumpkinCls(x + self.rng.randint(-20, 20), self.s.ground_y - 28))
            x += self.rng.randint(30, 80)

    # --- update/draw ---
    def update(self, player):
        # Enemies AI
        for z in self.zombies:
            z.update_ai(player, self.s.ground_y)
        # Attack interactions
        ab = player.attack_box()
        if ab:
            for z in list(self.zombies):
                if ab.colliderect(z.rect):
                    z.hp -= 1
        if z.hp <= 0:
            player.score += z.score_worth
        self.zombies.remove(z)
        for p in list(self.pumpkins):
            if ab.colliderect(p.rect):
                p.hp -= 1
        if p.hp <= 0:
            player.health = clamp(player.health + p.heal_amount, 0, player.max_health)
        self.pumpkins.remove(p)

    def draw_background(self, screen: pg.Surface, cam_x: float, width: int, height: int):
        SKY = (12, 12, 24);
        MOON = (250, 250, 200)
        screen.fill(SKY)
        pg.draw.circle(screen, MOON, (int(width * 0.8 - cam_x * 0.1) % (width + 200) - 100, 120), 40)
        for i in range(6):
            y = 200 + i * 40
            pg.draw.rect(screen, (40, 40, 60, 80), (0, y, width, 8))

    def draw_ground_and_deco(self, screen: pg.Surface, cam_x: float, width: int):
        GROUND = (30, 30, 30)
        pg.draw.rect(screen, GROUND, (0, self.s.ground_y, width, screen.get_height() - self.s.ground_y))
        for x in range(-((int(cam_x) // 40) % 40) * 40, width, 40):
            pg.draw.rect(screen, (80, 80, 90), (x, self.s.ground_y - 10, 4, 30))
        pg.draw.rect(screen, (80, 80, 90), (x + 20, self.s.ground_y - 8, 4, 28))
        for g in self.graves:
            if cam_x - 60 <= g.x <= cam_x + width + 60:
                pg.draw.rect(screen, (90, 90, 110), (g.x - cam_x, g.y, g.w, g.h), border_radius=6)

    def draw(self, screen: pg.Surface, camera):
        cam_x = camera.x
        w, h = screen.get_width(), screen.get_height()
        self.draw_background(screen, cam_x, w, h)
        self.draw_ground_and_deco(screen, cam_x, w)
        # pumpkins
        for p in self.pumpkins:
            if abs(p.rect.x - cam_x) < w + 100:
                p.draw(screen, camera)
        # zombies
        for z in self.zombies:
            if abs(z.rect.x - cam_x) < w + 200:
                z.draw(screen, camera)