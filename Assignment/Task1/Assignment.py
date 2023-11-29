import glob # to seach the files
from datetime import date # to know how many days between starting day and end day
import math

print("Code Petrol Gas Diesel")



# Search all text files that contain 3 capital letters of the alphabet (country code)
for file in glob.glob('[A-Z][A-Z][A-Z].txt'):
  # assign starting day in start_day variable
  start_day = date(2020, 3, 21)
  end_day = date(2020, 12, 31)
  # Calculate the number of days between the start and end dates to know the number of weeks
  # abs() function is to provide the absolute value of the number of days
  number_of_days = abs(start_day-end_day).days
  # list_len is the number of rows for the unit prices and the starting day is including in the first day, so add 1
  # Floor division: "//" operator rounds down to the nearest whole number
  list_len = number_of_days//7 + 1
  # print(list_len)
  # get country code
  country_code = file[:3]
  # set total price start with 0
  petrol_sum = 0
  gas_sum = 0
  diesel_sum= 0
  # set sum list 
  # petrol_sum_list = []
  # gas_sum_list = []
  # diesel_sum_list = []



  result_list = []

  # open county text file
  with open(file, 'r') as country_text_file:
      for line in country_text_file:
          numbers = line.split()
          # print(numbers)
          petrol = float(numbers[0])
          # print("petrol", petrol)
          gas = float(numbers[1])
          # print("gas", gas)
          diesel = float(numbers[2])
          # print("diesel", diesel)

          # print(petrol)
          petrol_sum += petrol
          gas_sum += gas
          diesel_sum += diesel

          # petrol_sum_list.append(petrol)
          # gas_sum_list.append(gas)
          # diesel_sum_list.append(diesel)

      # print("petrol sum:", petrol_sum)
      # print("gas sum:", gas_sum)
      # print("diesel sum:", diesel_sum)

      # print("list", petrol_sum_list)

      # print(petrol_len)
  petrol_ave = petrol_sum/list_len
  # print("petrol ave",petrol_ave)
    
  gas_ave = gas_sum/list_len
  # print("gas average", gas_ave)

  diesel_ave = diesel_sum/list_len
  # print("diesel average", diesel_ave)
  

  # print("Code Petrol Gas Diesel")
  # print(country_code,"{%5d} {%8d} {%12d}".format((petrol_ave, gas_ave, diesel_ave)))
  # print("{} {:>5.2f} {:>5.2f} {:>5.2f}".format(country_code,petrol_ave, gas_ave, diesel_ave))
  result_table = "{} {:>5.2f} {:>5.2f} {:>5.2f}".format(country_code,petrol_ave, gas_ave, diesel_ave)


print(result_table)

