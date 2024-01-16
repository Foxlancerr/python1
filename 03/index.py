# abstraction in python
from abc import ABC,abstractmethod

class Car(ABC):
    
    @abstractmethod
    def speed(self):
        pass
    

class Vehicle(Car):
    # pass
    def speed(self):
        print("Vehicle is Started")
    
class Honda(Car):
    def speed(self):
        print("Honda is Started")

    
c1 = Vehicle()
c2 = Honda()
c1.speed()
c2.speed()


# getter and setter methods
# encapsulation

# class Animal:
#      __symbol = "A" # private and can not be accessed in child classes
#      _id = 12 # protected and can be accessed in child classes
#      def getSymbol(self):
#          return self.__symbol
#      def setSymbol(self,val):
#          self.__symbol = val

# class Dog(Animal):
#     def barking(self):
#         print ("barking dogs")

# class DogChild(Dog):
#     pass

# d1 = DogChild()
# d1.barking()

# # print(d1._id) # protected
# # print(d1.__symbol) # not accessed

# # we can used the getter and setter to access its properties
# print(d1.getSymbol()) # get the private member in its child class
# d1.setSymbol("Z") # set the private member in its child class
# print(d1.getSymbol()) 


# encapsulation

# class Animal:
#      __symbol = "A" # private and can not be accessed in child classes
#      _id = 12 # protected and can be accessed in child classes
#      def _sound(self):
#          print ("barking animals") 

# class Dog(Animal):
#     def barking(self):
#         print ("barking dogs")

# class DogChild(Dog):
#     pass

# d1 = DogChild()
# d1.barking()
# d1._sound()
# print(d1._id) # protected
# print(d1.__symbol) # not accessed










# Multiple level Inheratance in python

# class Animal:
#      def sound(self):
#          print ("barking animals") 

# class Dog(Animal):
#     def barking(self):
#         print ("barking dogs")

# class DogChild(Dog):
#     pass

# d1 = DogChild()
# d1.barking()
# d1.sound()






# Single level Inheratance in python

# class Animal:
#      legs = "3 legs"
#      def barking(self):
#          print ("barking animals") 

# class Dog(Animal):
#     pass

# d1 = Dog()
# d1.barking()
# print(d1.legs)






# OOPS in python

# class EmptyClass:
#     pass

# class Car:
    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color
    
    # def displayInfo(self):
    #     print("The name of the car is " + self.name + " and color is " +self.color)  


# Object Define here
# c1 = Car("farari", "red")
# c2 = Car("BMW", "blue")

# c1.displayInfo()
# print(c2)
# print(id(c1.color))
# print(id(c2.color))