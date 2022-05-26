
from players import *
from help import show_help, show_message, COMMANDS, MESSAGES


# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')


if read_ini():
    show_help()


while True:
    command = input(MESSAGES[0]).lower()


    if command in COMMANDS['quit']:
        break
    elif command in COMMANDS['help']:
        show_help()
    elif command in COMMANDS['scores']:
        pass
    elif command in COMMANDS['new']:
        if not PLAYER:
            player_name()
            pass
        else:
            pass