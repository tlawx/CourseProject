from Hospital import Hospital


class Treatment:
    def __init__(self, concept_id, concept_code, vocabulary_id, treatment_name, hospitals={}, treatment_price=0.0, category=""):
        self.concept_id = concept_id
        self.concept_code = concept_code
        self.vocabulary_id = vocabulary_id
        self.treatment_name = treatment_name
        self.treatment_price = treatment_price
        self.category = category
        self.hospitals = hospitals

    def set_treatment_name(self, name):
        self.treatment_name = name

    def get_treatment_name(self):
        return self.treatment_name

    def set_treatment_price(self, price):
        self.treatment_price = price

    def get_treatment_price(self):
        return self.treatment_price

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def add_hospital_dict(self, hospital_id, hospital_object):
        self.hospitals[hospital_id] = hospital_object

    def add_new_hospital(self, hospital_id, name, city=None, state=None, affiliation=None, link="", treatments=None, rating=0):
        hospital = Hospital(hospital_id, name, city, state, affiliation, link, treatments, rating)
        self.hospitals[hospital_id] = hospital

    def get_hospital(self):
        return self.hospitals
