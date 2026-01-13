# def square(n):
#     return n * n

# print(square(5))

# import math
# def squar(n):
#     return pow(n,2)

# print(squar(8))

# def sqr(n):
#     return n ** 2

# print(sqr(6))

# def maxNo(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= c:
#         return b
#     else:
#         return c
    
# print('max number is',maxNo(100, 20, 500))

# factorial using loop

# def fact(n):
#     facts = 1
#     for i in range(1,n+1):
#         facts *= i 
#     return facts

# print(fact(5)) 

# even odd

# def checkEvenOdd(n):
#     if n % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
    
# print('Number is', checkEvenOdd(20))

# def table(n):
#     for i in range(1, 11):
#         print(f'{n} x {i} = {n * i}')
    
# n = int(input('Enter number '))
# table(n)

# count vowels

# def countVowels(str):
#     vowels = 'aeiou'
#     count = 0
#     for char in str:
#         if char in vowels:
#             count += 1
#     return count

# str = input('Enter string ')
# print('Number of vowels in string',countVowels(str))

# def greeting(name = 'Guest'):
#     print('Good morning',name)

# greeting()

# def sum_and_average(n1, n2, n3, n4):
   
#     sum = n1 + n2 + n3 + n4
#     avg = sum / 4
#     return sum, avg

# print(sum_and_average(10,20,30,40))


# def totalMarks(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print('Total marks',totalMarks(80,70,50,30,86))


# countdown

# def countdown(n):
#     if n <= 0 :
#         return 'Stop'
#     else :
#         print(n)
#         return countdown(n-1)
    
# print(countdown(10))