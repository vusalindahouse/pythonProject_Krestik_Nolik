
from configparser import ConfigParser
import help
import field

SCORES = {}
# PLAYERS = {'Ivan': [1, 1, 0]}

PLAYER = tuple()
# PLAYER = ('ivan', 'ai1')

SAVES = {}
# SAVES = {('ivan', 'ai1'): [[]],
#          ('ivan', 'oleg'): [[]]}


def read_ini():
    global SCORES, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):

        SCORES = {name.title(): [int(n) for n in score.split(',')]
                  for name, score in config['Scores'].items()}

        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i+3]]
                      for i in range(0,9,3)]
                 for name, field in config['Saves'].items()}
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileNotFoundError


def save_ini():
    config = ConfigParser()
    config['Scores'] = {name: ','.join(str(n) for n in score)
                        for name, score in SCORES.items()}
    config['Saves'] = {';'.join(name):
                           ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config['General']['first'] = 'no'
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)

def player_name(bot_mode='', *, change_order=False):
    global PLAYER
    if len(PLAYER) == 0:
        PLAYER = (input(help.MESSAGES[1]).lower(),)
    elif len(PLAYER) == 1:
        if bot_mode:
            PLAYER = (PLAYER[0], bot_mode)
        else:
            PLAYER = (PLAYER[0], input(help.MESSAGES[2]).lower())
    if change_order:
        PLAYER = (PLAYER[1], PLAYER[0])



def game_mode():
    global PLAYER
    while True:
        gm = input(help.MESSAGES[3]).lower()
        if gm in help.ANSWERS[3]:
            break
    if gm in help.ANSWERS[3][:3]:
        if save := field.check_saves():
            PLAYER = save
            return True
        while True:
            dl = input(help.MESSAGES[4]).lower()
            if dl in help.ANSWERS[4]:
                break
        if dl in help.ANSWERS[4][:3]:
            dl = 'ai1'
        else:
            dl = 'ai2'
        player_name(dl)
    else:
        player_name()
        if save := field.check_saves(single=False):

            PLAYER = save
            return True


    if not (input(help.MESSAGES[5]).lower() in help.ANSWERS[5]):
        player_name(change_order=True)


def show_stat():
    config = ConfigParser()
    config.read('data.ini')
    print('?????????????? ????????????????????')
    print()
    for name, score in config['Scores'].items():
        print (name, '=', score)