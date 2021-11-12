from Hospital import Hospital
from Treatment import Treatment

class Ranker:
    treatment_obj = []  
    hospital_obj = []

    def __init__(self):
        pass

    def add_treatments(self, relevant_treatment_object_list):
        self.treatment_obj = treatment_obj_list #list of relevant Treatment Objects

    def get_hospitals(self):
        for t in self.treatment_obj: 
            return t.hospital



if __name__ == "__main__":


    #For Testing
    test_relevant_treatment_object_list = ['A0021', 'B4034', 'C1300'] # load list of treatment HCPCS

    ranker = Ranker()
    ranker.add_treatments(test_relevant_treatment_object_list)
    ranker.get_hospitals()


        