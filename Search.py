

class Search: 

    def __init__(self, treatment_descriptions_long, treatment_codes, categories):
        self.treatment_codes = treatment_codes #one dim
        self.treatment_long_description_list = treatment_descriptions_long #two (2) dims ? 
        self.categories = categories
        self.query_category = ''
        self.query = ''
    
    def new_query(self, category, query):
        self.query_category = category
        self.query = query

    def find_possible_treatments(self, category, query):
        #search algorithm to return list of treatments within category that match string: 1)determine if hcpcs code 2) parse phrase & find matches within code

        if query in self.treatment_codes: #HOLD : assume passed HCPCS code
            print("Matched a treatment!")
            return query
        print("Did not find treatment. Please enter search with another description or HCPCS code.")

    
if __name__ == "__main__":

    test_treatment_codes = ['A0021', 'B4034', 'C1300'] # load list of treatment HCPCS
    test_treatment_descriptions_long = ['Ambulance service, outside state per mile, transport (medicaid only)', 'Enteral feeding supply kit; syringe fed, per day, includes but not limited to feeding/flushing syringe, administration set tubing, dressings, tape','Hyperbaric oxygen under pressure, full body chamber, per 30 minute interval']
    test_treatment_descriptions_short = ['Outside state ambulance serv', 'Enter feed supkit syr by day','Hyperbaric oxygen']
    test_categories = [] # pull in query
    test_query = 'A0020' # pull in query
    test_query_category = '' # pull in query

    search = Search(test_treatment_descriptions_long, test_treatment_codes,test_categories)
    search.new_query(test_query_category, test_query)
    
    results = search.find_possible_treatments(test_query_category, test_query) # treatment list

        