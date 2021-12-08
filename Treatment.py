
class Treatment:
    def __init__(self, concept_id, concept_code, vocabulary_id, treatment_name, hospitals={}, treatment_price=0.0, category=""):
        self.concept_id = concept_id
        self.concept_code = concept_code
        self.vocabulary_id = vocabulary_id
        self.treatment_name = treatment_name
        self.treatment_price = treatment_price
        self.category = category
        self.hospitals = hospitals


