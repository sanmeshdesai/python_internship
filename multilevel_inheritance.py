#  a => b => c

class Bank:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def details(self):
        print(f'Details: {self.name}, {self.branch}')

class Account(Bank):

    def __init__(self, name, branch, acc_no, acc_type, acc_bal):
        super().__init__(name, branch)
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.acc_bal = acc_bal

    def details(self):
        super().details()
        print(f'Details: {self.acc_no}, {self.acc_type}, {self.acc_bal}')

class Customer(Account):

    def __init__(self,customer_name, customer_age, name, branch, acc_no, acc_type, acc_bal):
        super().__init__(name, branch, acc_no, acc_type, acc_bal)
        self.customer_name = customer_name
        self.customer_age = customer_age

    def details(self):
        super().details()
        print(f'{self.customer_name}, {self.customer_age}')


c = Customer('Aditya','23','Hsbc','NYC','123456789','saving','1000')
c.details()