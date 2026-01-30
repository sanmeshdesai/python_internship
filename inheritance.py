
# # Single inheritance
# class Employee:
    
#     def __init__(self, empId, name, empRole, empDept, empCTC) :
#         self.empId = empId
#         self.name = name
#         self.empRole = empRole
#         self.empDept = empDept
#         self.empCTC = empCTC
        
#     def empDetails(self):
#         print(f'Emp ID : {self.empId} Emp Name : {self.name} Emp Role: {self.empRole} Emp Department: {self.empDept} Emp CTC : {self.empCTC}')


# class Manager(Employee):

#     def __init__(self, name, dept_name, empRole,):
#         super().__init__(self, name, empRole)
#         self.name = name
#         self.dept_name = dept_name
#         self.e


#     def managerDetails(self):
#         print(f'Emp ID : {self.name} Emp Name : {self.dept_name}')

#     def empDetails(self):
#         return super().empDetails()



# m1 = Manager(1,'f','g')

# print(m1.empRole)


class Vechicle:

    def __init__(self, vechicle_type, fuel_type, vechicle_mode):
        self.vechicle_mode = vechicle_mode
        self.fuel_type = fuel_type
        self.vechicle_type = vechicle_type
    
    def details(self):
        print(f'Details: {self.vechicle_type}')

class Car(Vechicle):

    def __init__(self, name, brand, color, model, price, vechicle_type, fuel_type, vechicle_mode):
        super().__init__(vechicle_type, fuel_type, vechicle_mode)
        self.name = name
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price

    def details(self):
        super().details()
        print(f'name {self.name}')


# c1 = Car('BMW','BNY','black','S+','50L')
# c2 = Car('Curve','Tata','white','top end','13L')
# c1.carDetails()
# c2.carDetails()
c1 = Car('Hyrider','Toyota','White','a','10','d','petrol','d')
c1.details()