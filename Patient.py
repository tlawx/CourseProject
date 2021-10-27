from Treatment import Treatment


class Patient:
    def __init__(self, name):
        self.name = name

    treatments_needed = []
    queries = []
    preferred_locations = []
    selected_hospitals = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_query(self, new_query):
        self.queries.append(new_query)

    def add_treatment_object(self, treatment):
        self.treatments_needed.append(treatment)

    def add_new_treatment(self, treatment_name, treatment_price):
        self.treatments_needed.append(Treatment(treatment_name, treatment_price))

    def set_treatments(self, treatments):
        self.treatments_needed = treatments

    def get_treatments(self):
        return self.treatments_needed
