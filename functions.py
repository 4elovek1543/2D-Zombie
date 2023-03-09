import pygame as pg
from math import sqrt

from CONFIG import *


def get_visual(paths, name, count, size):
    images = []
    for i in range(count):
        try:
            images.append(pg.image.load(f'{paths}{name}{i}.png').convert_alpha())
        except FileNotFoundError:
            images.append(pg.image.load(f'{paths}{name}{i}.jpg').convert_alpha())
        # добавляет в список изображений новое
        images[-1] = pg.transform.scale(images[i], (size.x,  size.y))
    return images


def dist(a, b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)
