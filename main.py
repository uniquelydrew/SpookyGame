import pygame
import time
import random
import math


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rhythm Battle")
clock = pygame.time.Clock()

# Load and play music
pygame.mixer.music.load('WhatsThis.ogg')  # Replace with your actual music file
pygame.mixer.music.play()

# Fonts and colors
font = pygame.font.SysFont("Arial", 28)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Constants
BPM = 120
BEAT_INTERVAL = 60 / BPM
TOLERANCE = 0.2


# Game variables
last_beat_time = time.time()
score = 0



# Enemy data structure
class Enemy:
    def __init__(self):
        self.health = 30
        self.max_health = 30
        self.x = 500
        self.y = 300
        self.image = pygame.Surface((80, 80))
        self.image.fill(RED)


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        # Draw health bar
        health_bar_width = 80 * (self.health / self.max_health)
        pygame.draw.rect(surface, GREEN, (self.x, self.y - 10, health_bar_width, 5))
    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)

# Player data
player_x = 200
player_y = 300
player_image = pygame.Surface((80, 80))
player_image.fill(WHITE)

# Instantiate enemy
enemy = Enemy()

def calculate_accuracy(press_time, beat_time):
    diff = abs(press_time - beat_time)
    if diff <= TOLERANCE:
        return max(0, 1 - (diff / TOLERANCE))  # Scale damage 0.0 to 1.0
    return 0

running = True
while running:
    current_time = time.time()
    time_since_last_beat = current_time - last_beat_time


    if time_since_last_beat >= BEAT_INTERVAL:
        last_beat_time = current_time
        print("Beat!")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            accuracy = calculate_accuracy(current_time, last_beat_time)
            damage = round(accuracy * 10)
            if damage > 0:
                print(f"Attack! Accuracy: {accuracy:.2f} → Damage: {damage}")
                enemy.take_damage(damage)
                score += damage
            else:
                print("Miss! Too off-beat.")


    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_x, player_y))
    enemy.draw(screen)


    # Draw score and instructions
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))


    if enemy.health <= 0:
        win_text = font.render("Enemy Defeated!", True, GREEN)
        screen.blit(win_text, (300, 100))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(f"Final Score: {score}")
