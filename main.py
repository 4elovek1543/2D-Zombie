import pygame as pg
from class_Point import Point
import Menu
import button_func
from CONFIG import *

pg.init()

clock = pg.time.Clock()

if FULL:
    win = pg.display.set_mode()
    WEIGHT, HEIGHT = win.get_width(), win.get_height()
else:
    win = pg.display.set_mode((WEIGHT, HEIGHT))

pg.display.set_caption(f'{NAME} {VERSION}')

menu_bg = pg.image.load(f'images/menu_bg.jpg').convert_alpha()
pg.transform.scale(menu_bg, (WEIGHT, HEIGHT))

start_button = Menu.Button(pos=Point(450, 450), size=Point(200, 60), bg=['images/', 'buttons_'],
                           func=button_func.start_func, func_args=win)

menu = Menu.Menu(win=win, pos=Point(), size=Point(WEIGHT, HEIGHT), bg=menu_bg, buttons=[start_button])

menu.proces()

pg.quit()
