
def addMoney(balance, amount):
    if amount <= 0:
        print('Invalid amount')

    else:
        balance += amount
        print('Money added successfully')

    return balance

def spendMoney(balance, amount):
        
    if amount > balance :
        print('Insufficient balance, Your balance is', balance)

    elif amount < 0:
        print('Invalid amount')
    
    else:
        balance -= amount
        print('Money spend successfully')
        
    return balance



def main():

    balance = 50000

    # while True:
    print('E-Wallet Menu \n 1. Add Money \n 2. Spend Money \n 3. Check balance \n 4. Exit')
    choice = input('Enter choice')

    match choice:

        case '1' | 'add':
            try:
                amount = int(input('Enter amount to add '))
                balance = addMoney(balance, amount)
                print('Your updated balance is', balance)
            except ValueError:
                print('Enter correct amount')

        case '2' | 'spend':
            try:
                amount = int(input('Enter amount to add '))
                balance = spendMoney(balance, amount)
                print('Your updated balance is', balance)
            except ValueError:
                print('Enter correct amount')

        case '3' | 'check':
            print('Your current balance is', balance)

        case '4' | 'exit':
            print('Thank you')
            exit()

        case _:
            print('Invalid choice, Please select right operation')


main()



