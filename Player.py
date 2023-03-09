import pygame as pg
from class_Point import Point
from functions import get_visual
from CONFIG import objects


class Player:
    def __init__(self, *, pos, size, facing, speed, visual, hp, defence, lvl=0, exp=0, n_exp=10, attack=(100, (None, 'b'))):
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(pos.x, pos.y, size.x, size.y)

        self.facing = facing
        self.speed = speed

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

        self.hp = hp
        self.defence = defence
        self.lvl = lvl
        self.exp = exp
        self.expToNextLvl = n_exp

        self.attack = attack[0]
        self.attack_func = []
        self.attack_dict = {}
        for i in range(1, len(attack)):
            _key = pg.key.key_code(attack[i][1])
            _attack = attack[i][0]
            _args = attack[i][2:]
            self.attack_func.append({'key': _key, 'attack': _attack, 'args': _args})
            self.attack_dict[f'{_attack}'] = i

    def step(self, keys):
        if keys[pg.K_UP]:
            self.facing = Point(0, -1)
            self._pos_update()
        if keys[pg.K_DOWN]:
            self.facing = Point(0, 1)
            self._pos_update()
        if keys[pg.K_LEFT]:
            self.facing = Point(-1, 0)
            self._pos_update()
        if keys[pg.K_RIGHT]:
            self.facing = Point(1, 0)
            self._pos_update()
        for attack in self.attack_func:
            if keys[attack['key']]:
                if attack['attack'] is not None:
                    attack['args'] = attack['attack'](attack['args'])

    def draw(self, win):
        if not self.textured:
            pg.draw.rect(win, self.color, self.rect)
        else:
            pass
        pg.display.update(self.rect)

    def _pos_update(self):
        new_pos = Point(self.pos + self.facing * self.speed)
        new_rect = pg.Rect(new_pos.x, new_pos.y, self.size.x, self.size.y)
        if objects['PlayScreen'].field.is_allowed(new_rect):
            self.pos = new_pos
            self.rect = new_rect
