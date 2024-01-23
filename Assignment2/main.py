# Assignment title: Develop an advanced Python application – individual assessment 3
# Student Name: Yuka Toshima (20023347)
# Date: 24th January 2024


# Import Product class from product.py file and checkoutregister class from checkoutregister.py file
from checkoutregister import CheckoutRegister
from product import Product

# Create product object from Product class and add to the products list
products =[
    Product("Milk", 3.0, "001", 10),
    Product("Cheese", 6.0, "002", 40),
    Product("cookie", 2.0, "003", 100),
    Product("coffee", 6.5, "004", 20),
    Product("Stake", 15.5, "005", 10)
]

# Create casher registar object called c1 from CheckoutRegister class
c1 = CheckoutRegister()

# Define the main method
def main():

    # Display "----- Welcome to Happy-Mart checkout! -----"
    print("----- Welcome to Happy-Mart checkout! -----")
    # Loop through while True
    while True: 
        # Set isExist variable and assign False into it
        isExist = False 
        # Input product's barcode from customer and assign into the inputBarcode variable 
        inputBarcode = input("Please enter the barcode of your item: ")
        
        # Loop through products object that created from class and perform the following processing for each product
        for product in products:
            # If inputBarcode is equal to the product barcode, the product's stock reduce 1
            if inputBarcode == product.barcode:
                product.stock -= 1
                # If the stock of the product is 0, display "This product is the last one."
                if product.stock == 0:
                    print("This product is the last one.")
                # If stock of the product is equal or less than -1, break the for loop
                elif product.stock <= -1:
                    break

                # Scan the product to the casher registar(c1) 
                c1.scan_item(product)
                # The 'total' variable is original total price for the receipt
                total = c1.total_amount
                # Assign True to isExist variable
                isExist = True

        # If isExist is not True, display "This product does not exist in our inventory."
        if  isExist != True:
            print("This product does not exist in our inventory.")

        # Loop through while True
        while True:
            # Set the break_scan variable and assign False. This is to break another outer while loop if the customer does not want to scan any more products.
            break_scan = False
            # Ask to the customer if there is any products that they want to scan, and assign the answer to nextScan varible
            nextScan = input("Would you like to scan another product? (Y/N)") 
            # If the nextScan is not either 'Y' or 'N', display "Enter 'Y'(yes) or 'N'(no)", and continue the loop
            if nextScan.upper() not in ['Y', 'N']:
                print("Enter 'Y'(yes) or 'N'(no)") 
            # If the nextScan is 'Y' or 'N' and if the value is 'N', assign True to the break_scan variable and then break the while loop.
            else:
                if nextScan.upper() == 'N':
                    break_scan = True
                break
        # If break_scan is True, break the while loop for scan products
        if break_scan:
            break

    # Loop through while the value of is_paid for c1 is False
    while c1.is_paid == False:
        # Ask the amount that the customer want to put into the register and assign into the amount variable with float data type
        amount = float(input("Total price: ${:.2f}. Please enter an amount to pay: ".format(c1.total_amount)))
        # Use the accept_payment function with the amount as argument in c1
        c1.accept_payment(amount)
        
    # Print receipt for the c1 with amount as an argument
    c1.print_receipt(amount, total)

    # Loop through while True
    while True:
        # Ask customer if they want to quit or change to the next customer and assign the answer to the variable called next 
        next = input("(N)ext customer, or (Q)uit?")

        # If uppered value of next is 'N', c1 will be reset to the default and call main() to start the register and break the while loop
        if next.upper() == "N":
            c1.reset_register()
            main()
            break

        # If uppered value of next is 'Q', break the loop
        elif next.upper() == "Q": 
            break

        # If the answer isn't 'N' or 'Q', display "Input invalid, (N)ext customer, or (Q)uit?" and continue to ask.
        else:
            print("Input invalid, (N)ext customer, or (Q)uit?")
            
# call main() function
main()

    