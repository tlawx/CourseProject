from Treatment import Treatment


class Category:
    def __init__(self, name, treatments=[]):
        self.name = name
        self.treatments = treatments

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_treatment_object(self, treatment):
        self.treatments.append(treatment)

    def add_new_treatment(self, treatment_name, treatment_price):
        self.treatments.append(Treatment(treatment_name, treatment_price))

    def set_treatments(self, treatments):
        self.treatments = treatments
