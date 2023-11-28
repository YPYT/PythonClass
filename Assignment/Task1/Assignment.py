import glob # to seach the files
from math import fsum # to sum float numbers

# Search all text files that contain 3 capital letters of the alphabet (country code)
for file in glob.glob('[A-Z][A-Z][A-Z].txt'):
  # get and print country code
  country_code = file[:3]
  print(country_code)

  # set total price start with 0
  patrol_sum = []
  gas_sum = []
  diesel_sum= []

  # open county text file
  with open(file, 'r') as country_text_file:
    for line in country_text_file:
        # convert strings to float to sum numbers
        # numbers = [float(item) for item in line.split()]
        # print(numbers)
        # print(numbers)
        # sum float numbers  
        # patrol_sum.append(numbers[0])
        # gas_sum.append(numbers[1])
        # diesel_sum.append(numbers[2])
        # print("Patrol:", fsum(patrol_sum))
        # print("Gas:", fsum(gas_sum))
        # print("Diesel:", fsum(diesel_sum))
        print("Line", float(line[0]))

