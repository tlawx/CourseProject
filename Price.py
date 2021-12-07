import math
class Price:
    def __init__(self, max=None, min=None, cash=None, gross=None):
        self.max = 0.0
        self.min = 0.0
        self.cash = 0.0
        self.gross = 0.0

    def set_price_amount(self, type, amount):
        amount = self.adjust_decimal_point(amount)
        if type == 'max':
            self.max = amount
        elif type == 'min':
            self.min = amount
        elif type == 'cash':
            self.cash = amount
        else:
            self.gross = amount

    def get_average_price(self):
        prices = []
        if self.max > 0.0:
            prices.append(self.max)
        if self.min > 0.0:
            prices.append(self.min)
        if self.gross > 0.0:
            prices.append(self.gross)
        if self.cash > 0.0:
            prices.append(self.cash)

        return str(sum(prices) // len(prices))

    def adjust_decimal_point(self, amount): 
        if '.' in amount:
            number, decimal = amount.split(".")
            if len(decimal) < 2:
                decimal += "00"
            amount = number + "." + decimal[:2]
        return float(amount)

    def __str__(self):
        return "Price Gross: ${}, Cash: ${}, Max: ${}, Min: ${}".format(self.gross, self.cash, self.max, self.min)

    def __repr__(self):
        if self.gross !=0.0 and self.max !=0.0 and self.min !=0.0 and self.cash !=0.0:
            return "Treatment Price: Gross: ${}, Cash: ${}, Max: ${}, Min: ${}".format(self.gross, self.cash, self.max, self.min)
        else:
            return "Treatment Average Cost: ${}".format(self.get_average_price())