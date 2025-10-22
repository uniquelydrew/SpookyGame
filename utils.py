# ==========================================
# file: utils.py
# ==========================================
import json, time, os


__all__ = ["clamp", "load_highscores", "save_highscore"]


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def load_highscores(path: str):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_highscore(path: str, score: int):
    hs = load_highscores(path)
    hs.append({"score": int(score), "ts": int(time.time())})
    hs.sort(key=lambda r: r["score"], reverse=True)
    hs = hs[:5]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(hs, f, indent=2)