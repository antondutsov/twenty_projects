"""
Silly game for using "random" library
"""
import random

while True:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game over.")
        break

    if user_input == computer_input:
        print("It is a tie!")

    if (user_input == options[0] and computer_input == options[1]) or \
            (user_input == options[1] and computer_input == options[2]) or \
            (user_input == options[2] and computer_input == options[0]):
        print("Computer wins!")

    elif (computer_input == options[0] and user_input == options[1]) or \
            (computer_input == options[1] and user_input == options[2]) or \
            (computer_input == options[2] and user_input == options[0]):
        print("Player wins!")
