import random

class Hero():
    """Attacking players in our game. The bully

        Attributes:
        name (str): name
        level (int) : level
    """
    def __init__(self, name="Herman", level=50, special="Thunderstruck!"):
        self.name = name
        self.level = level
        self.special = special

    def attack(self, opponent):
        hero_roll = random.randint(1,6) * self.level
        opponent_roll = random.randint(1,6) * opponent.level

        if hero_roll >= opponent_roll:
            return True
        else:
            return False

    def run(self):
        return "You ran like the little bitch you are!"

    def __str__(self):
        return f"{self.name} | {self.level} | {self.speacial}"


class Opponent():
    def __init__(self, name="Bob", level=45, special="Play Dead"):
        self.name = name
        self.level = level
        self.special = special

    def __str__(self):
        return f"Opponent {self.name} at {self.level} uses {self.special} special"


