import random
from function import monsterDungeonAlgoritm
from configs import *
import time

# Main code
def main():
    # Level and Monster Settings
    pickMonster = [goblin, orc, spider, ant]
    levelDungeon = 1
    monsterDungeon = monsterDungeonAlgoritm(pickMonster, levelDungeon)   
    
    
    print("Welcome To the Jungle \nYou Should Slains Every Monster!!!")
    while True:
        time.sleep(3)
        print("\nThere was a Monster")
        for no ,monster in enumerate(monsterDungeon):
            print(f"{no + 1}. {monster.name} ({monster.hp:,}HP) ({monster.att:,}Att)")
            time.sleep(.2)
        choice = int(input("Who you want to fight (Pick Number) : "))
        print("\n")
        
        if (choice > 0 and choice <= len(monsterDungeon)):
            choice -= 1
            jinwoo.attack(monsterDungeon[choice], levelDungeon)
            time.sleep(2)
            if (monsterDungeon[choice].hp <= 0): 
                monsterDungeon.pop(choice)
            else:   
                if (monsterDungeon[choice].attack(jinwoo, levelDungeon)): 
                    print("\nSorry Survival You was Lose, Maybe Try Again Next Time!!!")
                    break
        
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

# Gameplay
if __name__ == "__main__":
    main()
    