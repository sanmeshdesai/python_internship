# # bundlng data and methods within a single unit
# # data hiding
# # encapsulation in python is achieved through classes


# # access specifiers
# # public - free access
# # private - only within class
# # protected - class and subclasses

# # class A :
# #     acc_no = "1234567890"   
# #     print(acc_no)

# #     def acc_holder(self, name, id):
# #         print('res')
# #         self.name = name
# #         self.id = id
# #         return f'Account Holder: {self.name}, ID: {self.id}'
# #         # return self.name, self.id

# # user1 = A()
# # res = user1.acc_holder("John Doe", 123)
# # print(res)


# class A:
#     name = 'Pratik'
#     __emp_ctc = '20lpa'
#     _role = 'SDE-1'  # protected member

#     def details(self):
#         emp_id = 101
#         print(self.name)
#         print(emp_id)
#         print(self.__emp_ctc)
#         print(self._role)

# class B(A):
#     sklls = 'Python'
#     print(sklls)

# b1 = B()
# b1.details()  # accessing parent class method

# # can asccess private member outside class using name mangling
# print(b1._A__emp_ctc)  # accessing private member using name mangling


# print(b1._role)  # accessing protected member


class Account:
    
        def __init__(self):
            self.__balance = 0

        def deposit(self, amount):  
             
                self._balance += amount


        def withdraw(self, amount):
            
                if amount <= self.__balance:
                    self.__balance -= amount
                else:
                    raise ValueError("Insufficient funds")
            

        def check_balance(self):
         return self.__balance
        


try :
    acc = Account()
    acc.deposit(500)
    print(acc.check_balance())
    acc.withdraw(200)
    print(acc.check_balance())

except Exception as e:
    print("Error: ",e)