# Week3 Contents
# loop
# Data Sequence
# Formatting


# # ---- loop ----
# for counts in range(1,5):
#     print("The count is", counts)
# # >>> 
# # The count is 1
# # The count is 2
# # The count is 3
# # The count is 4

# for number in [1,2,3]:
#     print(number, end=" ")
# # >>>
# # 1 2 3

# for character in "Hi there!":
#     print(character, end=" ")
# # >>>
# # H i   t h e r e !


# # ---- Data Sequence ----
# print(list(range(1,6,1))) #[1, 2, 3, 4, 5]
# print(list(range(1,6,2))) #[1, 3, 5]
# print(list(range(1,6,3))) #[1, 4]
# print(list(range(10,6,-1))) #[10, 9, 8, 7]


# # ---- Formatting ----
# # % -Format Operator
# # s - displayed data for string 
# # d - displayed data for integer 
# # f -  floating-point number

# print("%7s" % "hello") # "  hello" (right justify)
# print("%-7s" % "hello") #"hello  " (left justify)

# for count in range(7,13):
#     print("%-3d%12d" % (count, 10 ** count))
# # >>> 
# # 7      10000000
# # 8     100000000
# # 9    1000000000
# # 10  10000000000
# # 11 100000000000
# # 12 1000000000000

# salary = 123.355
# print("Your salary is $" + str(salary)) # Your salary is $123.355
# print("Your salary is $%0.2f" % salary) # Your salary is $123.36
# print("Your salary is $%10.2f" % salary) # Your salary is $    123.36
# print("Your salary is $%10f" % salary) # Your salary is $123.355000



# Part 1
# # Input
# startingBalance = float(input("Enter the investment amount: "))
# numOfYears = int(input("Enter the number of years: "))
# rate = int(input("Enter the rate as a %: "))
# totalInterest = 0
# # Title
# title = ["Year", "Starting balance", "Interest", "Ending balance"]
# for name in title:
#     print(name, end=" ")
# print("\n")
# for count in range(1,numOfYears+1):
#     interest = startingBalance * rate / 100
#     totalInterest += interest
#     endingBalance = startingBalance + interest
#     print("%4d" % count, "%16.2f"%startingBalance, "%8.2f"%interest,"%14.2f"%endingBalance )
#     startingBalance = endingBalance
# print("Ending balance: $%10.2f" % endingBalance)
# print("Total interest earned: $%10.2f" % totalInterest)

# Part 2
# # Input
# salary = int(input("Enter your starting salary: $"))
# rate = int(input("Enter the percentage increase as a %: "))
# years = int(input("Enter the number of years: "))

# title = ["Year", "Salary"]
# for name in title:
#     print(name, end=" ")
# print("\n")
# for year in range(1,years+1):
#     print("%4d"%year, "%6d"%salary)
#     salary += salary * rate / 100
