import pygame
import time
from .config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, GRAVEYARD, TRACK
from .player import Player
from .enemy import Enemy
from .hud import draw_score, draw_win_message, draw_judgment, draw_pumpkins
from .beat_tracker import BeatTracker
from .projectile import SkullProjectile

class Game:
    def __init__(self):
        self.background = None
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load(GRAVEYARD).convert()

        pygame.display.set_caption("What's This")
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load(TRACK)
        pygame.mixer.music.play()

        pygame.display.set_caption("What's This")
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load(TRACK)
        pygame.mixer.music.play()

        self.running = True
        self.player = Player()
        self.enemy = Enemy()
        self.beat_tracker = BeatTracker()
        self.score = 0
        self.pumpkins = 0
        self.projectiles = []
        self.judgment_text = ""
        self.judgment_timer = 0

    def run(self):
        while self.running:
            beat_hit = self.beat_tracker.update()
            self.handle_events()
            if self.judgment_timer > 0:
                self.judgment_timer -= 1
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
                accuracy, judgment = self.beat_tracker.calculate_accuracy(time.time())
                damage = round(accuracy * 10)
                self.judgment_text = judgment
                self.judgment_timer = 30  # show for ~0.5 seconds at 60fps
                if damage > 0:
                    projectile = SkullProjectile(self.player.x + 50, self.player.y + 30)
                    projectile.damage = damage
                    self.projectiles.append(projectile)

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # ✅ MUST be first!
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        draw_score(self.screen, self.score)
        draw_pumpkins(self.screen, self.pumpkins)
        for projectile in self.projectiles:
            projectile.draw(self.screen)

        if self.judgment_timer > 0:
            draw_judgment(self.screen, self.judgment_text, (SCREEN_WIDTH // 2 - 50, 200), self.judgment_timer)

        if self.enemy.is_defeated():
            draw_win_message(self.screen)
            self.pumpkins += 1
            self.spawn_enemy()
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