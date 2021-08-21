"""
Author: Oscar Miles\n
Date: 20/8/21
"""
from random import shuffle

class Card:
    """
    Used to store the information of a playing card

    ...

    Attributes
    ----------
    suit : str
        The suit of the card
    value : str
        The value of the card
    cost : int
        The points the card is worth
    """
    def __init__(self, suit, value, cost):
        self.suit = suit
        self.value = value
        self.cost = cost

    def __repr__(self):
        """
        How a card object is printed

        ...

        Returns
        -------
        representation : str
            The string representation of a card object
        """
        representation = f" --------------- \n" \
                         f"|\t\t{self.value}\t\t|\n" \
                         f"|\t\t \t\t|\n" \
                         f"|\t\t \t\t|\n" \
                         f"|\t\t{self.suit}\t\t|\n" \
                         f"|\t\t \t\t|\n" \
                         f"|\t\t \t\t|\n" \
                         f"|\t\t{self.value}\t\t|\n" \
                         f" --------------- "
        return representation


class Deck:
    """
    Used to store a collection of 52 Card objects

    ...

    Attributes
    ----------
    deck_of_cards : list
        Holds the 52 card objects

    Methods
    -------
    create_deck():
        Fills the deck of cards with the Card objects
    shuffle_deck():
        Shuffles the deck of cards using the random shuffle() function
    """
    def __init__(self):
        """
        Instantiates the deck object with an empty deck of cards
        """
        self.deck_of_cards = []

    def create_deck(self):
        """
        Loops through a list of suits and a list of values and stores them in the card object.\n
        The card is then added to the end of the deck of cards
        """
        # S = Spades, C = Clubs, H = Hearts, D = Diamonds
        suits = ["S", "C", "H", "D"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # loop through the suit and values
        for suit in suits:
            for value in values:
                if value in ["A", "J", "Q", "K"]:
                    if value == "A":
                        cost = 11
                    else:
                        cost = 10
                else:
                    cost = int(value)

                self.deck_of_cards.append(Card(suit=suit, value=value, cost=cost))
        else:
            print("Deck created!")

    def shuffle_deck(self):
        """
        The deck of cards is shuffled using the random shuffle function
        """
        shuffle(self.deck_of_cards)

    def show_deck(self):
        """
        Loops through the deck of cards and prints each card
        """
        for card in self.deck_of_cards:
            print(card)
