"""
Author: Oscar Miles\n
Date: 20/8/21
"""
from Characters.player import Player

class BjPlayer(Player):
    """
    Used to store information about the player when they are in blackjack
    Inherits from the Player class

    ...

    Attributes
    ----------
    username : str
        The users username
    password : str
        The users password
    balance : float
        The users balance
    cards : list
        The users cards
    """
    def __init__(self, username, password, balance):
        super(BjPlayer, self).__init__(username=username, password=password, balance=balance)
        self.cards = []
