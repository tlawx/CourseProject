class Treatment:
    def __init__(self, concept_id, concept_code, vocabulary_id, treatment_name, treatment_price=0.0):
        self.concept_id = concept_id
        self.concept_code = concept_code
        self.vocabulary_id = vocabulary_id
        self.treatment_name = treatment_name
        self.treatment_price = treatment_price

    def set_treatment_name(self, name):
        self.treatment_name = name

    def get_treatment_name(self):
        return self.treatment_name

    def set_treatment_price(self, price):
        self.treatment_price = price

    def get_treatment_price(self):
        return self.treatment_price
