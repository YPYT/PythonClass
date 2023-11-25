# ##--------- Structure of String --------- 

# print(len("Yuka"))  #>4
# print(len(""))  #>0

# name = "Alan Turing"
# print(len(name)) #>11
# print(name[0]) #>A
# print(name[3]) #>n

# #name[len(name)] #IndexError: string index out of range
# print(name[len(name)-1]) #=> name[11-1]=name[10]   >g
# print(name[-1]) #g 

# data="Hi there!"
# print(len(data)) #> 9
# for ind in range(len(data)):  #range(len(data))>>range(9)
#     print(ind, data[ind])
### 0 H
### 1 i
### 2  
### 3 t
### 4 h
### 5 e
### 6 r
### 7 e
### 8 !

# ##--------- Slicing of Substrings --------- 
# ## Substrings : portions of strings. Operation of obtaining a substring is slicing 
# name = "myfile.tex"
# print(name[0:])   #The entire string > myfile.text
# print(len(name))  #11
# print(name[:len(name)]) #The entire string > myfile.text  ##print(name[:11])
# print(name[:11]) #The entire string > myfile.text
# print(name[:5]) #The first 5 characters > myfil

# print(name[11:])  #### NOTHING with no error

# print(name[0:1])  #The first character > m
# print(name[0:2])  #The first two characters > my
# print(name[1:3])  #Between index 1-3 > yf 

# print(name[-3:]) #The last 3 characters > tex
# print(name[:-3]) #Until the last 3 characters > myfile.


# fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
# for fileName in fileList:
#     if ".txt" in fileName:
#         print(fileName)
# ## myfile.txt
# ## yourfile.txt

# name = "myfile.txt"
# print(".txt" in name) #>True

# ##--------- Strings and Number System ---------
# ## DecimalToBinary program
# decimal = int(input("Enter a decimal integer: "))
# if decimal == 0:
#     print(0)
# else:
#     print("Quotient Remainder Binary")
#     bstring = ""
#     while decimal > 0:
#         remainder = decimal % 2
#         decimal = decimal // 2
#         bstring = str(remainder) + bstring
#         print("%5d%8d%12s" % (decimal, remainder, bstring))
#     print("The binary representation is ", bstring)

## Enter a decimal integer: 6 
## Quotient Remainder Binary
##    3       0           0
##    1       1          10
##    0       1         110
##The binary representation is  110

## BinaryToDecimal program
# bstring = input("Enter a string of bits: ")
# decimal = 0
# exponent =len(bstring) -1
# for digit in bstring:
#     decimal = decimal + int(digit) * 2 ** exponent
#     exponent = exponent -1
# print("The integer value is", decimal)

## Enter a string of bits: 11100011
## The integer value is 227


# ##--------- String Method ---------
# ## *String Method split to obtain a list of the words contained in an input string.

# sentence = input("Enter a sentence: ")
# ## This sentence has no long words.
# listOfWords = sentence.split()
# print("List of words is" ,listOfWords)
# ##> List of words is ['This', 'sentence', 'has', 'no', 'long', 'words.']
# print("There are", len(listOfWords), "words.")

# sum = 0
# for word in listOfWords:
#     #print(word)
#     sum += len(word)
# print("The average word length is", sum/len(listOfWords))


# s = "Hi there!"
# ## .center()
# print(s.center(11)) #>  ' Hi there! '
# ## .count()
# print(s.count('e')) #> 2
# ## .endswith()
# print(s.endswith("there!")) #> True
# print(s.endswith("re!"))  #> True
# print(s.endswith("the"))  #> False
# print(s.endswith("Hi")) #> False
# ## .startswith()
# print(s.startswith("Hi")) #> True
# ## .find()
# print(s.find("the")) #> 3
# print(s.find("i"))  #> 1
# print(s.find("re")) #> 6
# print(s.find("!")) #> 8
# ## .isalpha()
# print(s.isalpha()) #> False
# print("abc".isalpha()) #> True
# print("abf".isalpha()) #> True
# print("hithere".isalpha()) #> True
# print("hi there".isalpha()) #> False
# ## .isdigit()
# print("245".isdigit()) #> True
# ## .split()
# words = s.split()
# print(words) #> ['Hi', 'there!']
# ## .join()
# print("".join(words)) #> Hithere!
# print(" ".join(words)) #> Hi there!
# ## .lower()
# print(s.lower()) #> hi there!
# ## .upper()
# print(s.upper()) #> HI THERE!
# ## .replace()
# print(s.replace("i","o")) #> Ho there!
# ## .strip()
# print(" Hi, there! ".strip()) #> 'Hi, there!'

# print("myfile.txt".split("."))  #> ['myfile', 'txt']
# print("myfile.html".split("."))  #> ['myfile', 'html']

# filename = "myfile.html".split(".") ##['myfile', 'html']
# print(filename[1]) #> html


# ## --------- Writing Text to a File ---------
# ## *Data can be output to a text file using a file object
# f = open("myfile.txt", 'w')
# f.write("First line. \nSecond line. \n")
# f.close()

# ##--------- Writing Integer to a File ---------
# import random
# f= open("integer.txt", 'w')
# for count in range(100):
#     number = random.randint(1,100)
#     f.write(str(number) + "\n")
# f.close()

##--------- Reading Text From a File ---------
# f = open("myfile.txt", 'r')
# text = f.read()
# print(text)
# ## First line. 
# ##Second line. 

# for line in f:
#     print(line)
# ## First line. 
# ##
# ## Second line.

# ##--------- Reading Number From a File ---------
# f = open("integer.txt", 'r')
# sum = 0
# for line in f:
#     line = line.strip()
#     number = int(line)
#     sum += number
# print("The sum is", sum)
# ## > The sum is 5161

# ##--------- File and Directory Operations ---------
# import os
# currentDirectoryPath = os.getcwd()
# print(currentDirectoryPath)  #> /Users/yukatoshima/Desktop/VSC/Python
# listOfFileNames = os.listdir(currentDirectoryPath)
# print(listOfFileNames) #> ['week2.py', 'week3.py', 'integer.txt', 'myfile.txt', '.git', 'week4.py']
# for name in listOfFileNames:
#     if ".py" in name:
#         print(name)
# ## week2.py
# ## week3.py
# ## week4.py


# ##--------- Week 4 – Exercises ---------
# ## octalToDecimal

# oct = input("Enter a string of octal bits: ")
# decimal = 0
# exponent =len(oct) -1
# print("len(oct) is", len(oct))
# for digit in oct:
#     print("int(digit) is",int(digit))
#     decimal = decimal + int(digit) * 8 ** exponent
#     exponent = exponent -1
# print("The integer value is", decimal)
# ## Enter a string of octal bits: 637
# ## len(oct) is 3
# ## int(digit) is 6
# ## int(digit) is 3
# # #int(digit) is 7
# ## The integer value is 415


# ##  decimalToOctal program
# decimal = int(input("Enter a decimal integer: "))
# if decimal < 8:
#     print("The Octal representation is ", decimal)
# else:
#     print("Quotient Remainder Octal")
#     bstring = ""
#     while decimal > 0:
#         remainder = decimal % 8
#         decimal = decimal // 8
#         bstring = str(remainder) + bstring
#         print("%5d%8d%10s" % (decimal, remainder, bstring))
#     print("The octal representation is ", bstring)

# ## Enter a decimal integer: 415
# ## Quotient Remainder Octal
# ##    51       7           7
# ##     6       3          37
# ##     0       6         637
# ## The octal representation is  637