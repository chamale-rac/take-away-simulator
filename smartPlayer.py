import random


def play(dotsStock, maxMoves):
    limit = 2*maxMoves - 1

    for x in range(1, maxMoves+1):
        sub = dotsStock - x
        if((sub % limit == 0) or (sub == 0)):
            return x
    return random.randint(1, maxMoves)
