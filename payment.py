# user input
# select payment method
# gateway
# basic transaction
# success or failure message


# user interaction
# create bank account - balance, pin

class Bank():
    def __init__(self, pin, balance = 0):
        self.balance = balance
        self.pin = pin

    def verifyPin(self, user_pin):
        if user_pin != self.pin:
            raise ValueError ('Invalid Pin')
        
    def reset_pin(self, old_pin, new_pin):
        self.verifyPin(old_pin)
        self.pin = new_pin
        print("Pin reset")

class ATM:
    def __init__(self, account):
        self.account = account
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Invalid withdaw amount')
        if amount > self.account.balance:
            raise ValueError('Insufficient balance')

        self.account.balance -= amount
        print('Money withdraw')

    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError('Invalid deposit amount')
            self.account.balance += amount
        print('Money withdraw')
        

    def checkBalance(self):
        print(self.account.balance)        

account = Bank('1234', 100000)
atm = ATM(account)

try:
    pin = input('Enter your pin: ')
    account.verifyPin(pin)

    while(True) :


        print(" ATM Menu")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Reset")

        choice = input("Choose option")

        match choice:
            case "1": 
                amount = int(input("Enter withdraw amount :"))
                atm.withdraw(amount)
            
            case "2":
                amount = int(input("Enter amount :"))
                atm.deposit(amount)
            
            case "3":
                atm.checkBalance()
            
            case "4":
                old_pin = input('Enter your current pin: ')
                new_pin = input('Enter your new pin: ')
                account.reset_pin(old_pin, new_pin)

            case "5":
                print("Thanks")
            
            case _ :
                print('Invalid operation')


except Exception as e:
            print("Error ", e)