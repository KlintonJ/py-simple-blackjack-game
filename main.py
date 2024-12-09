#!/usr/bin/env python3

import blackjack as g
import re
from os import system


def check_input(user_input: str): 
    if re.match("^1$|^2$", user_input): return int(user_input) # regex here only allows a "1" or "2"
    else:
        user_input = ""
        return ValueError
    

if __name__ == '__main__':
    game = g.Game()
    choice = 0

    while choice not in [1, 2]:
        print("\nWhat would you like to do?")
        print("\t1. Play Blackjack.")
        print("\t2. Exit.")
        choice = input("Please enter either 1 or 2.\n-:")

        choice = check_input(choice)

        if choice == 1:
            system("clear")
            game.play()

            endgame_choice = 0
            while endgame_choice not in [1, 2]:
                print("What would you like to do?")
                print("\t1. Play again.")
                print("\t2. Exit.")
                endgame_choice = input("Please enter either 1 or 2.\n-:")
                endgame_choice = check_input(endgame_choice)

                if endgame_choice == 1:
                    system("clear")
                    game.play()
                    endgame_choice = 0
                    choice = 0
                    continue # TODO: consder using break to reduce lines
                elif endgame_choice == 2:
                    choice = 2
                    continue #TODO: consider using break to reduce lines
        elif choice == 2:
            print("\nThanks for playing!")
            break
        elif choice == ValueError:
            print("You must enter either 1 or 2. Try again...")
            continue

