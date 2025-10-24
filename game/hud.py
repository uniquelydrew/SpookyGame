import pygame
from .config import FONT, WHITE, GREEN, RED

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

def draw_judgment(surface, text, pos, timer):
    if timer > 0 and text in judgment_colors:
        color = judgment_colors[text]
        label = FONT.render(text, True, color)
        surface.blit(label, pos)
