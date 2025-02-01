class BankAccount():
    def __init__(self,name,account_no,balance=0):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Deposited amount {amount} and Total balance is {self.balance}')
        else:
            print("Enter valid amount to deposit")
    
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn money is {amount} and total balance is {self.balance}")
            
        else:
            print("enter correct amount to withdraww")
            
account=BankAccount("Sandeep",12345,500)

account.deposit(1000)
account.withdraw(200)
account.withdraw(500)
account.deposit(100)
