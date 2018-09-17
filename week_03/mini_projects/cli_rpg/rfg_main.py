import time
import RPG_start
#from RPG_start import *
import random

def main():
    print("Hello there! Ready to get tough?")
    play_game()

def play_game():

    opponents = [RPG_start.Opponent("Pikachu", 33, "Wild Charge"),
    RPG_start.Opponent("Onix", 40, "Iron Tail"),
    RPG_start.Opponent("Goldeen", 1, "Flail")]


    hero = RPG_start.Hero("Patrick", 10, "Body Slam")

    while True:

        if len(opponents) <= 0:
            return "Congrats you defeated a bunch of defenseless pokemon"
            break

        cmd = input("enter (a) for attack or (r) to run: ")

        while cmd not in ["a", "r"]:
            cmd = input("enter [a] for attack or [r] to run: ")

        if cmd == "r":
            print("You ran like the little bitch you are")
            exit()

        elif cmd == "a":
            opponent = random.choice(opponents)
            print(opponent)
            if hero.attack(opponent):
                print("you win!")
                opponents.remove(opponent)
            else:
                print("you lost..")
                time.sleep(5)
                print("you are refreshed again")

if __name__ == '__main__':
    main()
