

from players import PLAYER, SAVES
from help import MESSAGES, ANSWERS, COORDINATE

FIELD = [['']*3 for _ in range(3)]

def field():
    global FIELD
    result = ''
    for num in FIELD:
        result += f"{str(num)}\n"
    print(result)

def check_win(FIELD):
    c = COORDINATE
    for number in c:
        if FIELD[number[0]] == FIELD[number[1]] == FIELD[number[2]]:
            return FIELD[number[0]]
    return False


def check_saves(*, single=True):
    global FIELD
    s = set(PLAYER)
    if single:
        s |= {'ai1', 'ai2'}
    for save in SAVES:
        if set(save).issubset(s):
            load = input(MESSAGES[6]).lower()
            if load in ANSWERS[6]:
                FIELD = SAVES[save]
                return save
    return False
