from meta import Meta
from driver import Driver


class Search:
    treatment_codes = []  # one dim
    treatment_long_description_list = []  # two (2) dims ?
    categories = []

    def __init__(self, category_code, query):
        self.category_code = category_code
        self.query = query

    def find_possible_treatments(self):
        # OUTLINE:
        # 1. get correct config file from a method in driver

        # 2. search for relevant treatments from the category

        m = Meta()
        relevant_treatments = m.search_inverted_index(self.query)
        #print(relevant_treatments)
        return(relevant_treatments)

        # 3. print out treatments, their hospitals, price, hospital link, etc, in a nice format
        # print_treatment_info(relevant_treatments)

    def find_treatments(self):
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

    def add_treatments(self, treatment_descriptions_long, treatment_codes, categories):
        self.treatment_codes = treatment_codes # one dim
        self.treatment_long_description_list = treatment_descriptions_long # two (2) dims ?
        self.categories = categories

    def add_treatments(self, treatment_descriptions_long, treatment_codes, categories):
        self.treatment_codes = treatment_codes # one dim
        self.treatment_long_description_list = treatment_descriptions_long # two (2) dims ?
        self.categories = categories

    def print_treatment_info(treatments):
        # TODO: print (for each treatment) treatment name, treatment price, hospital name, hospital location, hospital link
        pass
    
    def get_treatment_list(self, treatments):
        # TODO: 
        index_list = []
        for tup in treatments: 
            index_list.append(tup[0])
        return index_list

        

if __name__ == "__main__":

    driver = Driver()

    driver.categories_dataset = 'data/hcpcs_categories.csv'
    driver.concepts_dataset = 'data/concept.csv'
    driver.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
    
    treatment_list = driver.create_treatment_list(driver.concepts_dataset)
    category_list, category_name_set = driver.create_category_list(driver.categories_dataset)

    category_dict_list_hcpcs = driver.create_category_files(driver.category_description_dataset, category_name_set) 
    category_treatment_dict = driver.create_category_treatment_dict(driver.categories_dataset, driver.concepts_dataset)
    category_treatment_dict_list = driver.create_category_treatment_list(category_treatment_dict)

    print(category_dict_list_hcpcs['A'][5])

    s = Search("A", "Rotary air transport")
    rel_treatment_tuples = s.find_possible_treatments()
    print("here")
    rel_treatment_list = s.get_treatment_list(rel_treatment_tuples)
    for i in rel_treatment_list: 
        print(category_dict_list_hcpcs['A'][i]+" "+category_treatment_dict['A'][category_dict_list_hcpcs['A'][i]].treatment_name)


    # test_treatment_codes = ['A0021', 'B4034', 'C1300'] # load list of treatment HCPCS
    # test_treatment_descriptions_long = ['Ambulance service, outside state per mile, transport (medicaid only)', 'Enteral feeding supply kit; syringe fed, per day, includes but not limited to feeding/flushing syringe, administration set tubing, dressings, tape','Hyperbaric oxygen under pressure, full body chamber, per 30 minute interval']
    # test_treatment_descriptions_short = ['Outside state ambulance serv', 'Enter feed supkit syr by day','Hyperbaric oxygen']
    # test_categories = [] # pull in query
    # test_query = 'A0020' # pull in query
    # test_query_category = '' # pull in query
    #
    # search = Search()
    # search.add_treatments(test_treatment_descriptions_long, test_treatment_codes, test_categories)
    # search.new_query("A", test_query_category, test_query)
    
    #results = search.find_possible_treatments(test_query_category, test_query) # treatment list

        