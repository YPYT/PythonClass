###### For loop #####

# fruits = ["apple", "banana", "peach"]
# for f in fruits:
#     print(f)
#     if f == "banana":
#         break
#output: 
# > apple
# > banana


# for x in range (6):
#     print(x)
# > 0
# > 1
# > 2
# > 3
# > 4
# > 5


# for x in range (5):
#     print("*")
# > *
# > *
# > *
# > *
# > *


# for x in range (5):
#     print("*", end=" ") 
# > * * * * *


# num = 2
# exponent = 3
# product = 1
# for x in range (exponent):
#     product = product * num
#     print(product, end=" ")
# > 2 4 8


# num = 1
# for count in range(4):
#     num = num * (count + 1)
#     print(num)
# > 1
# > 2
# > 6
# > 24


# lower = int(input("Enter the lower bound: "))
# upper = int(input("Enter the upper bound: "))
# sum = 0
# for count in range(lower, upper+1):
#     sum += count
#     print("count is", count)
#     print("sum is ", sum)
# print(sum)
# > Enter the lower bound: 1
# > Enter the upper bound: 10
# > 55


# print(list(range(4))) # > [0, 1, 2, 3]
# print(list(range(1,5))) # > [1, 2, 3, 4]


# for num in [1,2,3]:
#     print(num, end=" ") # > 1 2 3


# for char in "Hi, there!":
#     print(char, end=" ")
# > H i ,   t h e r e !

#------Data Sequence------
## --- Specifying the Steps in the Range----
# print(list(range(1,6,1))) #same as using two arguments
# > [1, 2, 3, 4, 5]

# print(list(range(1,6,2))) # Use every other number
# > [1, 3, 5]
 
# print(list(range(1,6,3)))   # Use every third number
# > [1, 4]


# sum = 0
# for count in range(2,11,2):
#     sum += count
#     print("count is ",count )
# print(sum)


## --- Count Down Loop ---
# for count in range(10, 0, -1):
#     print("count is ", count)

# print(list(range(10,0,-1)))
# > [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


## ------ Formatting Output -------
# for x in range(3, 5):
#     print ("x is ", x)
#     print ( "10 ** x is ", 10**x)
# >>> x is  3
# 10 ** x is  1000
# x is  4
# 10 ** x is  10000


# p18  Case Study: An Investment Report
starting_balance = float(input("Enter the starting balance: "))
years = int(input("Enter the number of years: "))
interest_rate = int(input("Enter the interest rate as a %: "))
total = 0.0

table=["Year", "Starting balance", "Interest", "Ending balance"]
for h in table:
    print(h, end=" ")
print("\n")

for year in range(1,years+1):
    interest = starting_balance * interest_rate/100
    ending_balance = starting_balance + interest

    print(year, "{:.2f}".format(starting_balance), "{:.2f}".format(interest), "{:.2f}".format(ending_balance))

    starting_balance = ending_balance
    total += interest
    
print("Ending balance: $ {:.2f}".format(ending_balance))
print("Total interest earned: $ {:.2f}".format(total))

