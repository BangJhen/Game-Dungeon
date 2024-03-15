import copy
import random

copyChar = lambda char : copy.copy(char)

# Algoritma untuk mengacak monster dalam dungeon
def monsterDungeonAlgoritm(allMonster : list, level : int) -> list:
    ''''Generate Monster Dungeon sesuai level'''
    probs = {}
    monsterDungeons = []
    for monster in allMonster:
        if monster.prob * level >= 10:
            probs[monster] = 10 - (monster.prob * level / 10)
        else:
            probs[monster] = monster.prob * level
    for prob in probs:
        monsterDungeons.extend([prob for i in range(int(probs[prob]))])

    return [copyChar(random.choice(monsterDungeons)) for i in range(1 + (level // 3))]
    