### --- Function (for reusability)
## Concept: 1. define function
##          2. call function

# import random

# articles = ("A", "THE")
# nouns = ("BOY", "GIRL", "DOG", "MOUSE")
# verbs = ("HIT", "RUN", "FOUND", "SAW")
# prepositions = ("WITH", "BY", "AT")

# def sentence():
#     return nounPhrase() + " " + verbPhrase()

# def nounPhrase():
#     return random.choice(articles) + " " + random.choice(nouns)

# def verbPhrase():
#     return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

# def prepositionalPhrase():
#     return random.choice(prepositions) + " " + nounPhrase()

# def main():
#     number = int(input("Enter the number of sentences: "))
#     for count in range(number):
#         print(sentence())

# main()

### -- recursive function --
# def sum(lower, upper):
#     if lower > upper:
#         return 0
#     else:
#         return lower + sum(lower + 1, upper)

# print(sum(1, 3))

########### ????????????????????????? ###########
# def example(string, index):
#     if index < len(string):
#         print("before example() index is ", index)
#         example(string, index + 1)
#         print("after example() index is ", index)

#         print("string[index] is ", string[index])
# example("ABCDE", 0)


# #1. Function define
# def greeting(name):
#     print("Hello, " + name)
# #2. Function call
# greeting("Emily")
# greeting("Jessie")
# greeting("Lisa")


# #1. Function define
# def addition(num1, num2): # num1 and num2 is parameter
#     total = num1 + num2
#     # print("The total is:", total)
#     return total
# # Function call
# addition(3,8) #3, 8 is arguments
# addition(2872, 1762583)
# addition(1.4, 2.4)

# def my_function():
#     print("This is my function")
# def main():
#     my_function()
# main()

# def average(list):
#     sum = 0
#     for num in list:
#         sum += num
#     return sum/len(list)
# print(average([2,1]))


## ------ recursive function -------------
# def displayRange (lower, upper):
#     if lower <= upper:
#         print(lower)
#         displayRange(lower + 1, upper)
# displayRange(2,9)



### -------- map() function
## map(function, iterables)
# def myfunc(n):
#   return len(n)
# x = map(myfunc, ('hahahah', 'banana', 'cherry'))
# #convert the map into a list, for readability:
# print(list(x))
# #>>[5, 6, 6]

# def myfunc(a, b):
#   return a + b
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(x)
# #>> <map object at 0x14c1d55c42b0>
# #convert the map into a list, for readability:
# print(list(x))
# #>> ['appleorange', 'bananalemon', 'cherrypineapple']

# words = ["1", "23", "123", "57"]
# list_words=list(map(int, words))
# print(list_words)
# print(",".join(map(str, list_words)))
# #>> [1, 23, 123, 57]
# #>> 1,23,123,57

# int = [2,5,65,755,34,3]
# float_list = list(map(float, int))
# print(float_list)
# #>>[2.0, 5.0, 65.0, 755.0, 34.0, 3.0]


## P 17
# replacements = {"I": "You", "me": "you", "my": "your", "we":"you", "us":"you", "mine":"yours"}
# def changePerson(sentence):
#     words = sentence.split()
#     print("words:", words)
#     # words: ['I', 'like', 'my', 'car']
#     replyWords = []
#     for word in words:
#         replyWords.append(replacements.get(word,word)) #.get(key,value) if the value of an key that do not exist attend value:
#     print("repluWords: ", replyWords)
#     #repluWords:  ['You', 'like', 'your', 'car']
#     return " ".join(replyWords)

# def main():
#     print(changePerson("I like my car"))

# main()

##P21
# import math
# def example(functionArg, dataArg):
#     return functionArg(dataArg)
# print(example(abs, -4))
# print(example(math.sqrt, 2))


# ### -------- Filtering/Reduce function
# def odd(n): return n % 2 == 1
# nums = [3,2,6,32,11,23,15,85,22,68]
# odd_list = list(filter(odd, nums))
# print(odd_list)
# #>> [3, 11, 23, 15, 85]

# def even(n): 
#     return n % 2 == 0
# nums = [3,2,6,32,11,23,15,85,22,68]
# even_list = list(filter(even, nums))
# print(even_list)
# #>> [2, 6, 32, 22, 68]

# from functools import reduce
# def add(num1, num2): return num1 + num2
# def multiply(num1,num2): return num1 * num2
# data = [1,2,3,4]
# print(reduce(add, data)) #> 10
# print(reduce(multiply, data)) #> 24

# x = ["apple", "peach", "banana"]
# print(reduce(add, x))
# #> applepeachbanana

# from functools import reduce
# numbers = [1,2,3,4,5,6,7,8]
# sum_of_nums = reduce(lambda x,y: x+y, numbers)
# print(sum_of_nums)

#### ------ Tutorial 6
"""
Part 1: (refer to the lecturer note)
• Implement and Run examples 1 to 4
• Implement and run the code in Class Practices 1 and 2
"""



"""
Part 2: Exercises
a) Write the code for a mapping that generates a list of the absolute values of the numbers
in a list named numbers.
b) Write a program that computes and prints the average of the numbers in a text file. 
You should make use of two higher-order functions to simplify the design.
higher-order functions => filtering, map, reduce
"""
# #a)
# numbers = [23,-22,34,45,-56,-2,-9,31]
# abs_list = list(map(abs, numbers))
# print(abs_list)
# #>> [23, 22, 34, 45, 56, 2, 9, 31]

# #b)
# from functools import reduce

# def add(x,y):
#     return x + y

# file = open("integer.txt", "r")
# num_list = []
# for line in file:
#     num_list.extend(line.split())
# # print("num_list: ", num_list)
# int_list = list(map(int, num_list))
# # print("int_list is", int_list)

# sum = reduce(add, int_list)
# # print("sum is", sum)
# if len(int_list) > 0:
#     average = sum / len(int_list)
# print("The average is ", average)

