from meta import Meta
from driver import Driver
from CSVParser import CSVParser
from Treatment import Treatment

class Search:
    treatment_codes = []  # one dim
    treatment_long_description_list = []  # two (2) dims ?
    categories = []
    treatment_object_list = []
    category_dataset = 'data/hcpcs_categories.csv'
    category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
    concepts_dataset = 'data/concept.csv'

    def __init__(self, category_code, query):
        self.category_code = category_code
        self.query = query

    def find_possible_treatments(self):
        m = Meta()
        relevant_treatments = m.search_inverted_index(self.query)
        return relevant_treatments

        # 3. print out treatments, their hospitals, price, hospital link, etc, in a nice format
        # print_treatment_info(relevant_treatments)

    def find_treatments(self):
        if self.query in self.treatment_codes: # HOLD : assume passed HCPCS code
            print("Matched a treatment!")
            return self.query
        print("Did not find treatment. Please enter search with another description or HCPCS code.")

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
    
    def create_treatment_hcpcs_index(treatment_obj_list): 
        """
        Creates a dict of treatment_id (keys) and treatment objects (values)
        """
        treatment_index = {}

        for treatment_obj in treatment_obj_list:
            treatment_index[treatment_obj.concept_code] = treatment_obj

        return treatment_index

    def get_treatment_objects(self, rel_treatment_list):
        # TODO: 
        treatments = CSVParser.readfile_to_dict(self.concepts_dataset)
        treatment_obj_index = {}

        for t in treatments:
            treatment_obj_index[t['concept_code']] = Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name'])
 
        categories = CSVParser.readfile_to_dict(self.category_dataset)
        category_name_set = set()
        for line in categories:
            category_name_set.add(line['category_letter'])

        category_descriptions = CSVParser.readfile_to_dict(self.category_description_dataset)
        index_treatment_objs = []
        relevant_treatment_objs = []
        #f = (open('files_for_config/all_treatments.csv', 'a'))

        for l in category_descriptions: 
            index_treatment_objs.append(treatment_obj_index[l['hcpcs_code']])
            #f.write("%s %s %s \n" % (l['hcpcs_code'], l['short_description'], l['long_description']))
        
        #f.close()
        if rel_treatment_list is not []: 
            print("Best Matches: ")
            for i in rel_treatment_list: 
                print(index_treatment_objs[i].treatment_name)
                relevant_treatment_objs.append(index_treatment_objs[i].treatment_name)
        else: 
            print("No Found Matches")

        return relevant_treatment_objs

if __name__ == "__main__":

    

    driver = Driver()

    driver.categories_dataset = 'data/hcpcs_categories.csv'
    driver.concepts_dataset = 'data/concept.csv'
    driver.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
    
    treatment_list = driver.create_treatment_list(driver.concepts_dataset)
    driver.set_treatment_list(treatment_list)
    category_list, category_name_set = driver.create_category_list(driver.categories_dataset)
    driver.set_category_list(category_list)
    driver.set_category_name_set(category_name_set)


    category_dict_list_hcpcs = driver.create_category_files(driver.category_description_dataset, category_name_set) 
    category_treatment_dict = driver.create_category_treatment_dict(driver.category_name_set, driver.categories_dataset, driver.concepts_dataset)
    category_treatment_dict_list = driver.create_category_treatment_list(category_treatment_dict)
    driver.set_category_dict_list_hcpcs(category_dict_list_hcpcs)
    driver.set_category_treatment_dict(category_treatment_dict)
    driver.set_category_treatment_dict_list(category_treatment_dict_list)

    test_category = "A"
    test_query = "air"
    print("Test Query Category Letter: ", test_category)
    print("Test Query: ", test_query)
    
    s = Search(test_category, test_query)
    rel_treatment_tuples = s.find_possible_treatments()
    
    rel_treatment_list = s.get_treatment_list(rel_treatment_tuples)
    rel_treatment_objects = s.get_treatment_objects(rel_treatment_list)


    #if rel_treatment_list is []: 
     #   print("Best Matches: ")
      #  for i in rel_treatment_list: 
       #     print(category_dict_list_hcpcs['A'][i]+" "+category_treatment_dict['A'][category_dict_list_hcpcs['A'][i]].treatment_name)
    #else: 
     #   print("No Found Matches")


    #for testing
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

        