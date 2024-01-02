# Week 5 Contents
# - list []
# - dictionary {}

# Part1
# sentence = input("Enter one sentence: ")
# words = sentence.split()
# index = 0
# while index < len(sentence):
#     words[index] = words[index].upper()
#     index += 1
# upperSentence = (",").join(words)
# print(upperSentence)

# numbers = list(range(6))
# print(numbers)
# numbers[0:3] = [10,11,12]
# print(numbers)
# numbers[2:4] = [13,12]
# print(numbers)

# numbers = list(range(6))
# numbers[2:5] = [200,300,400]
# print(numbers)

#---- Insert and Removing Elements ------
# INSERT- 
# numbers = [0,1,2,3,4,5]
# #1. insert(INDEX, new_element)
# numbers.insert(1,100)
# print(numbers)
# numbers.insert(2,200)
# print(numbers)

# #2. append(ELEMENTS)
# numbers.append(10)
# print(numbers)

# #3. extend(LIST)
# numbers.extend([11,12,13,14])
# print(numbers)

# REMOVE-
# numbers = [0,1,2,3,4,5,6,7]
# numbers.pop()
# print(numbers) #[0, 1, 2, 3, 4, 5, 6]
# numbers.pop(2)
# print(numbers) #[0, 1, 3, 4, 5, 6]
# numbers.pop(2)
# print(numbers) #[0, 1, 4, 5, 6]


# first = [1,2,3]
# second = first
# print("first: ", first)
# print("second: ", second)
# # first:  [1, 2, 3]
# # second:  [1, 2, 3]
# first[1] = 20
# print("first: ", first)
# print("second: ", second)
# # first:  [1, 20, 3]
# # second:  [1, 20, 3]

# # -- Dictionary
# info = {}
# info["name"] = "ABC"
# info["DOB"] = "1/1"
# print(info) #{'name': 'ABC', 'DOB': '1/1'}
# info["DOB"] = "11/13"
# print(info) #{'name': 'ABC', 'DOB': '11/13'}

# print(info["name"]) #ABC
# print(info["DOB"]) #11/13

# print(info.pop("DOB")) # 11/13
# print(info) #{'name': 'ABC'}

