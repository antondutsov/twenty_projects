import random


def roll_dice():
    roll = input("Ready to Roll the dices? (Yes/No): ")

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f" dice rolled: {dice1} and {dice2}")

        roll = input("Roll again? (Yes/No): ")


roll_dice()
