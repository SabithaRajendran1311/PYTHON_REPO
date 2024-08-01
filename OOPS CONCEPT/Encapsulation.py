class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insuffient balance!")
    def get_balance(self):
        return self.__balance
account=BankAccount("12345",1000)
account.deposit(500)
account.withdraw(300)
print(f"Account balance:{account.get_balance()}")
    
