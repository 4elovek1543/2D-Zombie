import pygame as pg
from CONFIG import *
from class_Point import Point
from functions import get_visual


class Menu:
    def __init__(self, *, win, pos=Point(), size=Point(), bg=(0, 0, 0),
                 buttons=None, esc_key=27):
        self.win = win
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(pos.x, pos.y, size.x, size.y)

        if isinstance(bg, tuple):
            self.imaged = False
            self.bg_color = bg
        else:
            self.imaged = True
            self.bg_image = bg

        self.buttons = buttons
        for button in self.buttons:
            button.win = self.win
            button.pos += self.pos

        self.escKey = esc_key

    def proces(self):
        pg.init()

        clock = pg.time.Clock()

        run = True
        while run:
            clock.tick(FPS//2)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            keys = pg.key.get_pressed()
            if keys[self.escKey]:
                break

            if self.imaged:
                self.win.blit(self.bg_image, tuple(self.pos))
            else:
                pg.draw.rect(self.win, self.bg_color, self.rect)
            pg.display.update(self.rect)

            for button in self.buttons:
                button.draw()


class Button:
    def __init__(self, *, win=None, pos=Point(), size=Point(), bg=((0, 0, 0), (40, 40, 40), (60, 60, 60)),
                 func=None, func_args=None):
        self.win = win
        self.pos = pos
        self.size = size
        self.rect = pg.Rect((pos.x, pos.y, size.x, size.y))

        if isinstance(bg, tuple):
            self.imaged = False
            self.bg_color = bg[0]
            self.on_color = bg[1]
            self.press_color = bg[2]
        else:
            self.imaged = True
            self.images = get_visual(bg[0], bg[1], 3, self.size)

        self.func = func
        self.func_args = func_args

    def draw(self):
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if self.imaged:
                self.win.blit(self.images[1], tuple(self.pos))
            else:
                pg.draw.rect(self.win, self.on_color, self.rect)

            if pg.mouse.get_pressed(num_buttons=3)[0]:
                if self.imaged:
                    self.win.blit(self.images[2], tuple(self.pos))
                else:
                    pg.draw.rect(self.win, self.press_color, self.rect)
                if self.func is not None:
                    self.func_args = self.func(self.func_args)

        else:
            if self.imaged:
                self.win.blit(self.images[0], tuple(self.pos))
            else:
                pg.draw.rect(self.win, self.bg_color, self.rect)

        pg.display.update(self.rect)
