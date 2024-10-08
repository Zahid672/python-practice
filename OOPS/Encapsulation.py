### Encapsulation: wrapping data and functions into a single unit (object)

### write a program that create Account class with 2 attributes- balance & account no.. create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

   


acc1 = Account(1000, 4321)
acc1.debit(10)
acc1.credit(50)
