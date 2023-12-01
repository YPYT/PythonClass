# Assignment title: Develop a Python program - individual assessment Task 1
# Student Name: Yuka Toshima (20023347)
# Date: 4th December 2023


import glob # to seach the files

# Search all text files that contain 3 capital letters of the alphabet (country code) and assign to files variable
# Loop for all the country text file
for file in glob.glob('[A-Z][A-Z][A-Z].txt'):
  # Get country codes
  country_code = file[:3]
  # Set the total price of each price to 0
  petrol_sum = 0
  gas_sum = 0
  diesel_sum = 0
  # Set the line length of each text file to 0
  num_of_line = 0     

  # Open each country text file as reading mode as country_text_file variable
  with open(file, 'r') as country_text_file:
      # Loop for each line in the country_text_file and assign to the "line" variable
      for line in country_text_file: 
          # Split the line and assign to prices variable         
          prices = line.split()
          # Count the number of line in the each file 
          num_of_line += line.count('\n')

          # Get the first value in each line as a float and assign in the petrol variable
          petrol = float(prices[0])
          # Get the second value in each line as a float and assign in the gas variable
          gas = float(prices[1])
          # Get the third value in each line as a float and assign in the diesel variable
          diesel = float(prices[2])

          # Add each value in petrol to the petrol_sum variable          
          petrol_sum += petrol
          # Add each value in gas to the gas_sum variable          
          gas_sum += gas
          # Add each value in diesel to the diesel_sum variable          
          diesel_sum += diesel

    # average of each unit prices
      petrol_ave = petrol_sum/num_of_line
      gas_ave = gas_sum/num_of_line
      diesel_ave = diesel_sum/num_of_line

  # Assign each price into the result variable formatted to the second decimal place 
  result = "{:.2f} {:.2f} {:.2f}".format(petrol_ave, gas_ave, diesel_ave)
  
  # Open file with write mode and name it COUNTRY_CODE_ave.txt
  result_file = open(country_code + "_ave.txt", 'w')
  # Write the result in the file
  result_file.write(result)
  # Close the file
  result_file.close()

