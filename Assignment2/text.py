from product import Product 
products =[
    Product("Milk", 3.0, "001", 10),
    Product("Cheese", 6.0, "002", 40),
    Product("cookie", 2.0, "003", 100),
    Product("coffee", 6.5, "004", 20),
    Product("Stake", 15.5, "005", 10)
]


class Test():
    def __init__(self): # 
        # Setting the initial value for each attribute
        self.cart_list = []
        self.total_amount = 9.0
        self.is_paid = False

    def accept_payment(self, amount):
        self.is_paid = False

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
#レシート--------------------------------------------------------------------------------------------------------------------
    # Define the print_receipt method and take a parameter called amount
    def print_receipt(self, amount, total):
        # Display "----- Happy-Mart Receipt -----"
        print("----- Happy-Mart Receipt -----")
        change = amount - self.total_amount 

        # Display Total amount to two decimal places
        print("Total amount: ${:.2f}".format(total))
        # Display received amount to two decimal places
        print("Amount received: ${:.2f}".format(total+change))
        # Display change amount to two decimal places
        
        print("Change given: ${:.2f}" .format(change))
        # Display "Thank you for shopping at Happy-Mart!"
        print("Thank you for shopping at Happy-Mart!")
# ---------------------------------------------------------------------------------------
t1 = Test()
 # Loop through while the value of is_paid for c1 is False
total = t1.total_amount
while t1.is_paid == False:
        # Ask the amount that the customer want to put into the register and assign into the amount variable with float data type
    amount = float(input("Total price: ${:.2f}. Please enter an amount to pay: ".format(t1.total_amount)))
        # Use the accept_payment function with the amount as argument in c1
    
    t1.accept_payment(amount)

        
    # Print receipt for the c1 with amount as an argument
t1.print_receipt(amount,total)