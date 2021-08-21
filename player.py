"""
Author: Oscar Miles\n
Date: 20/8/21
"""

class Player:
    """
    Used to store the users information whilst they are playing in the casino

    ...

    Attributes
    ----------
    username : str
        The users username
    password : str
        The users password
    balance : float
        The users balance
    """
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
