class Treatment:
    def __init__(self, category, treatment_name, treatment_price=0.0):
        self.category = category
        self.treatment_name = treatment_name
        self.treatment_price = treatment_price

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_treatment_name(self, name):
        self.treatment_name = name

    def get_treatment_name(self):
        return self.treatment_name

    def set_treatment_price(self, price):
        self.treatment_price = price

    def get_treatment_price(self):
        return self.treatment_price
