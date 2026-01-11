# conditional statement
# check conditions and return output
# ternary
# if, elif, else, match case
# looping 
# for in, while




# number = int(input('enter a number: '))
# if (number % 2  == 0):
#     print('even')

# age = int(input('enter your age: '))
# if age >= 18:
#     print('you are elligible for voting')
# if age < 18:
#     print('you are not elligible for voting')



# shopping_amount = int(input("Enter shopping amount "))
# discount = 0
# if shopping_amount >= 20000:
#     discount = 20
#     discount_amount = shopping_amount * ( discount / 100)
#     total = shopping_amount - discount_amount
#     print(f'Shopping amount is {shopping_amount}  your discount is {discount_amount} net total is {total}')


# if(True):
#     print('hello')


# age = int(input('Enter age'))

# if age >= 18:
#     print('Congrats')
# else:
#     print('sorry')

# score1 = int(input('Enter score 1'))
# score2 = int(input('Enter score 2'))
# score3 = int(input('Enter score 3'))
# score4 = int(input('Enter score 4'))
# score5 = int(input('Enter score 5'))
# score6 = int(input('Enter score 6'))

# if score1>=35 and score2>=35 and score3>=35 and score4>=35 and score5>=35 and score6>=35:
#     perc = ((score1+score2+score3+score4+score5+score6)/600 )* 100

#     if perc >= 75:
#         print('You got distinction', perc)
#     else:
#         print('pass')
# else:
#     print('fail')


# elif

# a = int(input('enter no 1'))
# b = int(input('enter no 2'))
# c = int(input('enter no 3'))



# user shopping amount -> if amt >= 10000 && < 20000 disc = 20%
# amt >=2000 && amt < 30000 % 30 if 40000 dic 40  


shop_amt = int(input('Enter shopping amount'))
dis = 0

if shop_amt >= 10000 and shop_amt < 20000:
    dis = 20
   
elif shop_amt >= 20000 and shop_amt < 30000:
    dis = 30
   
elif shop_amt >= 30000 and shop_amt < 40000:
    dis = 40
    
elif shop_amt >= 40000:
    dis = 50
else:
    dis = 0

discount_amt = shop_amt * dis / 100
total = shop_amt - discount_amt
print(f'shopping amount is {shop_amt} discount is {discount_amt} total is {total}')