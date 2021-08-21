"""
Author: Oscar Miles\n
Date: 20/8/21
"""

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


