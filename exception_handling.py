# def calc(a, b):
#     return a/b

# print(calc(5,5))

# print(calc(10,0)) # division by zero


# def user():
#     print('hello', name) # Name error


# exception: error that stop promgram
# prevent program crashes



# try:
#     a = 20
#     b = 'pratik'
#     print(a + b)
    
# except:
#     print("Error occured Invalid data type")

# print('hello pratik')



# def Calci(a,b):
#     return a/b

# print(Calci(5,5))


# res=Calci(50,0)
# print(res)

# def calci(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         print ("Error occured ", e)

# print(calci(5, 0))
# try:
#     a = 100
#     b = '300'
#     # b = 200

#     print(a + b)

# except TypeError as e:
#     print('Error occured. ', e)
    
# except NameError as e:
#     print('Error occured. ', e)


# finally
# finally block runs even exception occur
# try:
#     x = 100
#     y = '50'

#     print( x + y)

# except Exception as e:
#     print('error occured:', e)

# finally: 
#     print('code execute successfully')


# else if error not occured runs block


# try:
#     num = int(input('enter number :'))

# except ValueError:
#     print('Invalid error')

# else:
#     print('You entered ',num)

# finally:
#     print('Task completed')


# raise: custom error

# try:
#     age = int(input('Enter your age '))
    
#     def demo(a):
#         if a <= 0:
#             raise ValueError('Age cannot be negative')
#         print('your age is', a)
        

#     demo(age)

# except Exception as e:
#     print('Error', e)




# try:
#     a = 20
#     b = 'pratik'
#     print(a + b)
    
# except:
#     print("Error occured Invalid data type")

# print('hello pratik')






# try:
#     def calci(a, b):
#         return a / b

#     print(calci(5,5))
#     res = calci(50,0)
#     print(res)

# except Exception as e:
#     print('Error occured',e)

# print('hello')


try:
    userName = input('Enter username ')

    if userName == '':
        raise ValueError('Username cannot be empty')

    if len(userName) < 4:
        raise ValueError('username must be at least 4')
    
    if ' ' in userName:
        raise ValueError('username cannot contain spaces')
    
    print(userName)

except ValueError as e:
    print('Error', e)


