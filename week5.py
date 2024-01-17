# first = [1,2,3,4]
# second = list(range(1,5))
# print(first)
# print(second)
# # [1, 2, 3, 4]
# # [1, 2, 3, 4]


# third = first + [5,6]
# print(third)
# # [1, 2, 3, 4, 5, 6]
# print(third[4]) #5


# nums = [1, 2, 3, 4, 5, 6]
# index = 0
# while index < len(nums):
#     nums[index] = nums[index] ** 2
#     index += 1
# print(nums)
# # [1, 4, 9, 16, 25, 36]

# ex = [1,2,3,4]
# print(ex.index(3)) #2
# ex.insert(1, 10)
# print(ex) 
# # [1, 10, 2, 3, 4]

# num = [2,5,1,9,4]
# sort_num = num.sort()
# print(sort_num)


# ####------ Tuple
# # tuple: can not change


# ####------ Function

# def main():
#     number = float(input("Enter number:"))
#     result = square(number)
#     print("The square of", number, "is", result)
# def square(x):
#     return x * x
# main()

# ####------ Dictionary
# # dictionary = {key, value}

# person_info = {"name": "monky","phone": 123,"mail": "aaaa"} 
# print(person_info["name"]) #monky
# print(person_info["phone"]) #123


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