class Account:		# here's what we have so far
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.account_balance = balance
        # print(f"interest rate: {self.int_rate} balance: {self.account_balance}")
        # adding the deposit method

    def deposit(self, amount):	
        self.account_balance += amount
        return self

    def withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Rate: {self.int_rate}, Balance: ${self.account_balance}")
        return self


    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
        return self

beep = Account(.4, 20)
bop = Account(.4)
beep.deposit(20).deposit(20).deposit(20).withdrawal(30).yield_interest().display_account_info()
bop.deposit(20).deposit(20).withdrawal(5).withdrawal(5).withdrawal(5).withdrawal(5).yield_interest().display_account_info()

    # def transfer(self, friend, amount):
        
    #     if self.account_balance > amount:
    #         self.make_withdrawal(amount)
    #         friend.make_deposit(amount)
            
    #     else:
    #         print(self.name, " has insufficient funds.")
        
    #     return self