"""
Author: Oscar Miles\n
Date: 20/8/21
"""
import sys


class Accounts:
    """
    Used for signup and logging into your account

    ...

    Methods
    -------
    Static
    ------
    ask_username():
        Ask the user for the username of their account.
    ask_password():
        Ask the user for the password of their account.

    Public
    ------
    get_balance(username, password):
        Loop through the file and retrieve the balance from the username and password pair
    valid_info(username, password):
        Check that the information provided in currently stored in the file 'accounts.txt'
    sign_up():
        Call ask_username() and ask_password() and set the users balance to 1000.00 add this to 'accounts.txt'.
    login():
        Call ask_username() and ask_password() and if valid_info(username, password) returns True login.
    logout():
        Loop through the file and update the users balance to reflect the money made or lost in the casino, then exit.
    """
    # change this to the path of where your 'account.txt' is stored
    file = "/Users/oscarmiles/Desktop/Coding/Python/GitProjects/OMCasino/Accounts/accounts.txt"

    @staticmethod
    def ask_username():
        """
        Asks the user to enter a username, but the username can not be blank

        ...

        Returns
        -------
        userName : str
            The username chosen
        """
        while True:
            # ask user for username
            userName = input("Enter your username: ").rstrip()

            # check that username is not blank
            if userName:
                return userName
            else:
                print("Enter a username!")
                continue

    @staticmethod
    def ask_password():
        """
        Asks the user to enter the password for their account twice and both must match and cannot be blank

        ...

        Returns
        -------
        userPass : str
            The password chosen
        """
        while True:
            # ask user for password
            userPass = input("Enter your password: ").rstrip()

            # check userPass isn't blank
            if userPass:
                check = input("Enter your password again: ").rstrip()
            else:
                print("Enter a password!")
                continue

            # check userPass and check are the same
            if userPass == check:
                return userPass
            else:
                print("The passwords must match!")
                continue

    def get_balance(self, username, password):
        """
        Checks that the users account is valid. If so then return the users balance

        ...

        Parameters
        ----------
        username : str
            The username of the user you're looking for
        password : str
            The password of the user you're looking for

        Returns
        -------
        userBala : float
            The balance of the user you're looking for
        """
        with open(self.file, "r") as file:
            # loop through the file
            for line in file.readlines():
                data = line.rstrip()
                userName, userPass, userBala = data.split("|")
                # check if the user is in the file
                if userName == username and userPass == password:
                    return float(userBala)
                else:
                    continue

    def match(self, username, password):
        """
        Loops through the file looking and the username and password pairs, if they match the ones provided return True

        ...

        Parameters
        ----------
        username : str
            The username of the user you're looking for
        password : str
            The password of the user you're looking for

        Returns
        -------
        valid : bool
            Whether the username and password are in the 'accounts.txt' or not
        """
        match = True
        with open(self.file, "r") as file:
            # edge case - if no user has registered, looping through the file will produce an error.
            # so make sure there is more than one line in the file
            lines = file.readlines()

            # check edge case
            if len(lines) > 0:
                # loop through the file
                for line in lines:
                    data = line.rstrip()
                    userName, userPass, userBala = data.split("|")
                    # check that the user is in the file
                    if userName == username and userPass == password:
                        return match
            else:
                return not match

    def sign_up(self):
        """
        Asks the user for their details, initialises the balance and stores their information in 'accounts.txt'
        """
        print("\nWelcome new player!\n")

        # ask for details
        userName = self.ask_username()
        userPass = self.ask_password()
        userBala = 1000.00

        # if information matches - start again
        if self.match(username=userName, password=userPass):
            print("Try different information!")
            self.sign_up()
        else:
            with open(self.file, "a") as file:
                file.write(f"{userName}|{userPass}|{userBala}\n")

            print(f"{userName}'s account has been created!")

    def login(self):
        """
        Asks the user for their details and then checks if the details are in the system.
        """
        print("\nWelcome back old friend!\n")

        # ask for details
        userName = self.ask_username()
        userPass = self.ask_password()

        # if information matches - continue
        if self.match(username=userName, password=userPass):
            print(f"\nHello {userName}")
        else:
            print("Incorrect details!")

        # retrieve the users balance
        userBala = self.get_balance(username=userName, password=userPass)

        return userName, userPass, userBala

    def logout(self, username, password, balance):
        """
        Finds the user that is logging out in the file and changes the balance to what they ended the casino with.
        """
        print(f"\nGoodbye {username}\n")

        # read the file
        with open(self.file, "r") as in_file:
            lines = in_file.readlines()

        # write to the file
        with open(self.file, "w") as out_file:
            for line in lines:
                data = line.rstrip()
                userName, userPass, userBala = data.split("|")
                if userName == username and userPass == password:
                    out_file.write(f"{userName}|{userPass}|{balance}\n")
                else:
                    out_file.write(line)

        # exit the program
        sys.exit(0)


