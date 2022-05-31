from field import FIELD
from random import randrange
import field


def easy_lev():
    while True:
        y, x = randrange(field.DIM), randrange(field.DIM)
        if not field.DIM[y][x]:
            return False
        return [y][x]


