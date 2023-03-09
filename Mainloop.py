import pygame as pg

import Menu
import Player
import Field
from CONFIG import *


def main(win):

    clock = pg.time.Clock()

    run = True

    init(win)

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        keys = pg.key.get_pressed()

        objects['PlayScreen'].draw(keys)

        objects['Player'].step(keys)
        objects['Player'].draw(win)

        pg.display.update()


def init(win):
    field = Field.Field(win=win, pos=Field_stats['El_SIZE'], fiz_size=(Point(WEIGHT, HEIGHT)-2*Field_stats['El_SIZE']),
                                   el_size=Field_stats['El_SIZE'], visual=(True, 'images/', 'field_bg_'))
    # board_size = (Point(field.rect.topleft), Point(field.rect.bottomright))
    # board_vert = pg.image.load(f'images/board.png').convert_alpha()
    # board_vert = pg.transform.scale(board_vert, (board_size[0].x, board_size[1].y+board_size[0].y))
    # board_hor = pg.image.load(f'images/board.png').convert_alpha()
    # board_hor = pg.transform.scale(board_hor, (board_size[1].x+board_size[0].x, board_size[0].y))
    # boards = [(Point(0, 0), board_vert),
    #          (Point(board_size[1].x, 0), board_vert),
    #          (Point(0, 0), board_hor),
    #          (Point(0, board_size[1].y), board_hor)]
    boards = [(Point(0, 0), pg.transform.scale(pg.image.load(f'images/board_1.jpg').convert_alpha(), (WEIGHT, HEIGHT)))]

    pause_button = Menu.Button(win=win, pos=Point(0, 0), size=Field_stats['El_SIZE'], bg=['images/', 'buttons_'])

    objects['PlayScreen'] = Field.PlayScreen(win=win, pos=Point(), board=boards, field=field)
    objects['PlayScreen'].add_button(pause_button)

    objects['Player'] = Player.Player(pos=Player_stats['POS'], size=Player_stats['SIZE'], facing=Point(0, -1),
                                      speed=Player_stats['SPEED'], visual=(False, (0, 0, 255)), hp=Player_stats['HP'],
                                      defence=Player_stats['DEFENCE'], lvl=Player_stats['LVL'], exp=Player_stats['EXP'],
                                      n_exp=Player_stats['EXP_TO_TEXT_LVL'])


if __name__ == '__main__':
    pg.init()
    win = pg.display.set_mode((WEIGHT, HEIGHT))
    main(win)
