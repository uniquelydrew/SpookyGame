from pathlib import Path
WIDTH, HEIGHT = 960, 540
FPS = 60
GRAVITY = 0.7
WORLD_LEN = 8000
GROUND_Y = HEIGHT - 80
ASSET_DIR = Path(__file__).with_name("images")

# Densities/difficulty
BASE_ZOMBIE_HP = 3
BASE_ZOMBIE_SPEED = 1.2
ZOMBIE_SCALE_PER_1000PX = 0.35
SPAWN_DENSITY = 0.0016
PUMPKIN_DENSITY = 0.0007

# Controls
KEY_LEFT = ("a", "left")
KEY_RIGHT = ("d", "right")
KEY_JUMP = ("w", "up", "space")
KEY_ATTACK = ("j", "k", "lctrl")

HIGHSCORE_PATH = Path("highscores.json")
FONT_NAME = "arial"
