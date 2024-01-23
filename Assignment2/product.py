# Assignment title: Develop an advanced Python application – individual assessment 3
# Student Name: Yuka Toshima (20023347)
# Date: 24th January 2024


# Make Product class
class Product:
    # define __init__(constructor) method with attributes; name, price, barcode, stock
    def __init__(self, name, price, barcode, stock):
        # Setting the initial value for each attribute
        self.name = name
        self.price = price
        self.barcode = barcode
        self.stock = stock
    
