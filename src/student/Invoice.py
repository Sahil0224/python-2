from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_id: str
    user_id: str
    amount: str
    paid: str

def convert_data(data):
    invoices = []

    for list in data:
        d = [d.strip() for field in list.split(',')]
        invoice = Invoice(*d)
        invoices.append(invoice)
    return invoices