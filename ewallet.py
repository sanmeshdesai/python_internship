def checkAmount(amt):

    while True:
        amount = input(amt).strip()
        if amount.lower() == 'q':
            print('Transaction cancelled.')
            return None
        
        try:
            amount = int(amount)
            if amount <= 0:
                print('Invalid amount. Please enter positive value')
                continue
            
            return amount

        except ValueError:
            print('Invalid input. Please enter correct amount')



def addMoney(balance):

        amount = checkAmount("Enter amount or 'q' to cancel transaction ")
             
        if amount is None:
            return balance

        balance += amount
        print(f'Transaction successful {amount} added to your balance')
        print('Your updated balance is', balance)

        return balance
        
       


def spendMoney(balance):

    while True:
        amount = checkAmount("Enter amount or 'q' to cancel transaction ")
    
        if amount is None:
            return balance

        if amount > balance:
            print(f'Insufficient balance. Please enter smaller amount \nYour balance is {balance}')
            continue

        balance -= amount
        print(f'Transaction successful {amount} spent')
        print('Your updated balance is', balance)
        return balance
    
    



def main():

    balance = 50000

    while True:
        print('E-Wallet Menu \n 1. Add Money \n 2. Spend Money \n 3. Check balance \n 4. Exit')
        choice = input('Enter choice ').strip().lower()
    
        match choice:

            case '1' | 'add':
                    # prev_balance = balance
                    balance = addMoney(balance)
                    # if prev_balance != balance:
                        # print('Your updated balance is', balance)
                    print('----------------------------------')
                
            case '2' | 'spend':
                    # prev_balance = balance
                    # balance = spendMoney(balance)
                    # if prev_balance != balance:
                        # print('Your updated balance is', balance)
                    print('----------------------------------')
                
            case '3' | 'check':
                    print('Your current balance is', balance)
                    print('----------------------------------')

            case '4' | 'exit':
                    print('Thank you')
                    print('----------------------------------')
                    break

            case _:
                    print('Invalid choice, Please select right operation')


main()



