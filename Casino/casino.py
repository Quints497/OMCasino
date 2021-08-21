"""
Author: Oscar Miles\n
Date: 21/08/21
"""
from Accounts.accounts import Accounts

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
            signed = False

            if new:
                if new == "yes":
                    # setup the users account
                    self.account.sign_up()
                    print("\nNow login!\n")
                    signed = True
                elif new == "no" or signed:
                    # sign the user in
                    return self.account.login()
                else:
                    print("Please enter (yes or no)!")
                    continue
            else:
                print("Please enter something!")
                continue

    def run(self):
        pass


if __name__ == "__main__":
    cas = Casino()
    cas.new_user()


