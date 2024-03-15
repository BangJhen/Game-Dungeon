from abc import ABC, abstractmethod

class Char:

    def __init__(self, name : str, hp : int, att : int) -> None:
        self.name = name
        self.hp = hp
        self.att = att
    
    @abstractmethod    
    def attack(self, enemy, levelDung : int ) :
        ''''Menyerang ke musuh'''
        print(f"{enemy.name} \n{enemy.hp:,}HP (-{self.att:,}Dmg) ===> {(enemy.hp - self.att):,}HP")
        enemy.hp -= self.att
        print("Berhasil")
        
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
        self.__exp = 0
        self.__preqExp = (self.att * self.level) // 10

    @abstractmethod
    def expUp(self, enemy, levelDung : int):
        self.__exp += (enemy.att * levelDung) / 10
        
        if (self.__exp >= self.__preqExp):
            self.level += 1
            self.att += int(self.att * self.level * 0.08)
            self.hp += int(self.hp * self.level * 0.2)
            
            self.__exp = 0
            self.__preqExp = (self.att * self.level) // 10

    def __str__(self) -> str:
        return f"\nHero {' ' *  2}: {self.name} ({self.level} Level - {self.__exp:,}/{self.__preqExp:,}Exp) \nHealth : {self.hp:,} \nAttack : {self.att:,}"
    
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

