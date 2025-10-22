import pygame as pg

class AbstractScene:
    def __init__(self, game): self.game = game
    def handle_event(self, e): pass
    def update(self, dt): pass
    def draw(self, screen): pass

class SceneManager:
    def __init__(self, scene:AbstractScene): self.scene = scene
    def switch(self, scene_cls): self.scene = scene_cls(self.scene.game)
    def handle_event(self, e): self.scene.handle_event(e)
    def update(self, dt): self.scene.update(dt)
    def draw(self, screen): self.scene.draw(screen)
