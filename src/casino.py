"""
Author: Oscar Miles\n
Date: 21/08/21
"""
from src.accounts import Accounts
from src.blackjack import Blackjack

class Casino:
    """
    This is where all of the classes will interact with each other

    - Accounts : used to setup the users account
    - Characters : keep hold of the users details during the games
    - Games : the users characters will interact with the games
    """
    def __init__(self):
        self.account = Accounts()

    def new_user(self):
        # ask if the user is new or not
        while True:
            new = input("Are you a new user: ").strip().lower()

            if new:
                if new == "yes":
                    # setup the users account
                    self.account.sign_up()
                    print("\nNow login!\n")
                elif new == "no":
                    # sign the user in
                    return self.account.login()
                else:
                    print("Please enter (yes or no)!")
                    continue
            else:
                print("Please enter something!")
                continue

    def run(self):
        # sign up / login
        username, password, initial_balance = self.new_user()

        while True:
            game_mode = input("[1 : Blackjack]: ").strip().lower()

            if game_mode:
                if game_mode == "1":
                    blackjack = Blackjack(username=username, password=password, balance=initial_balance)
                    after_balance = blackjack.run()
                    break
                else:
                    print("No other games at the moment!")
            else:
                print("Please enter a value!")

        self.account.logout(username=username, password=password, balance=after_balance)


if __name__ == "__main__":
    cas = Casino()
    cas.run()
