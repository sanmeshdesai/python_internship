# # def Sum(a,b):
# #     print(a+b)

# # Sum(20,50)
# # Sum(20)

# # Default Parameter- such a  default values which we pass during function declartion 
# # used when user doesnt passed sufficient arguments

# def Sum(a=0,b=0):
#     print(a+b)

# Sum(100,200)
# Sum(10)
# Sum()
 
# #  *****************

# def Mult(a=1,b=1):
#     print(a*b)

# Mult(5,4)
# Mult()
# Mult(4)


# # ******************************

# def Emp(empName="JOHN",empSkill="React",empId=None):
#     return empName, " And ", empSkill, " And ", empId

# # print(Emp())
# # print("","Python")
# # print(Emp("","JS"))

# print(Emp(empSkill="Devops",empName="Pratik",empId=123))

# # ***************************************************

# # Arguments
# # used to handle extra arguments which we passed during function calling
# # *args

# def Addition(x=0,y=0,z=0,*args):
#     # print(args)
#     sum=x+y+z
#     for i in args:
#      print(i)
#      sum+=i

#     print("Total Sum Is : ", sum)

# # Addition(100,200,400)
# # Addition(200,300)

# # arguments-actual values
# Addition(10,30,20,1000,200,5000)



# # def add(a = 0, b = 0, c = 0, *args):
# #     sum = 0
# #     sum = a + b + c
# #     for i in args:
# #         sum += i
# #     return sum


# # print(add(10,20,30,100,200,300))


# # def fact(n):
# #     if n ==0 or n == 1:
# #         return 1
# #     else:# def Sum(a,b):
# #     print(a+b)

# # Sum(20,50)
# # Sum(20)

# # Default Parameter- such a  default values which we pass during function declartion 
# # used when user doesnt passed sufficient arguments

# def Sum(a=0,b=0):
#     print(a+b)

# Sum(100,200)
# Sum(10)
# Sum()
 
# #  *****************

# def Mult(a=1,b=1):
#     print(a*b)

# Mult(5,4)
# Mult()
# Mult(4)


# # ******************************

# def Emp(empName="JOHN",empSkill="React",empId=None):
#     return empName, " And ", empSkill, " And ", empId

# # print(Emp())
# # print("","Python")
# # print(Emp("","JS"))

# print(Emp(empSkill="Devops",empName="Pratik",empId=123))

# # ***************************************************

# # Arguments
# # used to handle extra arguments which we passed during function calling
# # *args

# def Addition(x=0,y=0,z=0,*args):
#     # print(args)
#     sum=x+y+z
#     for i in args:
#      print(i)
#      sum+=i

#     print("Total Sum Is : ", sum)

# # Addition(100,200,400)
# # Addition(200,300)

# # arguments-actual values
# Addition(10,30,20,1000,200,5000)



# # def add(a = 0, b = 0, c = 0, *args):
# #     sum = 0
# #     sum = a + b + c
# #     for i in args:
# #         sum += i
# #     return sum


# # print(add(10,20,30,100,200,300))


# # def fact(n):
# #     if n ==0 or n == 1:
# #         return 1
# #     else:
# #         return n * fact(n-1)
    
# # print(fact(5))


# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mul(a,b):
#     return a * b

# def div(a,b):
#     return a / b

# def mod(a,b):
#     return a % b



# #         return n * fact(n-1)
    
# # print(fact(5))


# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mul(a,b):
#     return a * b

# def div(a,b):
#     return a / b

# def mod(a,b):
#     return a % b



for i in range (10, 0, -1):
    print(i)