# is a professional way of writing our code to solve real world problems.
# avoid repetation
# security and properties
# easy maintaince
# organized code

# Inheritance
# Encapsulation
# Abstraction
# Polymorphism

# class and object
  
# class - is blueprint of object
# contain propertes and methods.

# object - real time entity, Instance of class.

# creating class
# class Mobile:
#     pass

# creating object
# m1 = Mobile()


# class Mobile:
#     name = 'iphone 18'
#     brand = 'apple'
#     color = 'midnight black'

#     def calling(self):
#         print('hello')

#     def chatting(self):
#         print('I am chatting with someone')

#     def cammera(self):
#         print('Clocking photos')

# m1 = Mobile()
# print(m1.name)
# print(m1.brand)
# print(m1.color)
# print(m1)

# m1.calling()

class Product:
    id = 101
    name = 'samsung'
    description = 'mobile phone'
    category = 'mobile'

    def addItem(self):
        print('Item added')
    
    def updateItem(self):
        print('Item updated')

p1 = Product()
print(p1.name)
print(p1.category)

p1.addItem()
p1.updateItem()





class Customer:
    id = 101
    name = 'john'
    email = 'john@gmail.com'

    def register(self):
        print('register successfull')
    
    def login(self):
        print('login successfull')

    
c1 = Customer()
print(c1.name)
print(c1.email)

c1.register()
c1.login()



class Order:
    userId = 101
    items = ['a','b']
    amount = 10000

    def placeOrder(self):
        print('Order placed')

    def cancelOrder(self):
        print('Order canceled')

o1 = Order()
print(o1.items)
print(o1.amount)

o1.placeOrder()
o1.cancelOrder()



class shoppingCart:
    userId = 101
    itemId = 1
    quantity = 2

    def addToCart(self):
        print('added succefully')
    
    def removeFromCart(self):
        print('remove item succefully')

s1 = shoppingCart()
print(s1.itemId)
print(s1.quantity)

s1.addToCart()
s1.removeFromCart()

class Payment:
    userId = 101
    type = 'COD'
    amount = 10000

    def addPaymentMethod(self):
        print('payment method added')