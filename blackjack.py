#!/usr/bin/env python3

"""
This contains the classes necessary to play a simple game of blackjack.

Classes present:

class Card: creates a card and can display information about it.

class Deck: creates a deck of card objects and can shuffle and deal them to a player or dealer.

class Hand: creates a hand of cards from the deck for the player and dealer,
and displays and calculates information about it.

class Game: runs the game(s) of blackjack.
"""
#TODO: refine documentation according to PEP standards and address warnings.

import random
from typing import Union, Dict, Any
from os import system
from time import sleep


class Card:
    def __init__(self, suit, rank):
        """
        Initializes a card object.
        :param suit:
        :param rank:
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Returns a card's suit and rank.
        :return: string in form: "rank of suit"
        """
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        """ Initializes a standard deck of card objects. """
        self.cards = []
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = [
            {"rank": "Ace", "value": 11}, 
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "Jack", "value": 10},
            {"rank": "Queen", "value": 10},
            {"rank": "King", "value": 10}
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """ Shuffles the deck of card objects. """
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        else:
            self.cards = self.cards

    def deal(self, number=1):
        """
        Deals player or dealer cards from the deck.
        :param number: optional, defaults to 1.
        :return: list of cards
        """
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        """
        Initializes a hand of cards.
        :param dealer: optional, defaults to False.
        """
        self.cards = []
        self.value = 0
        self.dealer = dealer
        self.has_ace = False

    def add_card(self, card_list):
        """
        Adds a card to the hand of cards from the current game's deck.
        :param card_list: intended to be added with the deal() method in the Hand class. Use other lists at your own peril.
        """
        self.cards.extend(card_list)

    def calculate_value(self):
        """ Calculates the value of the hand. """
        self.value = 0
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                self.has_ace = True

            if self.has_ace and self.value > 21:
                self.value -= 10

    def get_value(self):
        """
        Getter method for the current value of a hand.
        :return: self.value
        """
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        """ Checks if the hand is valued at a blackjack or not. """
        return self.get_value() == 21

    def display(self, show_all_dealers_cards=False):
        """
        Displays the dealer/player hand. Only the dealer's second card is shown if the optional
        parameter is set to False.
        :param show_all_dealers_cards: optional, defaults to False.
        """
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not show_all_dealers_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:", self.get_value())
        print()


class Game:
    def play(self):
        """ Begins and maintains the game(s) of blackjack. """
        game_number = 0
        games_to_play = 0

        # how many games menu
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games would you like to play?\n-: ")) #TODO: consider refactoring input validation/neutralization here
            except ValueError:
                print("You must enter a number to play...")
        
        self.clear_screen()

        while game_number < games_to_play:
            # if first game, do nothing, else issue menu 
            if game_number == 0:
                game_number += 1
            else:
                ready = 0
                #TODO: consider refactoring input validation/neutralization here
                while ready not in [1, 2]:
                    print()
                    print("Ready to continue to the next game?")
                    print("\t1. Yes (will go to the next game)")
                    print("\t2. No (will wait for 5 seconds and ask again)")
                    print("Enter either 1 or 2.\n-:")

                    try:
                        ready = int(input())
                        if ready == 1:
                            self.clear_screen()
                            game_number += 1
                        elif ready == 2:
                            sleep(5)
                            ready = 0
                    except ValueError:
                        print("You must enter either 1 or 2")
                        ready = 0

            # create deck of cards
            deck = Deck()
            deck.shuffle()
            
            # create player/dealer hand
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)
            
            # deal 2 cards
            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
            
            # initial in-game display
            print()
            print("*" * 30)  # divider
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue    # goes to the next game

            #TODO: consider refactoring input verification/neutralization for the below statements
            
            # Let player choose H/S
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand' (or H/S).\n-:").lower()
                print()
                while choice not in ["s", "stand", "h", "hit"]:
                    choice = input("Please choose 'Hit' or 'Stand' (or H/S).\n-:").lower()
                    print()
                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue    # goes to the next game
            
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            
            #TODO: look up why this is here; always document
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealers_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue  # goes to the next game

            print("Final Results: ")
            print("your hand:", player_hand_value)
            print("dealer's hand:", dealer_hand_value)
            
            self.check_winner(player_hand, dealer_hand, game_over=True)
    
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        """
        Checks if there is a winner.
        :param player_hand: intended to be used with the Hand class
        :param dealer_hand: intended to be used with the Hand class
        :param game_over: optional, defaults to False.
        :return:
        """
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! :(")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win! :)")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both players have a blackjack. It's a tie! :|")
                return True
            elif player_hand.is_blackjack():
                print("You have a blackjack. You win! :)")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins! :(")
                return True
        else:
            # This assumes that both players chose not to select more cards.
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! :)")
            elif player_hand.get_value == dealer_hand.get_value():
                print("It's a tie! :|")
            else:
                print("Dealer won! :(")
            return True
        return False

    #TODO: consider removing self made fn and just use system w/ a comment beside it
    def clear_screen(self):
        """
        Utility function that clears CLI when the user progresses to the next game.
        """
        system("clear")
