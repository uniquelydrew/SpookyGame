import pygame

from .config import SCREEN_WIDTH
from .config import FONT, WHITE, GREEN, RED, FONT_LARGE

judgment_colors = {
    "Perfect": (0, 255, 255),
    "Good": (0, 200, 0),
    "Miss": (255, 50, 50),
}

def draw_score(surface, score):
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (20, 20))

def draw_win_message(surface):
    win_text = FONT.render("Enemy Defeated!", True, GREEN)
    surface.blit(win_text, (300, 100))

def draw_judgment(surface, text, pos, frame, max_frames=30):
    if frame > 0 and text in judgment_colors:
        color = judgment_colors[text]
        float_y = pos[1] - (frame * 1.5) # float upward
        alpha = max(0, 255 - int((frame / max_frames) * 255))


        label = FONT_LARGE.render(text, True, color)
        label.set_alpha(alpha)
        surface.blit(label, (pos[0], float_y))

def draw_pumpkins(surface, pumpkins):
    score_text = FONT.render(f"Pumpkins: {pumpkins}", True, WHITE)
    surface.blit(score_text, (SCREEN_WIDTH-200, 20))