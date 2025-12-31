# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     def __init__(self, num, hours):
#         self.num = num
#         self.hours = hours

#     @abstractmethod
#     def calculate_fee():
#         pass


# class Car(Vehicle):
#     def calculate_fee(self):
#         return self.hours * 50


# class Bike(Vehicle):

#     def calculate_fee(self):
#         return self.hours * 20


# class Truck(Vehicle):

#     def calculate_fee(self):
#         return self.hours * 100


# n = int(input("Enter no. of vehicles : "))
# for i in  range(n):
#     v,r,h = input("Enter input <VehType> <reg no.> <hours> : ")
#     if v == "Car":
#         x = Car(int(r),int(h))

l = [1,2,3,4]
ls = lambda ls : [x**2 for x in ls]
print(ls(l))