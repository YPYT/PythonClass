# Part 1
# - calculation
# - String
# - Data Type
# - Function
# - Module


# ## tax
# # Constants
# taxRate = 0.2
# standartDeduction = 10000
# dependentDeduction = 3000
# # Input
# grossIncome = int(input("Enter the gross income: "))
# numDependents = int(input("Enter the number of dependents: "))
# # Calculate income tax
# taxableIncome = grossIncome - standartDeduction - dependentDeduction * numDependents
# incomeTax = taxableIncome * taxRate
# # Display the outcome
# print("The income tax is $", str(incomeTax))

# ## String Literal
# print("\" This is an example \n \t of escape \b sequences\'")
# # >>> OUTPUT
# # " This is an example 
# #          of escape sequences'

# ## Variable and Assignment Statements
# # - ord functions convert characters to their numeric ASCII codes
# print(ord('a')) # 97
# print(ord('A')) # 65
# print(ord('B')) # 66
# # - chr functions convert numeric to characters
# print(chr(97)) # a
# print(chr(66)) # B
# print(chr(67)) # C

# ## Arithmetic Expressions
# print(int(6.77)) # 6
# print(round(6.77)) # 7
# print(round(6.22)) # 6
# print(round(6.7723, 1)) # 6.8
# print(round(6.2223, 1)) # 6.2

# ## Module
# import math
# print(help(math))




# # Part 2
# # a)
# length = int(input("Enter the length: "))
# cubeSurface = length ** 2 * 6
# print("The cube's surface is", cubeSurface)

# # b)
# # Constants
# newRate = 3.00
# oldishRate = 2.00
# # Inputs
# numOfNew = int(input("Enter the number of the new videos: "))
# numOfOldish = int(input("Enter the number of the old videos: "))
# # Process
# totalCost = (newRate * numOfNew) + (oldishRate * numOfOldish)
# # Output
# print("The total cost is $", str(totalCost))

# # c)
# # Inputs
# hourlyWage = float(input("Enter the hourly wage: "))
# overTimeHours = float(input("Enter the total overtime hours: "))
# regularHours = float(input("Enter the total regular hours: "))
# # Process
# regularPay = hourlyWage * regularHours
# overtimePay = hourlyWage * 1.5 * overTimeHours
# totalWeeklyPay = round(regularPay + overtimePay, 1)
# # Output
# print("The total weekly pay is $", str(totalWeeklyPay))