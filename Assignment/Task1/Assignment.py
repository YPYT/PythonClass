import glob # to seach the files

# Search all text files that contain 3 capital letters of the alphabet (country code)
for file in glob.glob('[A-Z][A-Z][A-Z].txt'):
  # get country code
  country_code = file[:3]
  # set total price start with 0
  petrol_sum = 0
  gas_sum = 0
  diesel_sum= 0

  # set sum list 
  petrol_sum_list = []
  gas_sum_list = []
  diesel_sum_list = []

  # open county text file
  with open(file, 'r') as country_text_file:
      for line in country_text_file:
          prices = line.split()
          # print(prices)
          petrol = float(prices[0])
          # print("petrol", petrol)
          gas = float(prices[1])
          # print("gas", gas)
          diesel = float(prices[2])
          # print("diesel", diesel)

          # add the price in each lines and assign to the variable (example: petrol_sum = petrol_sum + petrol)
          petrol_sum += petrol
          gas_sum += gas
          diesel_sum += diesel

          # Add all petrol values into the petrol_sum_list variable
          petrol_sum_list.append(petrol)
          gas_sum_list.append(gas)
          diesel_sum_list.append(diesel)

      # average of each unit prices
      petrol_ave = petrol_sum/len(petrol_sum_list) 
      gas_ave = gas_sum/len(gas_sum_list)
      diesel_ave = diesel_sum/len(diesel_sum_list)

  

  result = "{:.2f} {:.2f} {:.2f}".format(petrol_ave, gas_ave, diesel_ave)
  
  # open file with write mode and name it COUNTRY_CODE_ave.txt
  result_file = open(country_code + "_ave.txt", 'w')
  # write the result in the file
  result_file.write(result)
  # close the file
  result_file.close()

