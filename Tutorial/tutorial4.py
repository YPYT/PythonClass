# Week4 Contents
# - String element (index, len())
# - Slicing for Substrings
# - .split() for string

# data = "Hi, there!"
# for index in range(len(data)):
#     print(index, data[index])
# # >>>
# # 0 H
# # 1 i
# # 2 ,
# # 3  
# # 4 t
# # 5 h
# # 6 e
# # 7 r
# # 8 e
# # 9 !

# print(data[0:]) # > Hi, there!
# print(data[0:1]) # > H
# print(data[0:3]) # > Hi,
# print(data[:len(data)]) # > Hi, there!
# print(data[-3:]) # > re!
# print(data[7:10]) # > re!
# print(data[:5]) # > Hi, t


# fileList = ["ABC.text", "python.py", "LMN.text", "index.html"]
# for fileName in fileList:
#     if ".text" in fileName:
#         print("text file name: ", fileName[:-5])
# # >> 
# # text file name:  ABC
# # text file name:  LMN


# Part 1
# --- Octal to Decimal 
# def octalToDecimal(octal):
#     decimal = 0
#     指数 = len(octal)-1
#     for num in octal:
#         decimal = decimal + int(num) * 8 ** 指数
#         指数 = 指数 - 1
#     print("The decimal is ", decimal)
# octalToDecimal("214")

# --- Decimal to Octal 
# def decimalToOctal(decimal):
#     if decimal < 8:
#         print("The octal is", decimal)
#     else:
#         print("Decimal Reminder Octal")
#         octal = ""
#         while decimal > 0:
#             reminder = decimal % 8
#             decimal = decimal // 8
#             octal = str(reminder) + octal
#             print("%7d%9d%6s"%(decimal, reminder, octal))
#         print("The octal is", octal)
# decimalToOctal(2344444)


# Part 2
# lastName = input("What is your last name: ")
# hourlyWage = int(input("How much is the hourly wage: $"))
# hoursWorked = int(input("How many hours did you work: "))
# total = hourlyWage * hoursWorked
# file = open(lastName + ".txt", "w")
# file.write("<Last name> <Hourly wage> <Hours worked> <Total pay> \n")
# file.write("%10s%12d%15d%12d" % (lastName, hourlyWage, hoursWorked, total))