#Part 1
# - calculate
# - inout 
# - Syntax error

## 2
print("A", end=" ")
print("B", end=" ")
print("C", end=" ")
print()
print("X")
print("Y")
print("Z")
#>> OUTPUT
# A B C 
# X
# Y
# Z

## 3 input
number = int(input("Enter number: "))
print(5+number)

## 4 
floatNum = float(input("Enter float number: "))
print(5.99+floatNum)




#Part 2

# a)
print(8) # 8
print(8*2) # 16
print(8**2) # 64
print(8/12) # 0.6666666666666666
print(8//12) # 0
print(8%6) # 2
print(8/0) # ZeroDivisionError: division by zero

# b)
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
area = width * height
print("The area is", area, "square units")
# >> OUTPUT
# Enter the width: 3
# Enter the height: 4
# The area is 12 square units

# c)
radius = int(input("Enter the radious: "))
area = 3.14 * radius ** 2
print("The area is", area, "cm2")

# d)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("I am", name, "and I'm", age, "years old.")



