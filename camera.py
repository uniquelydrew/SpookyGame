# ==========================================
# file: camera.py
# ==========================================
from self import self


class Camera:
    """Very small side-scrolling camera that follows a target x.
    Keeps x within [0, world_len - screen_width]."""
    def __init__(self, screen_width: int, world_len: int):
        self.x = 0.0
        self._w = screen_width
        self._len = world_len

    @staticmethod
    def _clamp(v, lo, hi):
        return max(lo, min(hi, v))

    def update(self, target_x: float):
        self.x = self._clamp(target_x - self._w * 0.5, 0, max(0, self._len - self._w))