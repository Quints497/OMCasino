"""
Author: Oscar Miles\n
Date: 20/8/21
"""
import time

from Characters.Blackjack.bjplayer import BjPlayer
from Characters.Blackjack.bjdealer import BjDealer
from Decks.Blackjack.bjdeck import BjDeck

class Blackjack:
    """
    Used to store the information about the blackjack game

    ...

    Parameters
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    balance : float
        The balance of the user

    Attributes
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    balance : float
        The balance of the user
    user : BjPlayer
        The users in game player
    dealer : BjDealer
        The dealer
    deck : BjDeck
        The deck of 312 cards to be used
    """
    def __init__(self, username, password, balance):
        """
        Instantiates blackjack table with a user, dealer and deck objects
        """
        self.user = BjPlayer(username=username, password=password, balance=balance)
        self.dealer = BjDealer()
        self.deck = BjDeck()
        self.running = False
        self.round = 0

    @staticmethod
    def total_value(player):
        """
        Add up the total value of the specified players hand

        ...

        Parameters
        ----------
        player : BjPlayer or BjDealer
            Either the user or the dealer

        Returns
        -------
        total : int
            The total value of the cards in the hand
        """

        total = 0
        for card in player.hand:
            if card.value == "A" and total + card.cost > 21:
                card.cost = 1
                total += card.cost
            total += card.cost
        return total

    @staticmethod
    def show_a_hand(player):
        """
        Prints all of the players cards
        """
        print(f"{player.username}'s hand")
        for card in player.hand:
            print(card)

    def clear_hands(self):
        """
        Clears the hands of the user and of the dealer
        """
        self.user.hand = []
        self.dealer.hand = []

    def ask_for_bet(self):
        """
        Ask the user for their bet amount
        """
        print(f"{self.user.username} balance: £{self.user.balance}\n\n")
        while True:
            bet = float(input(f"{self.user.username} bet amount: £"))

            if bet:
                if self.user.get_balance() - bet >= 0:
                    self.user.set_balance(self.user.get_balance() - bet)
                    break
                else:
                    print(f"Insufficient funds, your balance: £{self.user.balance}")
            else:
                print("See you later!")
                break

        return bet

    def deal(self, player):
        """
        Take the first card from the deck and add it to the specified players hand

        Parameters
        ----------
        player : BjPlayer or BjDealer
            Either the user or the dealer
        """
        player.hand.append(self.deck.deck_of_cards[0])
        self.deck.deck_of_cards.pop(0)

    def show_first_hand(self):
        """
        Prints the first two cards from the user and the first card from the dealer
        """
        print(f"{self.user.username}'s hand!")
        for card in self.user.hand:
            print(card)

        print(f"{self.dealer.username}'s first card!")
        print(self.dealer.hand[0])

    def hit_stand(self):
        """
        Ask the user if they want to hit or stand, calculating their score after each hit.
        The user can only exit if they stand or go bust.
        """
        while True:
            # calculate the hand total
            current = self.total_value(self.user)

            # show the players hand
            self.show_a_hand(self.user)

            # ask if the user wants to hit or stand
            cmd = input(f"Current total: {current} - hit or stand: ").strip().lower()

            # check user entered something
            if cmd:
                if cmd == "hit":
                    self.deal(player=self.user)
                    if self.total_value(self.user) > 21:
                        print(f"{self.user.username} went bust with {self.total_value(self.user)}")
                elif cmd == "stand":
                    print(f"{self.user.username} stood on {current}")
                    break
                else:
                    print("Enter hit or stand!")
                    continue
            else:
                print("Enter hit or stand! Not nothing")
                continue

        self.show_a_hand(self.dealer)

    def dealer_plays(self):
        """
        The dealer will hit until soft 17, if the dealer's total is on or above 17 after hitting they must stand
        The dealer will keep hitting until this condition is met
        """
        while self.total_value(self.dealer) <= 17:
            self.deal(self.dealer)
            self.show_a_hand(self.dealer)

    def compare(self):
        """
        Calculate the scores of both the user and the dealer and see which score is higher

        Returns
        -------
        2:
            The player has won with blackjack
        1:
            The player has won normally
        0:
            The player and dealer have tied
        -1:
            The player has lost
        """
        users_score = self.total_value(self.user)
        dealers_score = self.total_value(self.dealer)

        if len(self.user.hand) == 2:
            if users_score == 21:
                if dealers_score != 21:
                    return 2

        if users_score <= 21:
            if dealers_score <= 21:
                # user beats the dealer
                if users_score > dealers_score:
                    print(f"{self.user.username}'s {users_score} beats {self.dealer.username}'s {dealers_score}")
                    return 1
                # user and dealer draw
                elif users_score == dealers_score:
                    return 0
                # user loses to the dealer
                elif users_score < dealers_score:
                    print(f"{self.dealer.username}'s {dealers_score} beats {self.user.username}'s {users_score}")
                    return -1
            # dealer went bust
            else:
                print(f"{self.dealer.username}'s {dealers_score} is over 21!")
                return 1
        else:
            print(f"{self.user.username}'s {users_score} is over 21!")
            return -1

    def end_of_round(self, condition, bet):
        """
        Determines what message to display and what to do with the users bet

        ...

        Parameters
        ----------
        condition : int
            (2, player blackjack) (1, player wins) (0, push) (-1, dealer wins)
        bet : float
            (2, returns 3/2) (1, returns 2/1) (0, returns 1/1), (-1, returns 0)
        """
        if condition == 2:
            amount = 3 * bet / 2 + bet
            print(f"{self.user.username} won £{amount}!")
            self.user.balance += amount
        elif condition == 1:
            amount = 2 * bet / 1
            print(f"{self.user.username} won £{amount}!")
            self.user.balance += amount
        elif condition == 0:
            print(f"Push £{bet} returned!")
            self.user.balance += bet
        elif condition == -1:
            print(f"{self.user.username} lost £{bet}")
        else:
            raise ValueError("Condition needs to be either [2, 1, 0, -1]!")

    def run(self):
        """
        This is where all the methods are tied together to run the game of blackjack

        ...

        Returns
        -------
        balance : float
            The users balance
        """

        ''' Initialisation '''
        # create the deck
        self.deck.create_deck()
        self.running = True

        while self.running:
            # add 1 to the round count
            self.round += 1

            # when to shuffle the deck
            if self.round == 1 or self.round == 15:
                print("Shuffling!")
                self.deck.shuffle_deck()
                time.sleep(0.5)
                print("Shuffled!")
                if self.round == 15:
                    self.round = 0

            # ask for bet
            bet = self.ask_for_bet()

            if bet == 0:
                self.running = False
                return self.user.balance

            # deal the cards
            for _ in range(2):
                self.deal(self.user)
                self.deal(self.dealer)

            # show the hands
            self.show_first_hand()

            # ask user to hit or stand
            self.hit_stand()

            # dealers turn to hit
            self.dealer_plays()

            # compare the scores of their hands
            result = self.compare()

            # show who the winner is
            self.end_of_round(condition=result, bet=bet)

            # clear the hands
            self.clear_hands()

            # ask user to play again
            while True:
                again = input("Do you want to play another round: ").strip().lower()

                if again:
                    if again == "yes":
                        break
                    elif again == "no":
                        self.running = False
                        print("Goodbye! Thank you for playing blackjack!")
                        return self.user.balance
                    else:
                        print("Please enter (yes or no)!")
                        continue
                else:
                    print("Please enter at least something!")
                    continue

if __name__ == "__main__":
    black = Blackjack("oscar", "miles", 1000.00)

    black.run()