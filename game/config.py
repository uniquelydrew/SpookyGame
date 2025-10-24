import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BPM = 180
BEAT_INTERVAL = 60 / BPM
TOLERANCE = 0.2

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 28)