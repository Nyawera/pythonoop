


class Account:

    
    def __init__(self,account_number,account_name,balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance=balance
   
    

    def deposit(self,amount):
        current=self.balance-amount
        return f"your deposit is {amount} in account{self.account_number}. The balance is{current}"
    
       
        
        

    def withdraw(self,amount2):
        current2=self.balance-amount2
        return f"your withdraw is {amount2} in account {self.account_number}. The balance is {current2}"
    
   


    
    