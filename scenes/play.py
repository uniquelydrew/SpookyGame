import pygame as pg, random
from .state import AbstractScene
from ..camera import Camera
from ..entities.player import Player
from ..world.world import World
from ..ui.hud import HUD

class PlayScene(AbstractScene):
    def __init__(self, game):
        super().__init__(game)
        self.camera = Camera()
        self.world  = World(rng=random.Random())
        self.player = Player(60, self.world.ground_y-54)
        self.hud    = HUD()

    def handle_event(self, e):
        if e.type==pg.KEYDOWN and e.key==pg.K_ESCAPE:
            self.game.to_gameover(self.player.score)

    def update(self, dt):
        self.player.handle_input(self.game.keys)
        self.world.update(self.player, dt)
        self.camera.update(self.player.rect.x)
        if self.player.dead: self.game.to_gameover(self.player.score)

    def draw(self, screen):
        self.world.draw(screen, self.camera)
        self.player.draw(screen, self.camera)  # draw method can live on entity
        self.hud.draw(screen, self.player)
