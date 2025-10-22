

# ==========================================
# file: ui/hud.py
# ==========================================
import pygame as pg
try:
    from assets import font
except Exception: # fallback if assets.py not present yet
    font = None

WHITE=(240,240,240); GREY=(120,120,140); GREEN=(70,200,120)

class HUD:
    def __init__(self, width: int):
        self.width = width
        self._f_s = font(18) if font else pg.font.SysFont("arial", 18)
        self._f_m = font(24) if font else pg.font.SysFont("arial", 24, bold=True)


    def draw(self, screen: pg.Surface, player):
        # health bar
        pg.draw.rect(screen, GREY, (20, 20, 200, 16), border_radius=4)
        hpw = int(200 * (player.health / player.max_health))
        pg.draw.rect(screen, GREEN, (20, 20, hpw, 16), border_radius=4)
        screen.blit(self._f_m.render(f"Score: {player.score}", True, WHITE), (self.width-180, 16))