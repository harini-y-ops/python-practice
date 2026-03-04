class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        print(f"Amount deposited is {amount}")
    def withdraw(self,amount):
        self.amount=amount
        if amount>self.balance:
            print("Insufficient balance")
        else:
            print(f"Amount withdrawn is {amount}")
    def check_balance(self):
        print(f"{self.owner}'s balance is {self.amount}")
        
account=BankAccount("harini",1000)
account.deposit(2000)
account.withdraw(5000)
account.check_balance()
        
