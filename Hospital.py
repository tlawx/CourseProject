import Treatment


class Hospital:

    def __init__(self, name, address, link="", treatments=[], ranking=0):
        self.name = name
        self.address = address
        self.link = link
        self.treatments = treatments
        self.ranking = ranking

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

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

    def set_ranking(self, ranking):
        self.ranking = ranking

    def get_ranking(self):
        return self.ranking
