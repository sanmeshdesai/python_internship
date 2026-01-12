# match case: multiple cases at a same time.

# match choice:
#     case 1:
#     case 2:

#     case _:
    

# day = int(input('Enter a day '))

# match day: 
#     case 1: 
#         print('Monday')
#     case 2: 
#         print('Tuesday')
#     case 3: 
#         print('Wednesday')
#     case 4: 
#         print('Thursday')
#     case 5: 
#         print('Friday')
#     case _:
#         print('Invalid day no') 
        

# n1 = int(input('Enter first number '))
# n2 = int(input('Enter second number '))
# operation = input('Choose from + - * / % ')

# match operation:
#     case '+':
#         print(f'adiition is {n1} + {n2} is {n1 + n2}')
#     case '-':
#         print(f'subtraction is {n1} - {n2} is {n1 - n2}')
#     case '*':
#         print(f'subtraction is {n1} * {n2} is {n1 * n2}')
#     case '/':
#         print(n1 / n2)
#     case '%':
#         print(n1 % n2)
#     case _:
#         print('Invalid operation')
        

# weekwday or weekend

# day = input('Enter day ')

# match day:
#     case 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday' :
#         print('weekday')
#     case 'saturday' | 'sunday':
#         print('weekend')
#     case _: 
#         print('invalid day')




# looping
# while 
# 
# variable initialise
# while condition:
#       block of code
#       incr or decr

# a = 1
# while a <= 10:
#     print('hello welcome to modern python')
#     a += 1

# b = 1
# while b <= 100:
#     if b % 2 == 0:
#         print(b)
#     b += 1

# b = 1
# sum = 0
# while b <= 50:
#     if b % 2 == 0:
#         sum += b
#     b += 1
# print(sum)


# range(stop) 
# range(start, stop) 
# range(start, stop, steps)

# sum = 0
# for x in range(2,50,2):
#     sum += x2
# print(sum)


# for i in range(1, 11):
#     print(5 * i)


# n = int(input('enter a number'))
# for i in range(1, 11):
#     print(n * i)


# for i in range(3):
#     print(i)
# else:
#     print('loop finished')

for i in range(1,6):
    print('*' * i)

for i in range(1,6):
    print('*' * i)

def demo():
    print('a')

demo()