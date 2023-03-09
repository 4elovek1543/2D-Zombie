import pygame as pg
from class_Point import Point
from functions import get_visual, dist


class Bullet:
    def __init__(self, pos, size, facing, speed, dmg, visual):
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(pos.x, pos.y, size*2, size*2)

        self.facing = facing
        self.speed = speed

        if not visual[0]:
            self.textured = False
            self.color = visual[1]
        else:
            self.textured = True
            self.image = get_visual(visual[1], visual[2], str(self.facing)[1:-1], Point(2*size, 2*size))

        self.dmg = dmg

    def step(self):
        self.pos += self.facing*self.speed
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size*2, self.size*2)

    def draw(self, win):
        if self.textured:
            win.blit(self.image, (self.pos.x-self.size, self.pos.y-self.size))
        else:
            pg.draw.circle(win, self.color, tuple(self.pos), self.size)
        pg.display.update(self.rect)


class Grenade:
    def __init__(self, pos, size, facing, speed, dmg, rad, visual):
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(pos.x, pos.y, size*2, size*2)

        self.facing = facing
        self.speed = speed

        if not visual[0]:
            self.textured = False
            self.color = visual[1]
            self.end_color = visual[2]
        else:
            self.textured = True
            self.image = get_visual(visual[1], str(self.facing)[1:-1], 1, Point(2*size, 2*size))
            self.end_image = get_visual(visual[1], visual[2], 1, Point(2*rad, 2*rad))

        self.dmg = dmg
        self.rad = rad

    def step(self):
        self.pos += self.facing*self.speed
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size*2, self.size*2)

    def draw(self, win):
        if self.textured:
            win.blit(self.image, (self.pos.x-self.size, self.pos.y-self.size))
        else:
            pg.draw.circle(win, self.color, tuple(self.pos), self.size)
        pg.display.update(self.rect)

    def end(self, win, entities):
        if self.textured:
            win.blit(self.end_image, (self.pos.x-self.rad, self.pos.y-self.rad))
        else:
            pg.draw.circle(win, self.end_color, tuple(self.pos), self.rad)
        pg.display.update()
        damaged = []
        for i in range(len(entities)):
            if dist(self.pos, entities[i].pos) <= self.rad:
                damaged.append(i)
        return damaged
