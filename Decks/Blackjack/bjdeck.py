"""
Author: Oscar Miles\n
Date: 20/8/21
"""
from Decks.deck import Deck

class BjDeck(Deck):
    """
    Used to store a collection of 312 Card objects
    Inherits from the Deck class

    ...

    Methods
    -------
    Inherited
    ---------
    create_deck():
        Fills the deck of cards with the Card objects
    shuffle_deck():
        Shuffles the deck of cards using the random shuffle() function
    Changed
    -------
    create_deck():
        Calls the super method create_deck() 6 times
    """
    def __init__(self):
        """
        Instantiates the bjdeck object with an empty deck of cards
        """
        super().__init__()

    def create_deck(self):
        """
        Calls the deck objects create_deck() method 6 times
        """
        for _ in range(6):
            super(BjDeck, self).create_deck()



