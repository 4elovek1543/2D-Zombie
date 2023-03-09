from class_Point import Point

FULL = False

HEIGHT = 720
WEIGHT = 1120

NAME = '2D ZOMBIE'
VERSION = 1.0

FPS = 40

# stats
Field_stats = {
    'El_SIZE': Point(40, 40)
}
Player_stats = {
    'SIZE': Point(40, 40),
    'POS': Point((WEIGHT-40)//2, (HEIGHT-40)//2),
    'SPEED': 5,
    'HP': 100,
    'DEFENCE': 1.0,
    'LVL': 1,
    'EXP': 0,
    'EXP_TO_TEXT_LVL': 100
}
Zombie_stats = {
    'SIZE': Point(60, 60),
    'POS': Point(0, 0),
    'SPEED': 2,
    'HP': 100,
    'DEFENCE': 1.0,
    'COST': 10
}

# global objects

objects = {
    'PlayScreen': None,
    'Player': None,
    'Zombies': [],
    'Bullets': [],
}
