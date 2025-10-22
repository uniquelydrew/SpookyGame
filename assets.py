import pygame as pg
from functools import lru_cache
from .settings import ASSET_DIR

def _norm_key(k:str): return getattr(pg, f"K_{k}")

def init():  # call once after pg.init()
    pg.display.set_icon(pg.Surface((1,1)))  # placeholder to ensure display fmt

@lru_cache(maxsize=128)
def image(name:str, size=None, colorkey=None):
    surf = pg.image.load(str(ASSET_DIR / name))
    surf = surf.convert_alpha() if surf.get_alpha() else surf.convert()
    if colorkey and not surf.get_alpha(): surf.set_colorkey(colorkey)
    if size: surf = pg.transform.smoothscale(surf, size)
    return surf

@lru_cache(maxsize=64)
def font(size:int, bold=False):
    return pg.font.SysFont("arial", size, bold=bold)
