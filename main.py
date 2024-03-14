import copy
import random
class Char:

    def __init__(self, name : str, hp : int, att : int) -> None:
        self.name = name
        self.hp = hp
        self.att = att
        
    def attack(self, enemy, levelDung : int ) :
        ''''Menyerang ke musuh'''
        print(f"{enemy.name} \n{enemy.hp:,}HP (-{self.att:,}Dmg) ===> {(enemy.hp - self.att):,}HP")
        enemy.hp -= self.att
        
        if isinstance(self, Hero): # Win
            if enemy.hp <= 0:
                self.expUp(enemy= enemy, levelDung = levelDung)
                print(self)
            self.combo += 1
        elif isinstance(self, Monster): # Lose
            if enemy.hp <= 0: return True
               



class Monster(Char):
    def __init__(self, name : str, hp : int, att : int, prob : float) -> None:
        super().__init__(name, hp, att)
        self.prob = prob

class Hero(Char):
    def __init__(self, name : str, hp : int, att : int) -> None:
        super().__init__(name, hp, att)
        self.level = 1
        self.combo = 0
        self.exp = 0
        self.preqExp = (self.att * self.level) // 10

    def expUp(self, enemy, levelDung : int):
        self.exp += (enemy.att * levelDung) / 10
        
        if (self.exp >= self.preqExp):
            self.level += 1
            self.att += int(self.att * self.level * 0.08)
            self.hp += int(self.hp * self.level * 0.2)
            
            self.exp = 0
            self.preqExp = (self.att * self.level) // 10

    def __str__(self) -> str:
        return f"\nHero {' ' *  2}: {self.name} ({self.level} Level - {self.exp:,}/{self.preqExp:,}Exp) \nHealth : {self.hp:,} \nAttack : {self.att:,}"
    
    
class Assasin(Hero):
    def __init__(self, name : str, hp : int, att : int) -> None:
        super().__init__(name, hp, att)
        self.attBonus = int((att * self.level) / 10)
        self.heal = int((hp * self.level) /  75)

class Mage(Hero):
    def __init__(self, name : str, hp : int, att : int) -> None:
        super().__init__(name, hp, att)
        self.attBonus = int((att * self.level) / 7)
        self.heal = int((hp * self.level) /  50)

class Tank(Hero):
    def __init__(self, name : str, hp : int, att : int) -> None:
        super().__init__(name, hp, att)
        self.attBonus = int((att * self.level) / 4)
        self.heal = int((hp * self.level) /  50)


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
    
# Main code
def main():
    # Level and Monster Settings
    pickMonster = [goblin, orc, spider, ant]
    levelDungeon = 1
    monsterDungeon = monsterDungeonAlgoritm(pickMonster, levelDungeon)    
    
    
    print("Welcome To the Jungle \nYou Should Slains Every Monster!!!")
    while True:
        print("\nThere was a Monster")
        for no ,monster in enumerate(monsterDungeon):
            print(f"{no + 1}. {monster.name} ({monster.hp:,}HP) ({monster.att:,}Att)")
        choice = int(input("Who you want to fight (Pick Number) : "))
        print("\n")
        
        if (choice > 0 and choice <= len(monsterDungeon)):
            choice -= 1
            jinwoo.attack(monsterDungeon[choice], levelDungeon)
            
            if (monsterDungeon[choice].hp <= 0): 
                monsterDungeon.pop(choice)
            else:   
                if (monsterDungeon[choice].attack(jinwoo, levelDungeon)): break
                            
            if (len(monsterDungeon) <= 0):
                levelDungeon += 1
                monsterDungeon = monsterDungeonAlgoritm(pickMonster, levelDungeon)
                for monstDung in monsterDungeon:
                    monstDung.att += int(monstDung.att * levelDungeon * random.random())
                    monstDung.hp += int(monstDung.hp * levelDungeon * random.random())
                    
            
# Heroes 
hayabusa : Assasin = Assasin("Shin Hayabusa", 100, 10)
cyclop : Mage = Mage("One Eyes Cyclops", 90, 7)
jinwoo : Assasin = Assasin("Sung Jinwoo Shadow Monarch", 200, 10) # Ini Bakal jadi karakter OP
somat : Tank = Tank("Pak Somat The Conqueror", 150, 5)

# Monsters
goblin : Monster = Monster("Little Goblin", 20, 5, 1)
orc : Monster = Monster("Big Orc", 500, 100, .05)
spider : Monster = Monster("Spider Six Arm", 150, 70, .1)
ant : Monster = Monster("Ant Greek",50, 10, .4)

# monsterDungeon = [random.choice(pickMonster).name for i in range(5)]

# Gameplay
if __name__ == "__main__":
    main()
    