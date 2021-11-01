from Treatment import Treatment


class Hospital:

    def __init__(self, id, name, address=None, link="", treatments=None, ranking=0):
        self.hospital_id = id
        self.name = name
        self.address = address
        self.link = link
        self.treatments = [] # tuples of treatment_id, treatment_object?
        self.ranking = ranking

        # Might move these later to address class
        self.city = None
        self.state = None

    def set_hospital_id(self, id):
        self.hospital_id = id

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

    def __str__(self):
        return f"id: {self.hospital_id}, name: {self.name}"

    def __repr__(self):
        return f"id: {self.hospital_id}, name: {self.name}"
