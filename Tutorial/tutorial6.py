# Week6 Contents
# - function
# - mapping
# - fliter
# - reduce


# #scope
# x = 5
# def f():
#     x = 10
# f()
# print(x) #5

# # -- Mapping
# numbers = ["12","13","14","15","16","17"]
# print(map(int,numbers)) #<map object at 0x102deafa0>
# print(list(map(int,numbers))) #[12, 13, 14, 15, 16, 17]

# # -- Filter
# def even(n):
#     return n % 2 == 0
# print(list(filter(even, range(10)))) #[0, 2, 4, 6, 8]
# print(list(filter(even, range(20)))) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# # -- Reduce
# from functools import reduce
# def add(x,y):
#     return x + y
# def multiply(x,y):
#     return x*y

# data = list(range(10))
# print(data) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(reduce(add, data)) #45
# print(reduce(multiply,data)) #0
