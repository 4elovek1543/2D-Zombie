import pygame as pg
from class_Point import Point
from CONFIG import objects
import Auxiliary_Classes
from functions import dist


def bullet_throw(amount):
    if amount > 0:
        player = objects['Player']
        pos = Point(player.pos.x+player.size.x//2,  player.pos.y+player.size.y//2)
        size = player.size.y//10
        bullet = Auxiliary_Classes.Bullet(pos=pos, size=size, dmg=player.attack, facing=player.facing,
                                          speed=player.speed*3, visual=(255, 0, 0))
        objects['Bullets'].append(bullet)
        return amount-1
    else:
        return 0


def grenade_throw(amount):
    if amount > 0:
        player = objects['Player']
        pos = Point(player.pos.x+player.size.x//2,  player.pos.y+player.size.y//2)
        size = player.size.y//10
        grenade = Auxiliary_Classes.Grenade(pos=pos, size=size, dmg=player.attack, rad=size*70, facing=player.facing,
                                            speed=player.speed*3, visual=(255, 201, 14))
        objects['Grenades'].append(grenade)
        return amount-1
    else:
        return 0


def hand_attack():
    player = objects['Player']
    pass

