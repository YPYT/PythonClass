# Class (class is like a blueprint / category) => Object
# - sttributes (things)
# - method(action) -> init method(constractor: initialising all attribute) :default => __init__(self, )
## ex) vehicle(super class) -> water_vehicle, ground_vehicle, fly_vehicle (inheritane)
## 1: create class
## 2: create attribule
## 3: create method
# Object_Name = class_Name() :How to make object

# ex) 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 22)
print("p1 name:",p1.name)
print("p1 age:", p1.age)




### ------ Small Quiz -------
# large = 12
# medium = 10
# small = 8
# sum = 0

# while True:
#     lunch = input("Enter the serving size, L for large, M for medium, S for small, or Enter to exit:" )
#     lunch_lower = lunch.lower()
#     if lunch_lower == "l":
#         sum += large
#     elif lunch_lower == "m":
#         sum += medium
#     elif lunch_lower == "s":
#         sum += small
#     else: 
#         break
# print("The total cost is $" + str(sum))
# if sum > 50:
#     print("You will have free drink!!")

