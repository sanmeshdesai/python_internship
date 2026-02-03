# one method different forms
# based on the object, arguments, classes etc.

# run time polymorphism
# method overriding
# polymorphism with inheritance

class Parent:
    def Hello(self):
        print("Hello from Parent class")

class Child(Parent):    
    def Hello(self):
        super().Hello()
        print("Hello from Child class")


c1 = Child()
c1.Hello()  # Hello from Child class


class PaymentGateway:

    def __init__(self, balance, orderId, customerId, status):
        self.balance = balance
        self.orderId = orderId
        self.customerId = customerId
        self.status = status

    def details(self):
        print(f'Balance: {self.balance}, Order ID: {self.orderId}, Customer ID: {self.customerId}, Status: {self.status}')




class UPI(PaymentGateway):

    
    def pay(self):
        print("Paying through UPI")

    def details(self):
        print("UPI Payment Details:")
        super().details()

class COD(PaymentGateway):


    
    def pay(self):
        print("Paying through Cash on Delivery")

    def details(self):
        print("COD Payment Details:")
        super().details()

u = UPI(100, 'ORD123', 'CUST456', 'Completed')
u.pay()
u.details()



