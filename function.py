# function- is a block of code i.e is a bunch of statements / mini program inside your program
# we can reused functions multiple times by calling
# defined once and reused multiple times
# syntax:

'''

syntax

# function defination/declartion
def function_name():
    #block of code will execute

# function_call
function_name()

eg

def demo():
    print("hello world)

demo()

'''


# def add(a, b):
#     return a + b

# print(add(10,20))


# def isElligible(age):
#     if age >= 18:
#         return 'Congrats'
#     else:
#         return 'sorry'
    
# age = int(input())
# print(isElligible(age))

# def mul(a,b):
#     return a * b

# print(mul(10*20))

# def demo(name, skill):
#     print(name + " " + skill)
#     return name + skill
#     print('hello world')

# demo('sanmesh','react')


# def evenOdd(n):
#     if n % 2 == 0 :
#         return 'even'
#     else:
#         return 'odd'

# print(evenOdd(25))




# to pass dynamic values inside function

# parameters - value which we passed during function declartion/defination
# arguments-Actual values which we pass while function calling 


# Account_Balance=100000

def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    
    if amount <= 0:
        print("Invalid deposit amount")
        return balance

    balance += amount
    print("Account Balance:", balance)
    return balance


def withdraw(balance):
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid withdrawal amount")
        return balance

    if amount > balance:
        print("Insufficient balance")
        return balance

    balance -= amount
    print("Account Balance:", balance)
    return balance


def main():
    account_balance = 100000

    action = input("Would you like to deposit or withdraw? (deposit/withdraw/no): ").lower()

    match action:
        case "deposit":
            account_balance = deposit(account_balance)
        case "withdraw":
            account_balance = withdraw(account_balance)
        case "no":
            print("Account Balance:", account_balance)
        case _:
            print("Invalid choice")


main()
