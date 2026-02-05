# abstraction - hiding data complexity
# used for enhanced security
# ABC module create abstact base class
# @abstactmethod is a decorator.

from abc import ABC, abstractmethod

class Car(ABC):

    def details(self, _brand, color, price):
        self._brand = _brand
        self.color = color
        self.price = price

        print(f"brand: {self._brand}, color: {self.color}, price: {self.price}  ")

    @abstractmethod
    def start(self):
        print('car start')

class Tesla(Car):
    def car_details(self, _brand, color, price): 
        self.details(_brand, color, price)

    def start(self):
        print("tesla car stated")


t1 = Tesla()
t1.car_details('Tesla','White','$92,223')
t1.start()
