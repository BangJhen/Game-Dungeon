import copy
import math
import random
class Char:

    def __init__(self, name, hp, att) -> None:
        self.name = name
        self.hp = hp
        self.att = att
        
    def attack(self, enemy):
        print(f"\n{enemy.name} \n{enemy.hp}HP (-{self.att}Dmg) ===> {enemy.hp - self.att}HP\n")
        enemy.hp -= self.att
        if isinstance(self, Hero):
            if enemy.hp <= 0:
                self.upLevel()
            self.combo += 1


class Monster(Char):
    def __init__(self, name, hp, att, prob) -> None:
        super().__init__(name, hp, att)
        self.prob = prob

class Hero(Char):
    def __init__(self, name, hp, att) -> None:
        super().__init__(name, hp, att)
        self.level = 1
        self.combo = 0

    def upLevel(self):
        self.level += 1
        self.att += self.att * self.level * 0.5
        self.hp += self.hp * self.level * 0.75

    def __str__(self) -> str:
        return f"Hero {' ' *  2}: {self.name} ({self.level} Lvl) \nHealth : {self.hp} \nAttack : {self.att}"
class Assasin(Hero):
    def __init__(self, name, hp, att) -> None:
        super().__init__(name, hp, att)
        self.attBonus = int((att * self.level) / 10)
        self.heal = int((hp * self.level) /  75)

class Mage(Hero):
    def __init__(self, name, hp, att) -> None:
        super().__init__(name, hp, att)
        self.attBonus = int((att * self.level) / 7)
        self.heal = int((hp * self.level) /  50)

class Tank(Hero):
    def __init__(self, name, hp, att) -> None:
        super().__init__(name, hp, att)
        self.attBonus = int((att * self.level) / 4)
        self.heal = int((hp * self.level) /  50)




def main():
    pass

def copyChar(char):
    return copy.copy(char)

# Algoritma untuk mengacak monster dalam dungeon
def monsterDungeonAlgoritme(allMonster, level):
    probs = {}
    monsterDungeons = []
    for monster in allMonster:
        if monster.prob * level >= 10:
            probs[monster] = 10 - (monster.prob * level)
        else:
            probs[monster] = monster.prob * level
            
    for prob in probs:
        monsterDungeons.extend([prob for i in range(int(probs[prob]))])

    return [random.choice(monsterDungeons) for i in range(5 + (level // 3))]
    
            
# Heroes 
hayabusa : Assasin = Assasin("Shin Hayabusa", 100, 10)
cyclop : Mage = Mage("One Eyes Cyclops", 90, 7)
jinwoo : Assasin = Assasin("Sung Jinwoo Shadow Monarch", 200, 10) # Ini Bakal jadi karakter OP
somat : Tank = Tank("Pak Somat The Conqueror", 500, 5)

# Monsters
goblin : Monster = Monster("Little Goblin", 15, 2, 8)
orc : Monster = Monster("Big Orc", 50, 10, 1)
spider : Monster = Monster("Spider Six Arm", 35, 7, 2)
ant : Monster = Monster("Ant Greek",20, 4, 5)

levelDungeon = 1

pickMonster = [goblin, orc, spider, ant]

# monsterDungeon = [random.choice(pickMonster).name for i in range(5)]
monsterDungeon = monsterDungeonAlgoritme(pickMonster, levelDungeon)



if __name__ == "__init__":
    main()
    

# print("Welcome To the Jungle \nYou Should Slains Every Monster!!!\n")
# while sum(monsterDungeon.values()) > 0:
#     totalMonster = 0
