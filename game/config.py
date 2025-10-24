import os
import sys

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

# Asset Paths
SKELETON = 'assets/sprites/skeleton.png'
SKULL = 'assets/sprites/skull.png'
PUMPKIN = 'assets/sprites/pumpkin.png'
GRAVEYARD = 'assets/backgrounds/graveyard.jpg'
TRACK = 'assets/WhatsThis.ogg'


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)


SKELETON = resource_path(SKELETON)
SKULL = resource_path(SKULL)
PUMPKIN = resource_path(PUMPKIN)
GRAVEYARD = resource_path(GRAVEYARD)
TRACK = resource_path(TRACK)
