

class Search:
    treatment_codes = []  # one dim
    treatment_long_description_list = []  # two (2) dims ?
    categories = []
    category_name = ''
    query = ''
    category_code = ''

    def __init__(self):
        pass

    def add_treatments(self, treatment_descriptions_long, treatment_codes, categories):
        self.treatment_codes = treatment_codes # one dim
        self.treatment_long_description_list = treatment_descriptions_long # two (2) dims ?
        self.categories = categories

    def new_query(self, category_code, category_name, query):
        self.category_code = category_code
        self.category_name = category_name
        self.query = query

    def find_possible_treatments(self):
        # search algorithm to return list of treatments within category that match string: 1)determine if hcpcs code 2) parse phrase & find matches within code

        # OUTLINE:
        # 1. get list of treatments that start with category_code
        category_treatments = get_treatments_in_category(self.category_code)

        # 2. search for relevant treatments from the category
        relevant_treatments = get_relevant_treatments(category_treatments, self.query)

        # 3. rank relevant treatments
        ranked_treatments = get_ranked_treatments(relevant_treatments)

        # 4. print out treatments, their hospitals, price, hospital link, etc, in a nice format
        print_treatment_info(ranked_treatments)

        if self.query in self.treatment_codes: # HOLD : assume passed HCPCS code
            print("Matched a treatment!")
            return self.query
        print("Did not find treatment. Please enter search with another description or HCPCS code.")


def get_treatments_in_category(category_code):
    # TODO: for given category code return list of treatments 
    category_treatments = []
    return category_treatments


def get_relevant_treatments(category_treatments, query):
    # TODO: given all the treatments in a specific category, select the relevant ones that match the query
    relevant_treatments = []
    return relevant_treatments


def get_ranked_treatments(relevant_treatments):
    # TODO: rank the relevant treatments based on price
    ranked_treatments = []
    return ranked_treatments


def print_treatment_info(treatments):
    # TODO: print (for each treatment) treatment name, treatment price, hospital name, hospital location, hospital link
    pass


if __name__ == "__main__":

    test_treatment_codes = ['A0021', 'B4034', 'C1300'] # load list of treatment HCPCS
    test_treatment_descriptions_long = ['Ambulance service, outside state per mile, transport (medicaid only)', 'Enteral feeding supply kit; syringe fed, per day, includes but not limited to feeding/flushing syringe, administration set tubing, dressings, tape','Hyperbaric oxygen under pressure, full body chamber, per 30 minute interval']
    test_treatment_descriptions_short = ['Outside state ambulance serv', 'Enter feed supkit syr by day','Hyperbaric oxygen']
    test_categories = [] # pull in query
    test_query = 'A0020' # pull in query
    test_query_category = '' # pull in query

    search = Search()
    search.add_treatments(test_treatment_descriptions_long, test_treatment_codes, test_categories)
    search.new_query("A", test_query_category, test_query)
    
    #results = search.find_possible_treatments(test_query_category, test_query) # treatment list

        