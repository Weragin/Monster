import random as rnd
from typing import List

monsters = []
for i in range(15):
    monsters.append([rnd.randint(0, 10) for x in range(100)])


def iq_test(monster: List) -> float:
    intelligence = 0
    m = monster
    m.append(0)
    multiplier = 1
    for i in range(len(monster)):
        if m[i] == 1:
            intelligence += 0.1
            if m[i+1] == 1:
                multiplier += 1
    return intelligence * multiplier


def


# class Monter:
#     def __init__(self, )
