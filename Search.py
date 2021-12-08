from meta import Meta
from driver import Driver
from CSVParser import CSVParser
from Treatment import Treatment
import json

class Search:
    treatment_codes = []  # one dim
    treatment_long_description_list = []  # two (2) dims ?
    categories = []
    treatment_object_list = []
    category_dataset = 'data/hcpcs_categories.csv'
    category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
    concepts_dataset = 'data/concept.csv'

    def __init__(self, query):
        #self.category_code = category_code
        self.query = query

    def find_possible_treatments(self):
        m = Meta()
        relevant_treatments = m.search_inverted_index(self.query)
    
        if len(relevant_treatments) == 0:
#            #print("We've found a treatment!")
#        else: 
            print("Did not find treatment. You'll need try again and enter with another description or HCPCS code.")
            return 1
        rel_treatment_objects = self.get_treatment_objects(self.get_treatment_list(relevant_treatments))
        
        return rel_treatment_objects

    def print_treatment_info(treatments):
        # TODO: print (for each treatment) treatment name, treatment price, hospital name, hospital location, hospital link
        pass
    
    def get_treatment_list(self, treatments):
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
        #relevant_treatment_objs = {}
        relevant_treatment_objs = []
        index_treatment_set = set()
        f = (open('files_for_config/all_treatments.csv', 'a'))

        for l in category_descriptions: 
            index_treatment_set.add(l['hcpcs_code'])
            index_treatment_objs.append(treatment_obj_index[l['hcpcs_code']])
            f.write("%s %s %s \n" % (l['hcpcs_code'], l['short_description'], l['long_description']))
        
        for j in treatments: 
            if j['concept_code'] not in index_treatment_set:
                index_treatment_objs.append(treatment_obj_index[j['concept_code']])
                f.write("%s %s \n" % (j['concept_code'], j['concept_name']))

        f.close()
        if len(rel_treatment_list) != 0: 
            print("We Found Treatment Matches! ")
            for i in rel_treatment_list: 
                #print(index_treatment_objs[i].concept_id)
                #relevant_treatment_objs[index_treatment_objs[i].concept_code] = index_treatment_objs[i]
                relevant_treatment_objs.append(index_treatment_objs[i].concept_id)
        else: 
            print("No Found Matches")

        return relevant_treatment_objs

if __name__ == "__main__":

    #driver = Driver()

    #driver.categories_dataset = 'data/hcpcs_categories.csv'
    #driver.concepts_dataset = 'data/concept.csv'
    #driver.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
    
    #treatment_list = driver.create_treatment_list(driver.concepts_dataset)
    #driver.set_treatment_list(treatment_list)
    #category_list, category_name_set = driver.create_category_list(driver.categories_dataset)
    #driver.set_category_list(category_list)
    #driver.set_category_name_set(category_name_set)


    #category_dict_list_hcpcs = driver.create_category_files(driver.category_description_dataset, category_name_set) 
    #category_treatment_dict = driver.create_category_treatment_dict(driver.category_name_set, driver.categories_dataset, driver.concepts_dataset)
    #category_treatment_dict_list = driver.create_category_treatment_list(category_treatment_dict)
    #driver.set_category_dict_list_hcpcs(category_dict_list_hcpcs)
    #driver.set_category_treatment_dict(category_treatment_dict)
    #driver.set_category_treatment_dict_list(category_treatment_dict_list)

    test_query = "office visits"
    print("Test Query: ", test_query)
    
    s = Search(test_query)
    rel_treatment_tuples = s.find_possible_treatments()
    print(json.dumps(rel_treatment_tuples, sort_keys = False, indent = 3))

        