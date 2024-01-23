# Assignment title: Develop an advanced Python application – individual assessment 3
# Student Name: Yuka Toshima (20023347)
# Date: 24th January 2024


# Import Product class from product.py file
from product import Product 
# Make CheckoutRegister class
class CheckoutRegister(object):
    # define __init__(constructor) method with attributes;cart_list, total_amount, is_paid
    def __init__(self): # 
        # Setting the initial value for each attribute
        self.cart_list = []
        self.total_amount = 0.0
        self.is_paid = False

    # Define the scan_item method and take a parameter called product
    def scan_item(self, product):
        # Add product(value) to the cart_list list
        self.cart_list.append(product)
        # Display product name and price to two decimal places
        print(product.name + " : $%0.2f" % product.price)
        # Display the number of products in stock
        print("Stock: " + str(product.stock))
        # Add the price of product to the total_amount variable
        self.total_amount += product.price
        

    # Define the accept_payment method and take a parameter called amount
    def accept_payment(self, amount):

        ## If the amount is negative, display "We don't accept negative money!"
        if amount < 0:
            print("We don't accept negative money!")

        ## If the amount is more than the total products amount, assign True to the is_paid attribute
        ## and display the change amount and "Payment completed. Thank you very much."
        elif amount >= self.total_amount:
            self.is_paid = True
            print("Change: $" + str(amount-self.total_amount))
            print("Payment completed. Thank you very much.")
            print("\n") # next line

        ## If the amount is less than the total products amount, assign False to the is_paid attribute
        ## and subtract amount from total_amount and substitute the remaining amount for total_amount and display the remining amount 
        else: 
            self.is_paid = False
            self.total_amount -= amount
            print("Remaining payments: $" + str(self.total_amount))

    # Define the print_receipt method and take a parameter called amount
    def print_receipt(self, amount, total):
        # Display "----- Happy-Mart Receipt -----"
        print("----- Happy-Mart Receipt -----")
        # Loop through the products in cart_list and perform the following processing for each product
        for product in self.cart_list:
            # Display product name and price to two decimal places
            print(product.name + " ${:.2f}".format(product.price))
        # Display Total amount to two decimal places
        print("Total amount: ${:.2f}".format(total))
        # Display received amount to two decimal places
        print("Amount received: ${:.2f}".format(amount))
        # Display change amount to two decimal places
        print("Change given: ${:.2f}" .format(amount-self.total_amount))
        # Display "Thank you for shopping at Happy-Mart!"
        print("Thank you for shopping at Happy-Mart!")

    # Define the reset_register method to reset the registar for the next person
    def reset_register(self):
        # Set all the valiable to initial value
        self.cart_list = []
        self.total_amount = 0.0
        self.is_paid = False
