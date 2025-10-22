import pygame as pg
from settings import WIDTH, HEIGHT, FPS
from assets import init as assets_init
from scenes.state import SceneManager
from scenes.title import TitleScene  # implements start->PlayScene, shows highscores

class Keys:
    def __init__(self): self.left=self.right=self.jump=self.attack=False
    def read(self):
        k = pg.key.get_pressed()
        self.left  = k[pg.K_a] or k[pg.K_LEFT]
        self.right = k[pg.K_d] or k[pg.K_RIGHT]
        self.jump  = k[pg.K_w] or k[pg.K_UP] or k[pg.K_SPACE]
        self.attack= k[pg.K_j] or k[pg.K_k] or k[pg.K_LCTRL]

class Game:
    def __init__(self):
        pg.init(); assets_init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.manager = SceneManager(TitleScene(self))
        self.keys = Keys()

    def to_gameover(self, score): from .scenes.gameover import GameOverScene; self.manager.scene = GameOverScene(self, score)
    def to_play(self):             from .scenes.play import PlayScene;       self.manager.scene = PlayScene(self)

    def run(self):
        running=True
        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT: running=False
                self.manager.handle_event(e)
            self.keys.read()
            dt = self.clock.tick(FPS) / 1000.0
            self.manager.update(dt)
            self.manager.draw(self.screen)
            pg.display.flip()

if __name__ == "__main__":
    Game().run()
