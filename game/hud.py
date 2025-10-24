from .config import FONT, WHITE, GREEN

def draw_score(surface, score):
    text = FONT.render(f"Score: {score}", True, WHITE)
    surface.blit(text, (20, 20))

def draw_win_message(surface):
    win_text = FONT.render("Enemy Defeated!", True, GREEN)
    surface.blit(win_text, (300, 100))
