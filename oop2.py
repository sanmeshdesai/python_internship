# constructor
# special method 

class Parent:
    name= 'parent'
    def __init__(self):
        print('constructor called')


    def parentDetails(self):
        print('parent class method')

class Child:
    name= 'child'

    def __init__(self):
        print('child constructor called')


c1 = Child()
print(c1.name)
