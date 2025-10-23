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

# Constants
BPM = 120
BEAT_INTERVAL = 60 / BPM
TOLERANCE = 0.2  # How much error (in seconds) is allowed for "perfect"

# Variables
last_beat_time = time.time()
score = 0

def calculate_accuracy(press_time, beat_time):
    diff = abs(press_time - beat_time)
    if diff <= TOLERANCE:
        return max(0, 1 - (diff / TOLERANCE))  # Scale damage 0.0 to 1.0
    return 0

running = True
while running:
    current_time = time.time()
    time_since_last_beat = current_time - last_beat_time

    # Advance beat
    if time_since_last_beat >= BEAT_INTERVAL:
        last_beat_time = current_time
        print("Beat!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for keypress (attack)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            accuracy = calculate_accuracy(current_time, last_beat_time)
            damage = round(accuracy * 10)  # Scale damage out of 10
            if damage > 0:
                print(f"Attack! Accuracy: {accuracy:.2f} → Damage: {damage}")
                score += damage
            else:
                print("Miss! Too off-beat.")

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(f"Final Score: {score}")
