import time

import pygame

from .beat_tracker import BeatTracker
from .config import SCREEN_WIDTH, SCREEN_HEIGHT, GRAVEYARD, TRACK, BEAT_INTERVAL
from .enemy import Enemy
from .hud import draw_score, draw_win_message, draw_judgment, draw_pumpkins
from .player import Player
from .projectile import SkullProjectile


def _now() -> float:
    return pygame.time.get_ticks() / 1000.0


class Game:
    def __init__(self):
        # Init audio first to reduce pops/stutter
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("What's This")
        self.clock = pygame.time.Clock()

        # Background (scaled to fit)
        try:
            self.background = pygame.image.load(GRAVEYARD).convert()
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except Exception:
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill((10, 10, 14))

        # Music (non-fatal if missing)
        try:
            pygame.mixer.music.load(TRACK)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        except Exception:
            pass

        # Start time for beat phase
        self.start_time_sec = _now()

        # State
        self.running = True
        self.player = Player()
        self.enemy = Enemy()
        self.beat_tracker = BeatTracker()
        self.score = 0
        self.pumpkins = 0
        self.projectiles = []

        # Judgment UI
        self.judgment_text = ""
        self.judgment_timer = 0  # frames remaining

        # Win/respawn handling
        self.win_timer = 0  # frames remaining to show win banner
        self.win_flash_duration = 48  # ~0.8s at 60fps

    def run(self):
        while self.running:
            beat_hit = self.beat_tracker.update()  # (kept if you use it elsewhere)
            self.handle_events()

            # Countdown judgment label
            if self.judgment_timer > 0:
                self.judgment_timer -= 1

            self.update_projectiles()
            self.update_win_state()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        print(f"Final Score: {self.score}")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # Use Python time for your tracker (as your code did),
                    # but you could also use _now() for consistency.
                    accuracy, judgment = self.beat_tracker.calculate_accuracy(time.time())
                    damage = round(accuracy * 10)

                    self.judgment_text = judgment
                    self.judgment_timer = 30  # ~0.5 sec at 60fps

                    if damage > 0:
                        # Spawn from player center so it works even without x/y attrs
                        px, py = getattr(self.player, "rect", pygame.Rect(0, 0, 0, 0)).center
                        projectile = SkullProjectile(px + 30, py - 10)
                        projectile.damage = damage
                        self.projectiles.append(projectile)

    def draw(self):
        # Background first
        self.screen.blit(self.background, (0, 0))

        # Entities
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)

        # Projectiles
        for projectile in self.projectiles:
            projectile.draw(self.screen)

        # Beat ring visualizer around player
        elapsed = _now() - self.start_time_sec
        phase = (elapsed % (BEAT_INTERVAL * 2)) / (BEAT_INTERVAL * 2)
        radius = 40 + int(60 * phase)
        alpha = 255 - int(255 * phase)
        surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 255, 255, alpha), (radius, radius), radius, 3)
        px, py = getattr(self.player, "rect", pygame.Rect(0, 0, 0, 0)).center
        self.screen.blit(surf, (px - radius, py - radius))

        # HUD
        draw_score(self.screen, self.score)
        draw_pumpkins(self.screen, self.pumpkins)

        # Judgment text centered near top (or position above player if you prefer)
        if self.judgment_timer > 0 and self.judgment_text:
            draw_judgment(self.screen, self.judgment_text, (SCREEN_WIDTH // 2 - 50, 200), self.judgment_timer)

        # Win banner (if any)
        if self.win_timer > 0:
            draw_win_message(self.screen)

        pygame.display.flip()

    def update_projectiles(self):
        # Iterate over a copy so we can remove safely
        for projectile in self.projectiles[:]:
            projectile.update()

            # Offscreen?
            if projectile.off_screen(self.screen.get_width()):
                self.projectiles.remove(projectile)
                continue

            # Enemy rect: prefer enemy.rect, else build from image + x/y
            enemy_rect = getattr(self.enemy, "rect", None)
            if enemy_rect is None:
                ex = getattr(self.enemy, "x", 0)
                ey = getattr(self.enemy, "y", 0)
                enemy_img = getattr(self.enemy, "image", None)
                if enemy_img is not None:
                    enemy_rect = enemy_img.get_rect(topleft=(ex, ey))

            if enemy_rect and projectile.collides_with(enemy_rect):
                self.enemy.take_damage(projectile.damage)
                self.score += projectile.damage
                self.projectiles.remove(projectile)
                # Start win flow if enemy just died
                if hasattr(self.enemy, "is_defeated") and self.enemy.is_defeated():
                    self.begin_win_flow()

    def begin_win_flow(self):
        # Trigger win banner and schedule respawn once
        if self.win_timer == 0:
            self.win_timer = self.win_flash_duration
            self.pumpkins += 1  # your collectible increment

    def update_win_state(self):
        if self.win_timer > 0:
            self.win_timer -= 1
            if self.win_timer == 0:
                self.spawn_enemy()

    def spawn_enemy(self):
        # Fresh enemy instance
        self.enemy = Enemy()
