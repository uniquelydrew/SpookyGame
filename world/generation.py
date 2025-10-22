import random, pygame as pg
from ..settings import (WORLD_LEN, GROUND_Y, SPAWN_DENSITY, PUMPKIN_DENSITY,
                        ZOMBIE_SCALE_PER_1000PX)
from ..entities.zombie import Zombie
from ..entities.pumpkin import Pumpkin

def level_tier_at(x:int)->int:
    return int((x//1000) * ZOMBIE_SCALE_PER_1000PX * 3)

def populate(zombies_group, pumpkins_group, graves:list, rng:random.Random):
    for _ in range(200):
        gx = rng.randint(0, WORLD_LEN-30)
        gy = GROUND_Y - 40 - rng.randint(0, 20)
        graves.append(pg.Rect(gx, gy, rng.randint(16,32), rng.randint(24,48)))

    x=300
    while x < WORLD_LEN-200:
        if rng.random() < SPAWN_DENSITY*50:
            tier = level_tier_at(x) + rng.randint(0, 1)
            zombies_group.add(Zombie(x, GROUND_Y-60, tier))
        if rng.random() < PUMPKIN_DENSITY*50:
            pumpkins_group.add(Pumpkin(x+rng.randint(-20,20), GROUND_Y-28))
        x += rng.randint(30, 80)
