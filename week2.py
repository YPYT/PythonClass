# p10

## Initialize the constants
TAX_RATE = 0.2
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(incomeTax))


# p15
print("\" This is an example \n \t of escape \b sequences\'")

# p24
## ord
print(ord('a')) #97
print(ord('A')) #65
## chr
print(chr(97)) #a
print(chr(66)) #B
## mix
print(chr(ord('A')+3)) #D


# p29
## Arithmetic Expressions
radius = input("Enter the radious: ")
print(float(radius))
print(float(radius) ** 2 * 3.14)

# p30
print(int(6.75)) #6
print(round(6.75)) #7

print(3+4*2**5) #131
print(3//2*5.0) #1*5.0=5.0
print(3/2*5) #1.5*5 = 7.5

#p32
x = 8
y = 2
print(x+y*3) #14
print((x+y)*3) #30
print(x**y) #64
print(x%y) #0
print(x/12.0) #0.6666666666666666
print(x//6) #1

#p34
print(4-5+3) #2
print(abs(4-5)+3) #4
print(round(7.563)) #8


#p36 module
from math import pi, sqrt
print(sqrt(4)) #2.0
print(pi) #3.141592653589793
print(round(7.563, 1)) #7.6


###Part 2: Exercises
"""
a) You can calculate the surface area of a cube if you know the length of an edge. Write a
program that takes the length of an edge (an integer) as input and prints the cube’s
surface area as output.
"""
# input length of the edge
length = int(input("Enter the length of the cube's edge: "))
# calculate the surface of the cube
surfaceArea = 6 * (length ** 2)
# display the surface are of the cube to the user
print("The surface area of the cube is ", surfaceArea)

""""
b) Five Star Video rents new videos for $3.00 a night and oldies for $2.00 a night. Write a
program that the clerks at Five Star Video can use to calculate the total charge for a
customer’s video rentals. The program should prompt the user for the number of each
type of video and output the total cost.
"""
# The cost
newVideoRate = 3.00
oldieVideoRate = 2.00

# input how many new video and old video the customers rent
numNewVideos = int(input("How many new video did you rent? "))
numOldies = int(input("How many old video did you rent? ")) 

# Calculate the total cost
totalCost = (newVideoRate * numNewVideos) + (oldieVideoRate * numOldies)

# Display the total cost to the customer
print("The total cost is $ ", totalCost )

""""
c) An employee’s total weekly pay equals the hourly wage multiplied by the total number
of regular hours plus any overtime pay. Overtime pay equals the total overtime hours
multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly
wage, total regular hours, and total overtime hours and displays an employee’s total
weekly pay.
"""
# Prompt the user for hourly wage, total regular work hours, and total overtime hours
hourlyWage = float(input("Enter the hourly wage: $"))
totalRegularHours = float(input("Enter the total regular hours worked: "))
totalOvertimeHours = float(input("Enter the total overtime hours worked: "))

# Caluculate the regular pay
regularPay = hourlyWage * totalRegularHours

# Caluculate the overtime pay
overtimePay = hourlyWage * 1.5 * totalOvertimeHours

# Caluculate the total weekly pay
totalWeeklyPay = regularPay + overtimePay

# Display the total weekly pay to the user
print("The weekly pay is $ ", totalWeeklyPay)