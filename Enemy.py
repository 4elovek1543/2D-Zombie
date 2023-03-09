import pygame as pg
from class_Point import Point
from functions import get_visual
from math import fabs
from CONFIG import objects


class Zombie:
    def __init__(self, *, pos, size, speed, facing, visual, hp, defence, cost, attack=None):
        self.pos = pos
        self.size = size
        self.rect = pg.Rect((pos.x, pos.y, size.x, size.y))

        self.speed = speed
        self.facing = facing

        self.textured = visual[0]
        if self.textured:
            hor = visual['hor']
            self.img_hor = get_visual(hor[0], hor[1], hor[2], self.size)
            vert = visual['vert']
            self.img_vert = get_visual(vert[0], vert[1], vert[2], self.size)
            stat = visual['stat']
            self.img_stat = get_visual(stat[0], stat[1], stat[2], self.size)
            self.animCount = 0
            self.maxAimCountHor = hor[2]
            self.maxAimCountVert = vert[2]
        else:
            self.color = visual[1]

        self.attack = attack

        self.hp = hp
        self.defence = defence
        self.cost = cost

    def step(self, target_pos):
        dx = fabs(target_pos.x-self.pos.x)
        dy = fabs(target_pos.y-self.pos.y)
        if fabs(dx) <= fabs(dy):
            self.facing = Point(1 if dx >= 0 else -1, 0)
        else:
            self.facing = Point(0, 1 if dy >= 0 else -1)
        self.pos += self.facing*self.speed
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def draw(self, win):
        if not self.textured:
            pg.draw.rect(win, self.color, self.rect)
        else:
            pass
        pg.display.update(self.rect)


