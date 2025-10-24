import pygame
import time
from .config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from .player import Player
from .enemy import Enemy
from .hud import draw_score, draw_win_message
from .beat_tracker import BeatTracker
from .projectile import SkullProjectile

class Game:
    def __init__(self):
        self.background = None
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load("assets/backgrounds/graveyard.jpg").convert()

        pygame.display.set_caption("What's This")
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load('assets/WhatsThis.ogg')
        pygame.mixer.music.play()

        pygame.display.set_caption("What's This")
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load('assets/WhatsThis.ogg')
        pygame.mixer.music.play()

        self.running = True
        self.player = Player()
        self.enemy = Enemy()
        self.beat_tracker = BeatTracker()
        self.score = 0
        self.projectiles = []

    def run(self):
        while self.running:
            beat_hit = self.beat_tracker.update()
            self.handle_events()
            self.update_projectiles()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        print("Final Score: {self.score}")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                accuracy = self.beat_tracker.calculate_accuracy(time.time())
                damage = round(accuracy * 10)
                if damage > 0:
                    projectile = SkullProjectile(self.player.x + 50, self.player.y + 30)
                    projectile.damage = damage
                    self.projectiles.append(projectile)

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # ✅ MUST be first!
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        draw_score(self.screen, self.score)
        for projectile in self.projectiles:
            projectile.draw(self.screen)

        if self.enemy.is_defeated():
            draw_win_message(self.screen)
        pygame.display.flip()

    def update_projectiles(self):
        for projectile in self.projectiles[:]:
            projectile.update()

            if projectile.off_screen(self.screen.get_width()):
                self.projectiles.remove(projectile)
                continue

            enemy_rect = self.enemy.image.get_rect(topleft=(self.enemy.x, self.enemy.y))

            if projectile.collides_with(enemy_rect):
                self.enemy.take_damage(projectile.damage)
                self.score += projectile.damage
                self.projectiles.remove(projectile)
                print(f"Hit! Damage: {projectile.damage}, New Score: {self.score}")

    def spawn_enemy(self):
        from .enemy import Enemy  # if not already imported
        self.enemy = Enemy()  # Replace with new instance