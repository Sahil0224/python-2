class TaxMan:
    # define the constructor which has list of items and a percent sales tax as parameter
    def __init__(self, items, tax):
        # store the items and tax as attributes
        self.items = items
        self.tax = tax
        # initialize the total price to 0
        self._total = 0
        # method to calculate total price including sales tax
    def calc_total(self):
        # get tax rate as decimal by removing percent sign and divide by 100
        tax_rate = float(self.tax.strip('%')) / 100
        # loop through the items in the list
        for item in self.items:
            # get price of the current item
            price = item['price']
            # add the price plus the tax 
            self._total += price + price * tax_rate
            # round it to two decimal price 
            self._total = round(self._total, 2)
    # getter method to return the total price
    def get_total(self):
        return self._total
        
