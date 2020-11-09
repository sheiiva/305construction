############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

EMPTY_SQUARE    = '0'
WALL            = '1'
GHOST           = 'F'
PACMAN          = 'P'

X = 0
Y = 1


def UP(x: int, y: int) -> tuple:
    return (x, y-1)


def RIGHT(x: int, y: int) -> tuple:
    return (x+1, y)


def DOWN(x: int, y: int) -> tuple:
    return (x, y+1)


def LEFT(x: int, y: int) -> tuple:
    return (x-1, y)


DIR = {"UP": UP, "RIGHT": RIGHT, "DOWN": DOWN, "LEFT": LEFT}


def GETUP(list: list, x: int, y: int):
    return list[y-1][x]


def GETRIGHT(list: list, x: int, y: int):
    return list[y][x+1]


def GETDOWN(list: list, x: int, y: int):
    return list[y+1][x]


def GETLEFT(list: list, x: int, y: int):
    return list[y][x-1]


GETDIR = {"UP": GETUP, "RIGHT": GETRIGHT, "DOWN": GETDOWN, "LEFT": GETLEFT}


def isDigit(elem) -> bool:

    try:
        int(elem)
    except ValueError:
        return False
    else:
        return True
