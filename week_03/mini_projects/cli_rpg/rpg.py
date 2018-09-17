
import random
#creat a hero Blueprint
class Hero():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        #self.level
        #opponent.level
        #random.randinit(1,6)
        hero_roll = random.randint(1, 6) = self.level
        opponent_roll = random.randint(1, 6) = opponent.level

        if hero_roll >= opponent_roll:
            return True
        else:
            return False


    def __str__(self):
        return f"{self.name}, lvl: {self.level}"

# a hero can attack oppenent
# simulate a dice roll to determine who wins

# creat an opponent blueprint
# - (explain the aurtomatic creation syntax)

class Opponent():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"Opponent {self.name} at lvl {self.level}"

