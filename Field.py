import pygame as pg
from class_Point import Point
from functions import get_visual


class Field:
    def __init__(self, win, pos, fiz_size, el_size, visual):
        self.win = win

        self.pos = pos
        self.size = fiz_size

        count_x = fiz_size.x//el_size.x
        count_y = fiz_size.y//el_size.y
        self.el_size = Point(fiz_size.x//count_x, fiz_size.y//count_y)

        self.pos = Point(pos) + Point((fiz_size.x-count_x*self.el_size.x)//2, (fiz_size.y-count_y*self.el_size.y)//2)
        self.size = Point(self.el_size.x*count_x, self.el_size.y*count_y)
        self.rect = pg.Rect(pos.x, pos.y, self.size.x, self.size.y)

        if visual[0]:
            self.textured = True
            self.images = get_visual(visual[1], visual[2], 2, self.el_size)
        else:
            self.textured = False
            self.bg_color = (visual[1], visual[2])

        self.cells = []
        loc_pos = Point(pos)
        for i in range(count_y):
            self.cells.append([])
            for j in range(count_x):
                self.cells[i].append((0, Point(loc_pos)))
                loc_pos.x += self.el_size.x
            loc_pos.x = pos.x
            loc_pos.y += self.el_size.y

    def draw(self):
        for line in self.cells:
            for el in line:
                if self.textured:
                    self.win.blit(self.images[el[0]], tuple(el[1]))
                else:
                    pg.draw.rect(self.win, self.bg_color[el[0]], (el[1].x, el[1].y, self.el_size.x, self.el_size.y))

    def is_allowed(self, rect):
        return self.rect.collidepoint(rect.topleft[0], rect.topleft[1]) and \
            self.rect.collidepoint(rect.topright[0], rect.topright[1]) and \
            self.rect.collidepoint(rect.bottomleft[0], rect.bottomleft[1]) and \
            self.rect.collidepoint(rect.bottomright[0], rect.bottomright[1])


class PlayScreen:
    def __init__(self, *, win, pos, board, field):
        self.win = win

        self.pos = pos
        self.size = Point(win.get_width(), win.get_height())
        self.rect = win.get_rect()

        self.board = board
        self.field = field
        self.images = []
        self.buttons = []
        self.menus = {}

    def add_img(self, pos, size, visual):
        self.images.append((pos, get_visual(visual[0], visual[1], 1, size)))

    def add_button(self, button):
        self.buttons.append(button)

    def add_menu(self, key, menu):
        self.menus[key] = menu

    def draw(self, keys):
        for el in self.board:
            self.win.blit(el[1], tuple(el[0]))

        self.field.draw()

        for img in self.images:
            self.win.blit(img[1], tuple(self.pos+img[0]))

        for button in self.buttons:
            button.draw()

        for key in self.menus.keys():
            if keys[key]:
                self.menus[key].proces()
