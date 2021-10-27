# *********************************************************
# Subj: Coding Dojo > Python > Fundamentals: User
# By:   Virgilio D. Cabading Jr.    Created: October 26, 2021
# *********************************************************

def print_all_users_info (user_array):                      # Go through an array of users and print their info
    for idx in range(len(user_array)):
        user_array[idx].info()

def print_desc(description:str):
    print(f"{f' {description} ':*^80}\n")

# //// CLASS USER /////////////////////////////////////////
class User:

    # **** CLASS METHODS **********************************
    def __init__(self) -> None:                             # Class Instance Constructor
        self.first_name = "John"
        self.last_name = "Doe"
        self.account_balance = 0;

    def make_deposit (self, amount=0):                      # Method that increases the user's account balance by amount
        self.account_balance += amount
        return self
    
    def make_withdrawal (self, amount):                     # Method that decreases the user's account_balance by specified amount
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):                         # Method display user balance
        print(f"{' Balance Information ':*^80}")
        print(f" User: {self.first_name} {self.last_name} ::: Balance: {self.account_balance}\n")
        return self
    
    def transfer_money (self, other_user, amount):     # Method to transfer an amount from user to another user
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
    
    def update_user_info (self, first_name="John", last_name="Doe", account_balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = account_balance
        return self

    def info(self):                                         # Method that displays info of class instance
        print(f"{f' {self.first_name} {self.last_name} Information ':*^80}")
        print(f"first_name : {self.first_name}")
        print(f"last_name : {self.last_name}")
        print(f"account_balance: {self.account_balance}\n")
        return self

# //// MAIN EXECUTABLE SECTION ////////////////////////////

user = []
user.append(User())                                         # Create 3 users
user.append(User())
user.append(User())

user[0].update_user_info("Vin", "Diesel", 1000)             # Initialize object their information
user[1].update_user_info("Brad", "Pitt", 1000)
user[2].update_user_info("Dwayne", "Johnson", 1000)

print_all_users_info(user)

print_desc("Depositing 100 for Vin Diesel")                 # Make a deposit
user[0].make_deposit(100)

user[0].display_user_balance()

print_desc("Depositing 200 for Vin Diesel")                 # Make a deposit
user[0].make_deposit(200)

user[0].display_user_balance()

print_desc("Depositing 500 for Vin Diesel")                 # Make a deposit
user[0].make_deposit(500)

user[0].display_user_balance()

print_desc("Withdrawing 200 from Vin Diesel")               # Make a withdrawal
user[0].make_withdrawal(200)


user[0].display_user_balance()                              # Display updated user balance

print_desc("Depositing 200 for Bradd Pitt")                 # Make a deposit
user[1].make_deposit(200)

user[1].display_user_balance()

print_desc("Depositing 600 for Brad Pitt")
user[1].make_deposit(600)

user[1].display_user_balance()

print_desc("Withdrawing 300 from Brad Pitt")                 # make a withdrawal
user[1].make_withdrawal(300)

user[1].display_user_balance()

print_desc("Withdrawing 200 from Brad Pitt")                 # make a withdrawal
user[1].make_withdrawal(200)

user[1].display_user_balance()

user[2].display_user_balance()

print_desc("The rock will make 3 deposits of 400 each")         # make 3 deposits
print_desc("The rock will make a withdrawal of 500")            # make a withdrawal

user[2].make_deposit(400).make_deposit(400).make_deposit(400).make_withdrawal(500).display_user_balance()

# user[2].display_user_balance()

# user[2].make_withdrawal(500)

# user[2].display_user_balance()

# Bonus: have the first user transfer money to the third user and then print both users' balances

print_desc("Bonus: have the first user transfer money to the third user and then print both users' balances")
print_all_users_info(user)

print_desc("Vin gives The Rock 300")
user[0].transfer_money(user[2], 300)

print_all_users_info(user)