fees = 0
class BankAccount:
    def __init__(self, init_bal):

           #Creates an account w/ the given balance.
        self.init_bal = init_bal   # the init_bal is the initial amount the customer
        self.current_bal = init_bal # is starting off with. current_bal is the
        self.fees = fees        # updated balance after the operations are performed.

    def deposit(self, amount):

        #deposits the amount into the account
        self.amount = amount
        self.current_bal += amount

    def withdraw(self, amount):

        # withdraws the amount from the account. Each withdrawal resulting
        # in a negative balance also deducts a penalty fee of $5 from balance.

        self.current_bal -= amount
        if self.current_bal < 0:
            self.current_bal -= 5
            self.fees += 5

    def get_balance(self):

        #returns the current balance in the account
        return self.current_bal

    def get_fees(self):

        #returns the total fees ever deducted from the account
        return self.fees

my_account_1 = BankAccount(10)
my_account_1.withdraw(15)
my_account_1.deposit(20)
my_account_1.withdraw(25)
print my_account_1.get_balance(), my_account_1.get_fees()
# First, u have $10. Then u loose 15, plus an extra 5 b/c of the fee.
# Now u have -$10, but plus 20 makes it 10. Then take out 25-->
# 10-25= -15, then -5 for the fee--> -20.-20 is ur account balance.
# Your account fees were 5 the first over withdrawal, and 5 the 2nd time, making
# it 10 for total fees.
