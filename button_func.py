import pygame as pg
import Mainloop


def start_func(args=None):
    Mainloop.main(args)
    return args


def menu_call(args=None):
    args.proces()
    return args
