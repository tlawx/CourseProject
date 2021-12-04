class Price:
    def __init__(self, max=None, min=None, cash=None, gross=None):
        self.max = 0
        self.min = 0
        self.cash = 0
        self.gross = 0

    def set_price_amount(self, type, amount):
        if type == 'max':
            self.max = amount
        elif type == 'min':
            self.min = amount
        elif type == 'cash':
            self.cash = amount
        else:
            self.gross = amount

    def __str__(self):
        return "Gross: ${}, Cash: ${}, Max: ${}, Min: ${}".format(self.gross, self.cash, self.max, self.min)

    def __repr__(self):
        return "Gross: ${}, Cash: ${}, Max: ${}, Min: ${}".format(self.gross, self.cash, self.max, self.min)        