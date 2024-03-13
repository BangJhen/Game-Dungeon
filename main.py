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
        super().__init__(name, hp, att, prob)

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
        self.attBonus = int((att * self.level) / 5)
        self.heal = int((hp * self.level) /  50)


def copyChar(char):
    return copy.copy(char)

def monsterDungeon(allMonster, levelDungeon):

# Hero 
hayabusa : Assasin = Assasin("Shin Hayabusa", 100, 10)
cyclop : Mage = Mage("One Eyes Cyclops", 90, 7)

# Monster
goblin : Monster = Monster("Little Goblin", 15, 2, 0.8)
orc : Monster = Monster("Big Orc", 50, 10, 0.2)
spider : Monster = Monster("Spider Six Arm", 35, 7, 0.2)
ant : Monster = Monster("Ant Greek",20, 4, 0.5)

levelDungeon = 1

allMonster = [goblin, orc, spider, ant]

monsterDungeon = [random.choice(allMonster).name for i in range(5)]
print(monsterDungeon)




# print("Welcome To the Jungle \nYou Should Slains Every Monster!!!\n")
# while sum(monsterDungeon.values()) > 0:
#     totalMonster = 0
