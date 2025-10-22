# ==========================================
# file: scenes/gameover.py
# ==========================================
import pygame as pg
import self

from utils import save_highscore


WHITE=(240,240,240)


class GameOverScene:
    def __init__(self, game, score: int):
        self.game = game
        self.score = score
        save_highscore(self.game.highscore_path, score)
        self.font_l = pg.font.SysFont("arial", 48, bold=True)
        self.font_m = pg.font.SysFont("arial", 24, bold=True)


    def handle_event(self, e):
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_r:
                self.game.to_play()
            if e.key == pg.K_ESCAPE:
                self.game.quit()


    def update(self, dt):
        pass

    def draw(self, screen):
        w, h = screen.get_width(), screen.get_height()
        screen.fill((12,12,24))
        screen.blit(self.font_l.render("GAME OVER", True, WHITE), (w//2-150, h//2-80))
        screen.blit(self.font_m.render(f"Score: {self.score}", True, WHITE), (w//2-60, h//2-30))
        screen.blit(self.font_m.render("Press R to restart or ESC to quit", True, WHITE), (w//2-200, h//2+10))