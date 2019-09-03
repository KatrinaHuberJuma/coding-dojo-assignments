class Account:		# here's what we have so far
    def __init__(self, int_rate, balance=0, name='default'):
        self.int_rate = int_rate
        self.balance = balance
        self.name =name
        # print(f"interest rate: {self.int_rate} balance: {self.balance}")
        # adding the deposit method

    def deposit(self, amount):	
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_info(self):
        print(f"Rate: {self.int_rate}, Balance: ${self.balance}")
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


# beep = Account(.4, 20)
# bop = Account(.4)
# beep.deposit(20).deposit(20).deposit(20).withdrawal(30).yield_interest().display_info()
# bop.deposit(20).deposit(20).withdrawal(5).withdrawal(5).withdrawal(5).withdrawal(5).yield_interest().display_info()

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        print("welcome ", self.name)
        self.accounts = {'default': Account(.4, 0)}


    def make_deposit(self, amount, account="default"):	# takes an argument that is the amount of the deposit
        print(self.name, " has depositted $", amount)
        self.accounts[account].balance += amount
        print(f"User: {self.name}, Balance: ${self.accounts[account].balance}")
        return self

    def make_withdrawal(self, amount, account="default"):
        print(self.name, " has withdrawn $", amount)
        self.accounts[account].balance -= amount
        return self

    def display_user_balance(self, account='default'):
        print(f"User: {self.name}, Balance: ${self.accounts[account].balance}")
        return self

    def make_transfer(self, friend, amount, account="default"):
        
        if self.accounts[account].balance > amount:
            self.make_withdrawal(amount)
            print(f"User: {self.name}, Balance: ${self.accounts[account].balance}")
            friend.make_deposit(amount)
            
        else:
            print(self.name, " has insufficient funds.")
        return self
    
    def add_account(self, account_name, int_rate, balance=0):
        
        self.accounts[account_name] = Account(int_rate, balance)
        return self


jaqui = User("Jaqui", "Yay.com")
monty = User("Monty", "thebomb.com")
fred = User("Fred", "fredbread.said")
jaqui.make_deposit(200).display_user_balance().make_deposit(500).make_transfer(fred, 320)