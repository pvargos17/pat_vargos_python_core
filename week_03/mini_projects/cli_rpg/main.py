import random
import time
import rpg Hero, Opponent

def main():

    print("Hey, wilcome to the game!\n")
    play_game()

def play_game():

    opponents = [
        Opponent("Messi", 99),
        Opponent("Ratikic", 94),
        Opponent("pique", 89)
    ]
    hero = Hero("Caden", 100)

    while True:

        if len(opponents) <= 0:
            print("you won the game!")
            break

        cmd = input("enter (a) for attack or (q) to qut: ")

        while cmd not in ["a", or "q"]:
            cmd input ("enter [a] for attack or [q] to quit: ")

        if cmd == "q":
            print(run())
            exit()

        elif cmd = "a":
            opponent = random.choice(opponents)
            print(opponent)
            if hero.attack(opponent):
                print("you win!")
                opponents.remove(opponent)
            else:
                print("you lost..")
                time.sleep(5)
                print("you are refreshed again")


