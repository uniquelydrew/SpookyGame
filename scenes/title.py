# ==========================================
# file: scenes/title.py
# ==========================================
import pygame as pg
import self

from utils import load_highscores


WHITE=(240,240,240)


class TitleScene:
    def __init__(self, game):
        self.game = game
        self.font_l = pg.font.SysFont("arial", 48, bold=True)
        self.font_m = pg.font.SysFont("arial", 24, bold=True)
        self.font_s = pg.font.SysFont("arial", 18)

    def handle_event(self, e):
        if e.type == pg.KEYDOWN:
            self.game.to_play()

    def update(self, dt):
        pass

    def draw(self, screen):
        w, h = screen.get_width(), screen.get_height()
        screen.fill((12,12,24))
        screen.blit(self.font_l.render("SKELETON'S WAKE", True, WHITE), (w//2-220, h//2-120))
        screen.blit(self.font_m.render("WASD/Arrows move · Space/W jump · J/K/Ctrl attack", True, WHITE), (w//2-320, h//2-40))
        screen.blit(self.font_m.render("Press any key to begin", True, WHITE), (w//2-150, h//2+10))
        y = h//2 + 60
        screen.blit(self.font_m.render("High Scores", True, WHITE), (w//2-70, y))
        y += 28
        for i, r in enumerate(load_highscores(self.game.highscore_path)[:5], 1):
            screen.blit(self.font_s.render(f"{i:>2}. {r['score']}", True, WHITE), (w//2-20, y))
            y += 20