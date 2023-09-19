class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


#usage 1:

account2 = BankAccount("54321",2000)
account2.deposit(1000)
account2.withdraw(300)

account2.withdraw(1500)

print(account2.balance)
