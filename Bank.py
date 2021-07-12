class Bank:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self):
        amount = int(input("Enter the amount you want to deposit ->"))
        if(amount < 0):
            print("Please enter valid amount")
        else:
            self.balance += amount
            print(f"Your updated balance is {self.balance}")
    
    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw ->"))
        if(amount <= 0):
            print("Please enter valid amount")
        elif(amount > self.balance):
            print("You have insufficient funds. Please enter lesser aount and retry")
        else:
            self.balance -= amount
            print(f"Your updated balance is {self.balance}")
    
b = Bank("Tharun")
# b.withdraw()
# b.deposit()
# b.deposit()
# b.withdraw()
while(True):
    s = input("Please enter w for withdrawl or d for deposit or e for exit \n->")
    if(s=="w"):
        b.withdraw()
    elif(s=="d"):
        b.deposit()
    elif(s=="e"):
        print("Thanks for using our services. Have a nice day")
        break
    else:
        print("Please enter a valid input")