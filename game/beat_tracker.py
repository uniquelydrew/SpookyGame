import time
from .config import BEAT_INTERVAL, TOLERANCE

class BeatTracker:
    def __init__(self):
        self.last_beat_time = time.time()

    def update(self):
        current_time = time.time()
        if current_time - self.last_beat_time >= BEAT_INTERVAL:
            self.last_beat_time = current_time
            return True
        return False

    def calculate_accuracy(self, press_time):
        diff = abs(press_time - self.last_beat_time)
        if diff <= TOLERANCE:
            return max(0, 1 - (diff / TOLERANCE))
        return 0
