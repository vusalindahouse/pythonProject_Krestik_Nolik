from shutil import get_terminal_size as gts
import players
import help
import ai
DIM = 3
FIELD = [['']*DIM for _ in range(DIM)]
SYMBOLS = ("X", "O")


def field(*, right=False, center=False):
    if center:
        FIELD = [[f'{i}, {j}' for j in range(3)] for i in range(3)]

    mx = max([len(cell) for row in FIELD for cell in row])
    wd = mx*DIM + DIM*3 - 1
    margin = " "*((gts()[0] - 1 - wd)//2) if center else " "*(gts()[0] - 1 - wd) if right else " "
    rows = [margin + '|'.join([cell.center(mx+2) for cell in row]) for row in FIELD]

    print('\n' + ('\n' + margin + '-'*wd + '\n').join(rows) + '\n')
def check_win_or_tie():
    def check_win():
        FIELD_T = [[FIELD[i][j] for j in range(DIM)] for i in range(DIM)]

        DIAGONALS = [[FIELD[i][j] for i in range(DIM)],
                     [FIELD[i][DIM - i - 1] for i in range(DIM)]]

        for matrix in (FIELD, FIELD_T, DIAGONALS):
            if 1 in[len(set(row)) for row in matrix if all(row)]:
                return True

    return (win := check_win()), all([all(row) for row in FIELD]) and not win


def check_saves(*, single=True):
    global FIELD
    s = set(players.PLAYER)
    if single:
        s |= {'ai1', 'ai2'}
    for save in players.SAVES:
        if set(save).issubset(s):
            load = input(help.MESSAGES[6]).lower()
            if load in help.ANSWERS[6]:
                FIELD = players.SAVES[save]
                return save
    return False



def game_mode(load=False):
    global FIELD

    fl = set(players.PLAYER).isdisjoint({'ai1', 'ai2'})

    check_win_ = (False, False)
    while True:
        for i in range(2):
            prompt = ('делайте ход', f'ход игрока {players.PLAYER[i]}')[fl]

            if players.PLAYER[i].startwith('ai'):

                if load and not i:
                    load = False
                    continue

                y, x = ai.easy_lev() if players.PLAYER[i][-1] == '1' else ai.ai_turn(i)
            else:
                if load and len([cell for row in FIELD for cell in row if cell]) % 2 != i:
                    load = False
                    continue

                while True:
                    y, x = map(int, input(prompt).split())
                    if not FIELD[y][x]:
                        break
                    print('Эта клетка занята. Введите символ  в свободную клетку')
            FIELD[y][x] = SYMBOLS[i]

            field(right=bool(i))

            check_win_ = check_win_or_tie()

            if not any(check_win_):
                continue
            elif check_win_[0]:
                help.show_message(f"Победа за игроком{players.PLAYER[i]}")

                FIELD = [['']*3 for _ in range(3)]
                return {players.PLAYER[i]: [1, 0, 0]}, {players.PLAYER[i - 1]: [0, 1, 0]}
            elif check_win_[1]:
                help.show_message("Ничья")

                FIELD = [['']*3 for _ in range(3)]
                return {players.PLAYER[i]: [0, 0, 1]}, {players.PLAYER[i-1]: [0, 0, 1]}





