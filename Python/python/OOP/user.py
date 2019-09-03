class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        print(self.name, " has depositted $", amount)
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        print(self.name, " has withdrawn $", amount)
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def make_transfer(self, friend, amount):
        
        if self.account_balance > amount:
            self.make_withdrawal(amount)
            friend.make_deposit(amount)
            
        else:
            print(self.name, " has insufficient funds.")
        
        return self





jaqui = User("Jaqui", "yay.yay")
monty = User("Monty", "thebomb.com")
fred = User("Fred", "fredbread.said")

print("#############  The Story Of Jaqui  ##########")
# jaqui.display_user_balance()
jaqui.make_deposit(100).make_deposit(200).make_deposit(400).display_user_balance()



# monty.display_user_balance()
print("#############  The Story Of Monty  ##########")
monty.make_deposit(100).make_deposit(400).make_withdrawal(200).make_withdrawal(200).display_user_balance()


print("#############  The Story Of Fred  ##########")
# fred.display_user_balance()
fred.make_deposit(100).make_withdrawal(400).make_withdrawal(200).make_withdrawal(200).display_user_balance()

print("############  Oh, poor Fred! Jaqui loan him money!  ################")

jaqui.make_transfer(fred, 650).display_user_balance()
fred.display_user_balance()
print("############  Oh, poor Fred! Monty loan him money!  ################")
monty.make_transfer(fred, 55).display_user_balance()
fred.display_user_balance()
