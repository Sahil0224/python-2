class Calculator:
    # constructor with two parameter 
    def __init__(self, num1, num2):
        # store the numbers
        self.num1 = num1
        self.num2 = num2
        self.result = None
    # method to add, sub, mul and div
    def add(self):
        self.result = self.num1 + self.num2
    def sub(self):
        self.result = self.num1 - self.num2
    def mul(self):
        self.result = self.num1 * self.num2
    def div(self):
        self.result = self.num1 / self.num2
    # method to return the result
    def get_result(self):
        return self.result
