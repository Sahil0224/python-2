from dataclasses import dataclass

# define the invoice data class with four fields 
@dataclass
class Invoice:
    invoice_id: str
    user_id: str
    amount: str
    paid: str

    # a function with data as parameter and return the list of invoice objects
    @staticmethod
    def convert_data(data):
        invoices = []
        # loop through the data list
        for list in data:
             # split the line by comma
            d = [list.strip() for field in list.split(',')]
            # create an invoice object 
            invoice = Invoice(*d)
            # append the invoice object to the list
            invoices.append(invoice)
            # return the list 
        return invoices