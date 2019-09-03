class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        # print(self.name, " has depositted $", amount)
        self.account_balance += amount

    def make_withdrawal(self, amount):
        # print(self.name, " has withdrawn $", amount)
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def make_transfer(self, friend, amount):
        
        if self.account_balance > amount:
            self.account_balance -= amount
            friend.make_deposit(amount)
        else:
            print(self.name, " has insufficient funds.")





jaqui = User("Jaqui", "yay.yay")
monty = User("Monty", "thebomb.com")
fred = User("Fred", "fredbread.said")

# jaqui.display_user_balance()
jaqui.make_deposit(100)
jaqui.make_deposit(200)
jaqui.make_deposit(400)
jaqui.display_user_balance()



# monty.display_user_balance()
monty.make_deposit(100)
monty.make_deposit(400)
monty.make_withdrawal(200)
monty.make_withdrawal(200)
monty.display_user_balance()

# fred.display_user_balance()
fred.make_deposit(100)
fred.make_withdrawal(400)
fred.make_withdrawal(200)
fred.make_withdrawal(200)
fred.display_user_balance()

print("===========================Oh, poor Fred! Jaqui loan him money!")

jaqui.make_transfer(fred, 650)
jaqui.display_user_balance()
fred.display_user_balance()
print("===========================Oh, poor Fred! Monty loan him money!")
monty.make_transfer(fred, 55)
monty.display_user_balance()
fred.display_user_balance()
