from Treatment import Treatment


class Hospital:

    def __init__(self, name, city, state, affiliation, link="", treatments=[], rating=0):
        self.name = name
        self.city = city
        self.state = state
        self.affiliation = affiliation
        self.link = link
        self.treatments = treatments
        self.rating = rating

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_affiliation(self, affiliation):
        self.affiliation = affiliation

    def get_affiliation(self):
        return self.affiliation

    def set_link(self, link):
        self.link = link

    def get_link(self):
        return self.link

    def add_treatment_object(self, treatment):
        self.treatments.append(treatment)

    def add_new_treatment(self, treatment_name, treatment_price):
        self.treatments.append(Treatment(treatment_name, treatment_price))

    def set_treatments(self, treatments):
        self.treatments = treatments

    def get_treatments(self):
        return self.treatments

    def set_rating(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.rating
